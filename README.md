# La famille Berloty — Léon Peillon

[![Validation LaTeX et publication](https://github.com/grostim/LeonPeillon-FamilleBerloty/actions/workflows/ci-release.yml/badge.svg)](https://github.com/grostim/LeonPeillon-FamilleBerloty/actions/workflows/ci-release.yml)

Transcription du docuement  **« Des débuts modestes de Claude Denis Berloty et Scholastique Bonaventure Poulat à la fortune immobilière laissée par leur fils F.F. Berloty en 1871 »**, signé **L. P., Février 1988**, attribué à **Léon Peillon** .

### Télécharger la dernière édition

Les liens suivants pointent vers les livrables de la dernière release réussie et nécessitent l'accès au dépôt privé :

| Format | Téléchargement |
| --- | --- |
| PDF | [Édition paginée](https://github.com/grostim/LeonPeillon-FamilleBerloty/releases/latest/download/Leon_Peillon_Famille_Berloty.pdf) |
| EPUB | [Édition pour liseuse](https://github.com/grostim/LeonPeillon-FamilleBerloty/releases/latest/download/Leon_Peillon_Famille_Berloty.epub) |
| Markdown | [Texte exporté](https://github.com/grostim/LeonPeillon-FamilleBerloty/releases/latest/download/Leon_Peillon_Famille_Berloty.md) |

[Historique des releases](https://github.com/grostim/LeonPeillon-FamilleBerloty/releases). Les sorties locales restent disponibles dans `output/` après construction et sont exclues du versionnement.

## Contenu

L'essai retrace les origines rurales des Berloty et Poulat, leur installation à Bourg puis à Lyon, la carrière notariale de François Félix Berloty, ses acquisitions immobilières et le partage de sa succession, notamment à Ouroux, Vauxrenard, Vougy et Lyon. Le NOTA final porte sur les quais du Puits-au-Sel, de la Peyrollerie et Pierre Scize.


## Structure

```text
Originaux/                  Onze JPG inchangés et manifest.csv avec SHA-256
transcription.md            Source éditoriale complète
edition/main.tex            Source LaTeX générée, ouvrable dans l'éditeur
scripts/build.py            Construction reproductible des trois formats
scripts/template.tex        Mise en page LaTeX
scripts/pages.lua           Conservation des repères photographiques
CONVENTIONS_TRANSCRIPTION.md
RELEVE_EDITORIAL.md
.github/workflows/ci-release.yml
output/                     Livrables générés (non versionnés)
```

## Construire

Installer Python 3, Pandoc et TeX Live avec `pdflatex`, `babel-french`, `lmodern`, `geometry`, `parskip`, `fancyhdr` et `hyperref`. Sous Debian/Ubuntu, la CI utilise les paquets `texlive-latex-base`, `texlive-latex-recommended`, `texlive-latex-extra`, `texlive-lang-french`, `texlive-fonts-recommended`, `lmodern`, `cm-super` et `pandoc`.

Depuis la racine :

```sh
python3 scripts/build.py
```

Pour régénérer seulement le source LaTeX :

```sh
python3 scripts/build.py --source-only
```

Corriger `transcription.md`, puis reconstruire ; ne pas modifier directement `edition/main.tex`. La pagination de l'édition est indépendante des onze pages photographiées. Les titres des deux parties du récit sont éditoriaux ; le NOTA final appartient au tapuscrit. Les conventions et interventions de transcription sont documentées dans `CONVENTIONS_TRANSCRIPTION.md` et `RELEVE_EDITORIAL.md`.

## Intégration continue

La [pipeline de FelixBerloty](https://github.com/grostim/FelixBerloty/blob/master/.github/workflows/ci-release.yml) est reprise avec les noms de ce projet. Elle calcule la prochaine version depuis le plus grand tag `v*` (ou `v0.0.0`), selon le titre du dernier commit : `feat` incrémente la majeure ; `fix`, `style`, `refactor`, `docs` ou `correction` incrémentent la mineure ; les autres titres incrémentent le correctif.

Après installation des dépendances, elle régénère `edition/main.tex` depuis le Markdown, injecte le numéro de version dans une copie `edition/main.release.tex`, compile le PDF en deux passes puis exporte Markdown et EPUB depuis cette même copie LaTeX avec Pandoc. Les trois formats sont conservés comme artefacts. Chaque push sur `main` ou `master` publie automatiquement le tag calculé et une release contenant les trois fichiers ; les propositions et lancements manuels valident la construction sans publication. Le tag cible le commit qui a déclenché la pipeline.

## Provenance

Onze photographies fournies pour ce projet : `IMGP0080.JPG` à `IMGP0090.JPG`, respectivement `Originaux/Page 01.jpg` à `Originaux/Page 11.jpg`. Transcription visuelle réalisée avec Codex le 20 octobre 2026 ; corrections manuscrites lisibles intégrées, annotations hors texte décrites séparément. Aucune licence de redistribution des archives familiales n'est présumée.
