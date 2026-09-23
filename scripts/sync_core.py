"""Distribui o núcleo canônico; --check detecta divergência sem modificar arquivos."""
from pathlib import Path
import argparse
import shutil

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--check', action='store_true')
a = p.parse_args()
erros = []
for skill in sorted((ROOT / 'skills').glob('*/SKILL.md')):
    for src in (ROOT / 'core').iterdir():
        if not src.is_file():
            continue
        dst = skill.parent / '.cortex' / src.name
        if a.check:
            if not dst.exists() or src.read_bytes() != dst.read_bytes():
                erros.append(str(dst.relative_to(ROOT)))
        else:
            dst.parent.mkdir(exist_ok=True)
            shutil.copy2(src, dst)
if erros:
    p.exit(1, '\n'.join(erros) + '\n')
