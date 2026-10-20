#!/usr/bin/env python3
"""Construit LaTeX, PDF et EPUB à partir du texte relu en Markdown."""
from pathlib import Path
import argparse
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
STEM = 'Leon_Peillon_Famille_Berloty'

def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-only', action='store_true')
    args = parser.parse_args()
    (ROOT / 'edition').mkdir(exist_ok=True)
    run('pandoc', 'transcription.md', '--from=markdown', '--to=latex', '--standalone',
        '--top-level-division=chapter', '--template=scripts/template.tex',
        '--lua-filter=scripts/pages.lua', '--wrap=none', '--output=edition/main.tex')
    if args.source_only:
        return
    out = ROOT / 'output'
    (out / 'pdf').mkdir(parents=True, exist_ok=True)
    scratch = ROOT / 'tmp' / 'latex'
    scratch.mkdir(parents=True, exist_ok=True)
    for _ in range(2):
        run('pdflatex', '-interaction=nonstopmode', '-halt-on-error',
            f'-output-directory={scratch}', 'edition/main.tex')
    shutil.copyfile(scratch / 'main.pdf', out / 'pdf' / f'{STEM}.pdf')
    run('pandoc', 'transcription.md', '--to=epub3', '--toc', '--split-level=1',
        f'--output=output/{STEM}.epub')
    shutil.copyfile(ROOT / 'transcription.md', out / f'{STEM}.md')

if __name__ == '__main__':
    main()
