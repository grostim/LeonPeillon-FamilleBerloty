# La famille Berloty — Léon Peillon

Transcription du tapuscrit **« Des débuts modestes de Claude Denis Berloty et Scholastique Bonaventure Poulat à la fortune immobilière laissée par leur fils F.F. Berloty en 1871 »**, signé **L. P., Février 1988**, attribué à **Léon Peillon** d'après les tampons du document.

Projet préparé sur le modèle de [grostim/FelixBerloty](https://github.com/grostim/FelixBerloty) : photographies sources conservées, transcription éditée, notes du transcripteur, édition LaTeX et exports PDF, EPUB et Markdown. Les onze photographies ont été transcrites ; les lectures incertaines et contradictions restent signalées. Il ne s'agit pas d'une vérification historique des actes cités.

## Lire et corriger

- [Transcription complète](transcription.md), avec notes et repères des pages sources dans les commentaires.
- [Conventions de transcription](CONVENTIONS_TRANSCRIPTION.md).
- [Relevé des incohérences et annotations](RELEVE_EDITORIAL.md).
- [Originaux et correspondance des noms](Originaux/manifest.csv).
- [Source LaTeX générée](edition/main.tex).

Après construction locale : [PDF](output/pdf/Leon_Peillon_Famille_Berloty.pdf), [EPUB](output/Leon_Peillon_Famille_Berloty.epub), [Markdown exporté](output/Leon_Peillon_Famille_Berloty.md). Ces sorties sont générées et exclues du versionnement ; elles sont également disponibles comme artefacts d'une exécution réussie de la CI. Aucun lien de release distante n'est annoncé tant qu'une publication n'a pas eu lieu.

## Contenu

L'essai retrace les origines rurales des Berloty et Poulat, leur installation à Bourg puis à Lyon, la carrière notariale de François Félix Berloty, ses acquisitions immobilières et le partage de sa succession, notamment à Ouroux, Vauxrenard, Vougy et Lyon. Le NOTA final porte sur les quais du Puits-au-Sel, de la Peyrollerie et Pierre Scize.

Le texte comporte plusieurs contradictions conservées et annotées : âge de Claude Denis, année de naissance de Bonaventure, décès de Scholastique Bonaventure et date d'achat de la maison rue Gasparin. Les indications de 1838 et 1887 conduisent aussi à un intervalle de 49 ans, arrondi à « cinquante ans » par l'auteur. Une propriété attribuée à Denise n'est pas nommée dans la phrase originale.

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

Corriger `transcription.md`, puis reconstruire ; ne pas modifier directement `edition/main.tex`. La pagination de l'édition est indépendante des onze pages photographiées. Les trois parties du corps sont éditoriales ; elles sont identifiées dans l'avertissement.

## Intégration continue

Le workflow construit les trois formats et conserve les artefacts sur les mises à jour, propositions et lancements manuels. Une release est publiée uniquement lors d'un envoi explicite de tag `v*`. La création d'un dépôt distant, les commits, les tags et l'envoi sur GitHub restent des opérations distinctes de la construction locale.

## Provenance

Onze photographies fournies pour ce projet : `IMGP0080.JPG` à `IMGP0090.JPG`, respectivement `Originaux/Page 01.jpg` à `Originaux/Page 11.jpg`. Transcription visuelle réalisée avec Codex le 20 octobre 2026 ; corrections manuscrites lisibles intégrées, annotations hors texte décrites séparément. Aucune licence de redistribution des archives familiales n'est présumée.
