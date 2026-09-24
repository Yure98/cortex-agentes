#!/usr/bin/env python3
"""Instalação recuperável das skills Cortex, sem alterar skills de terceiros."""
import argparse
import json
import shutil
import os
import stat
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def entries():
    return sorted([p.parent.relative_to(ROOT) for p in (ROOT / 'skills').glob('*/SKILL.md')]
                  + [p.relative_to(ROOT) for p in (ROOT / 'commands').glob('*.md')])


def retry_readonly(func, path, exc_info):
    """Retry only a read-only PermissionError; never change ACLs or bypass file locks."""
    error = exc_info[1]
    if not isinstance(error, PermissionError) or Path(path).is_symlink():
        raise error
    mode = os.stat(path).st_mode
    if mode & stat.S_IWUSR:
        raise error
    os.chmod(path, mode | stat.S_IWUSR)
    func(path)


def remove(path):
    if path.is_symlink() or path.is_file():
        try:
            path.unlink()
        except PermissionError:
            retry_readonly(os.unlink, str(path), sys.exc_info())
    elif path.exists():
        shutil.rmtree(path, onerror=retry_readonly)


def copy(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    else:
        shutil.copy2(src, dst)


def safe_target(dest, rel):
    if rel not in entries():
        raise ValueError('caminho não pertence ao manifesto Cortex: ' + str(rel))
    target = dest / rel
    if target.is_symlink() or any(p.is_symlink() for p in (dest, target.parent)):
        raise ValueError('destino simbólico não suportado: ' + str(target))
    return target


def restore(dest, backup, changed=None):
    manifest = json.loads((backup / 'manifest.json').read_text(encoding='utf-8'))
    if manifest['destino'] != str(dest.resolve()):
        raise ValueError('backup pertence a outro destino')
    for item in manifest['arquivos']:
        rel = Path(item['path'])
        safe_target(dest, rel)
        if item['existia'] and not (backup / 'anterior' / rel).exists():
            raise ValueError('backup incompleto: ' + str(rel))
    for item in manifest['arquivos']:
        if changed is not None and Path(item['path']) not in changed:
            continue
        rel = Path(item['path']); target = safe_target(dest, rel)
        remove(target)
        if item['existia']:
            copy(backup / 'anterior' / rel, target)


def _install(dest):
    dest = dest.absolute()
    if dest.is_symlink():
        raise ValueError('destino simbólico não suportado')
    dest.mkdir(parents=True, exist_ok=True)
    paths = entries()
    if {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')} != {
        'prev', 'aposentadoria-pcd', 'aposentadoria-especial', 'auxilio-acidente', 'beneficios-incapacidade', 'bpc-loas', 'calculos-previdenciarios',
        'cortex-maternidade', 'decisor-aposentadoria', 'estagiario-peticoes',
        'pensao-por-morte', 'raio-x-cnis', 'recurso-inss', 'segurado-especial-rural'
    }:
        raise ValueError('pacote incompleto: esperado coordenador prev e treze especialistas')
    for rel in paths:
        safe_target(dest, rel)
        if rel.parts[0] == 'skills' and not (ROOT / rel / '.cortex/protocolo.md').is_file():
            raise ValueError('núcleo ausente: executar scripts/sync_core.py')
    existentes = [str(rel) for rel in paths if (dest / rel).exists()]
    print("Cortex " + VERSION + " | Yure Digital")
    print("Uso exclusivo de clientes autorizados. Compartilhamento sem autorizacao expressa proibido.")
    print("Destino: " + str(dest))
    print("Atualizando " + str(len(existentes)) + " pastas/comandos existentes." if existentes else "Instalacao nova.")
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    backup = dest / 'cortex-backups' / stamp
    backup.mkdir(parents=True)
    manifest = {'destino': str(dest.resolve()), 'arquivos': []}
    with tempfile.TemporaryDirectory(prefix='cortex-stage-') as tmp:
        stage = Path(tmp)
        # Preparar cópias e backup completos antes de tocar nos destinos.
        for rel in paths:
            copy(ROOT / rel, stage / rel)
            exists = (dest / rel).exists()
            manifest['arquivos'].append({'path': rel.as_posix(), 'existia': exists})
            if exists:
                copy(dest / rel, backup / 'anterior' / rel)
        (backup / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
        print('Backup pronto: ' + str(backup))
        changed = []
        try:
            for rel in paths:
                target = safe_target(dest, rel)
                changed.append(rel)
                remove(target)
                copy(stage / rel, target)
        except Exception as error:
            try:
                restore(dest, backup, changed=changed)
            except Exception as recovery_error:
                raise OSError(
                    'Falha ao atualizar: ' + str(error) +
                    '\nRestauracao incompleta: ' + str(recovery_error) +
                    '\nBackup preservado em ' + str(backup) +
                    '\nFeche Claude/editores que estejam usando estas pastas. Nao apague o backup.'
                ) from error
            raise OSError('Atualizacao interrompida; arquivos afetados restaurados. Backup: '
                          + str(backup) + '\nCausa: ' + str(error)) from error
    return backup


def install(dest):
    dest = dest.absolute()
    dest.mkdir(parents=True, exist_ok=True)
    lock = dest / '.cortex-install.lock'
    try:
        fd = lock.open('x')
    except FileExistsError:
        raise ValueError('outra instalacao esta em andamento; se foi interrompida, confira o backup antes de remover ' + str(lock))
    try:
        fd.close()
        return _install(dest)
    finally:
        lock.unlink(missing_ok=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dest', type=Path, default=Path.home() / '.claude')
    p.add_argument('--restore', type=Path, help='pasta do backup que será restaurado')
    a = p.parse_args()
    try:
        if a.restore:
            restore(a.dest.absolute(), a.restore)
            print('Versão anterior restaurada.')
        else:
            backup = install(a.dest)
            print('Cortex ' + VERSION + ' instalado. Coordenador /prev e treze especialistas instalados. Abra uma nova sessão do Claude Code e use /prev seguido do caso.')
            if shutil.which('claude') is None:
                print('Claude Code nao foi localizado no PATH. Se ainda nao estiver instalado, consulte https://code.claude.com/docs/en/setup e entre na sua conta antes de usar /prev.')
            print('Backup das personalizações e versão anterior: ' + str(backup))
            print('Para restaurar: python3 scripts/install.py --dest "' + str(a.dest) + '" --restore "' + str(backup) + '"')
    except (ValueError, OSError) as e:
        p.exit(1, 'Instalação não concluída: ' + str(e) + '\n')

if __name__ == '__main__':
    if sys.version_info < (3, 10):
        raise SystemExit('Python 3.10 ou superior necessário.')
    main()
