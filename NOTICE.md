# Provenance et licences

Ce dépôt n'a pas de fichier `LICENSE` unique. Les skills n'ont pas toutes la même origine, et une seule licence couvrirait mal le mélange.

## Skills marketing importées (MIT)

`ai-seo`, `analytics`, `cold-email`, `emails`, `product-marketing`, `programmatic-seo`, `seo-audit`, `social` et `video` viennent de [marketingskills](https://github.com/coreyhaines31/marketingskills) (Corey Haines). Les versions indiquées dans leur frontmatter sont celles qui ont été importées. Le texte d'instructions n'a pas été réécrit ; `source` et `license` ont été ajoutés au frontmatter.

Copyright (c) 2025 Corey Haines

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

`podcast-to-vertical-shorts` est une adaptation de la skill `video` du même dépôt (reprise telle quelle sous `skills/video/video/`). Le texte présent ici n'est pas une copie intégrale.

## Autres sources

- `llm-council` s'appuie sur la méthode de [karpathy/llm-council](https://github.com/karpathy/llm-council). Ce dépôt amont n'a pas de fichier `LICENSE`.
- `substack-editor` indique dans son texte être adapté de `lifegenieai/substack-editor`. Aucune licence n'était identifiable dans les fichiers importés.
- `experteam-design`, `pptx-vers-presentation-interactive`, `ma-banque-pro-articles`, `prompteur-script`, `montage-vlog` et `sx-note-de-frais-ligne` sont des skills d'équipe. Elles sont versionnées sans licence séparée.

## Skills reprises de l'environnement Claude

Copiées telles quelles depuis les skills utilisées au quotidien dans Claude et d'autres agents. Chaque dossier garde son fichier de licence quand il en a un.

- **Apache 2.0 (Anthropic)** : `docx`, `pdf`, `pptx`, `xlsx`, `canvas-design` (avec les polices sous licence OFL de leurs auteurs) et `skill-creator`. Chaque dossier contient son `LICENSE.txt`.
- **Apache 2.0 (plugins officiels Claude)** : `frontend-design` et `claude-md-improver` (plugin `claude-md-management`).
- **MIT (Vercel)** : `vercel-react-best-practices` (déclaré dans son frontmatter). `find-skills` vient du dépôt `vercel-labs/skills` ; aucune licence n'est présente dans le fichier importé.
- **Sans licence identifiable dans les fichiers importés** : `deep-research` et `google-workspace` (skills d'exemple Anthropic), et les 19 skills `figma-*` (plugin Figma officiel pour Claude, sauf `figma-implement-design` et `figma-create-design-system-rules`, issues des skills synchronisées). Elles sont conservées pour l'usage interne de l'équipe ; à retirer si Figma ou Anthropic l'exigent.

Non reprises : `built-in-browser`, `chrome-browser` et `computer-use` (« All rights reserved » Anthropic), ainsi que `docs`, `morning` et `import-memory`, qui dépendent de fonctions propres à l'application Claude.

Tant que l'équipe n'a pas choisi une licence pour l'ensemble, ne pas considérer le dépôt comme réutilisable au-delà de THATMUCH, sauf les extraits MIT ci-dessus, qui restent sous MIT.
