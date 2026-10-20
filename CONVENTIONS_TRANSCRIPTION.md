# Conventions de transcription

Adaptation des [conventions de FelixBerloty](https://github.com/grostim/FelixBerloty/blob/master/CONVENTIONS_TRANSCRIPTION.md), consultées le 20 octobre 2026. Le présent texte est une transcription de Léon Peillon et ne doit pas être attribué à Félix Berloty.

## Texte et sources

- Lecture visuelle des onze photographies fournies, dans l'ordre IMGP0080.JPG à IMGP0090.JPG ; correspondance et empreintes SHA-256 dans `Originaux/manifest.csv`. Les photographies sont copiées sans modification.
- `transcription.md` est la source éditoriale unique. `edition/main.tex` est généré par Pandoc : corriger le Markdown puis régénérer pour éviter toute divergence entre PDF, EPUB et texte.
- Conserver les paragraphes et réunir les phrases qui traversent les pages 5–6, 8–9 et 9–10. Les repères photographiques sont des commentaires, y compris dans le LaTeX généré ; ils ne forcent pas la pagination de l'édition.
- Le titre est celui de la première page. Les titres de parties sont éditoriaux et annoncés comme tels. Le séparateur page 5 est représenté par le début de la deuxième partie. Le NOTA final demeure une partie distincte ; il n'est pas transformé en note du transcripteur.

## Normalisations

- Corriger les I/O employés pour 1/0, espaces mécaniques, césures et coquilles grammaticales évidentes ; conserver les tournures de l'auteur, même maladroites.
- Passer les noms de personnes et lieux en casse usuelle. Conserver les graphies du document sans inventer une identification géographique ou généalogique ; notamment Trefort, Lagneu, Lantigne, Saint Savin-Moncarra, St. Genest-Malifaux.
- Conserver les abréviations, unités et dates telles que formulées (Frs, frs, Ha, Km, dates numériques). Espaces et guillemets sont adaptés à la typographie française.
- Intégrer les corrections manuscrites lisibles, notamment « deux » page 3, « lui » et « est » page 6, « chez » page 8, « à » page 10. En cas de doute, donner une lecture accompagnée d'une note explicite.
- Le soulignement d'insistance page 7 est rendu en gras dans les formats dérivés.

## Appareil critique

- Toute note ajoutée commence par « (Note du transcripteur) ».
- Ne pas rectifier silencieusement les incohérences de dates, âges ou montants. Les hypothèses sont formulées comme telles et restent distinctes d'une vérification d'état civil, qui n'a pas été menée.
- Sur confirmation du responsable du projet, une correction peut être intégrée au récit avec une note indiquant la leçon originale et la date de confirmation. Le 20 octobre 2026 : décès de Scholastique Bonaventure en 1883, borne d'achat rue Gasparin en 1871, naissance de Bonaventure en 1856, âge de Claude Denis au décès de 73 ans. La lacune pour la propriété de Denise est conservée ; les lectures Lijobard de Chappe, Briort et Gouverdriat sont confirmées sans identification externe.
- Les annotations de possession hors texte ne sont pas intégrées au récit ; elles sont décrites dans `RELEVE_EDITORIAL.md`.
- La signature finale a été relue sur un agrandissement : « L. P. Février 1988 ».

## Construction et versionnement

- Source LaTeX : classe `report`, 11 pt, A4, marges de 2,5 cm, Latin Modern, Babel français, en-têtes et liens discrets ; modèle adapté à un essai court sans portrait fourni.
- `python3 scripts/build.py` produit PDF (deux passes), EPUB et copie Markdown. Les dépendances sont documentées dans le README.
- La CI reprend la pipeline de FelixBerloty : version calculée à partir du plus grand tag `v*` et du titre du dernier commit (`feat` → majeure ; `fix`/`style`/`refactor`/`docs`/`correction` → mineure ; autres → correctif). Base sans tag : `v0.0.0`.
- Après régénération du LaTeX depuis le Markdown, la CI injecte cette version dans `edition/main.release.tex`, compile le PDF en deux passes et génère les exports Markdown et EPUB depuis cette copie LaTeX. Chaque push sur `main` ou `master` publie automatiquement une release et ses trois livrables. Les propositions et lancements manuels construisent les artefacts sans publier.
- Si des commits sont créés, utiliser les Conventional Commits en français (`feat:`, `fix:`, `docs:`, `style:`, `chore:`). Aucun dépôt distant ou tag n'est créé par le script de construction.

## Avancement

11/11 pages transcrites et relues sur les images fournies ; les six points principaux ont été arbitrés par le responsable du projet le 20 octobre 2026 et leur traitement est consigné dans le relevé éditorial. Restent à confirmer la fraction après « une coupée », l'ajout du chiffre 3 dans les articles de l'achat de bois et les annotations manuscrites hors récit.
