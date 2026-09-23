#!/usr/bin/env python3
"""Instalação recuperável das skills Cortex, sem alterar skills de terceiros."""
import argparse
import json
import shutil
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def entries():
    return sorted([p.parent.relative_to(ROOT) for p in (ROOT / 'skills').glob('*/SKILL.md')]
                  + [p.relative_to(ROOT) for p in (ROOT / 'commands').glob('*.md')])


def remove(path):
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


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


def restore(dest, backup):
    manifest = json.loads((backup / 'manifest.json').read_text(encoding='utf-8'))
    if manifest['destino'] != str(dest.resolve()):
        raise ValueError('backup pertence a outro destino')
    for item in manifest['arquivos']:
        rel = Path(item['path'])
        safe_target(dest, rel)
        if item['existia'] and not (backup / 'anterior' / rel).exists():
            raise ValueError('backup incompleto: ' + str(rel))
    for item in manifest['arquivos']:
        rel = Path(item['path']); target = safe_target(dest, rel)
        remove(target)
        if item['existia']:
            copy(backup / 'anterior' / rel, target)


def install(dest):
    dest = dest.absolute()
    if dest.is_symlink():
        raise ValueError('destino simbólico não suportado')
    dest.mkdir(parents=True, exist_ok=True)
    paths = entries()
    if {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')} != {
        'prev', 'aposentadoria-pcd', 'auxilio-acidente', 'calculos-previdenciarios',
        'cortex-maternidade', 'decisor-aposentadoria', 'estagiario-peticoes',
        'pensao-por-morte', 'raio-x-cnis', 'recurso-inss'
    }:
        raise ValueError('pacote incompleto: esperado coordenador prev e nove especialistas')
    for rel in paths:
        safe_target(dest, rel)
        if rel.parts[0] == 'skills' and not (ROOT / rel / '.cortex/protocolo.md').is_file():
            raise ValueError('núcleo ausente: executar scripts/sync_core.py')
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
        try:
            for rel in paths:
                target = safe_target(dest, rel)
                remove(target)
                copy(stage / rel, target)
        except Exception:
            restore(dest, backup)
            raise
    return backup


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
            print('Coordenador /prev e nove especialistas instalados. Abra uma nova sessão do Claude Code e use /prev seguido do caso.')
            print('Backup das personalizações e versão anterior: ' + str(backup))
            print('Para restaurar: python3 scripts/install.py --dest "' + str(a.dest) + '" --restore "' + str(backup) + '"')
    except (ValueError, OSError) as e:
        p.exit(1, 'Instalação não concluída: ' + str(e) + '\n')

if __name__ == '__main__':
    if sys.version_info < (3, 10):
        raise SystemExit('Python 3.10 ou superior necessário.')
    main()
