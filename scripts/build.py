#!/usr/bin/env python3
"""Construit PDF, EPUB et Markdown depuis le source LaTeX versionné."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
STEM = 'Leon_Peillon_Famille_Berloty'

def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)

def main():
    out = ROOT / 'output'
    (out / 'pdf').mkdir(parents=True, exist_ok=True)
    scratch = ROOT / 'tmp' / 'latex'
    scratch.mkdir(parents=True, exist_ok=True)
    for _ in range(2):
        run('pdflatex', '-interaction=nonstopmode', '-halt-on-error',
            f'-output-directory={scratch}', 'edition/main.tex')
    shutil.copyfile(scratch / 'main.pdf', out / 'pdf' / f'{STEM}.pdf')
    run('pandoc', 'edition/main.tex', '--from=latex', '--to=epub3', '--toc', '--toc-depth=2',
        '--metadata=title=La famille Berloty — Des débuts modestes à la fortune immobilière',
        '--metadata=author=Léon Peillon', '--metadata=language=fr',
        f'--output=output/{STEM}.epub')
    run('pandoc', 'edition/main.tex', '--from=latex', '--to=gfm', '--wrap=none',
        f'--output=output/{STEM}.md')

if __name__ == '__main__':
    main()
