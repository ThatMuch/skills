# Contribuer une skill

Une skill est un mode d'emploi qu'un agent peut charger. Elle doit marcher pour n'importe qui dans l'équipe, pas seulement pour la personne qui l'a écrite.

## 1. Choisir la catégorie

Les catégories actuelles :

| Dossier | Contenu |
| --- | --- |
| `skills/marketing/` | stratégie produit, mesure, e-mailing, réseaux sociaux |
| `skills/seo/` | référencement naturel : audit, pages à grande échelle, visibilité dans les IA |
| `skills/redaction/` | écriture d'articles et de posts (blog, newsletter) |
| `skills/design/` | méthodes et protocoles de design, présentations interactives (valables pour toute charte) |
| `skills/video/` | script, montage et déclinaisons vidéo |
| `skills/ai/` | modèles, agents et SDK d'IA (Genkit, LLM Council) |
| `skills/firebase/` | plateforme Firebase : CLI, auth, Firestore, hosting, Data Connect, AI Logic |
| `skills/dev/` | règles et conventions de code |
| `skills/experteam/` | tout ce qui est propre à Experteam (charte, note de frais, outils internes) : à mettre ici plutôt que dans une catégorie générale |

S'il en faut une nouvelle, créer `skills/<categorie>/` avec un slug en kebab-case (minuscules, chiffres, tirets). Une catégorie = un regroupement, pas une skill.

## 2. Créer le dossier

```
skills/<categorie>/<skill-slug>/SKILL.md
```

`<skill-slug>` est le nom de la skill en kebab-case. Il est **identique** au champ `name` du frontmatter. Partir de [templates/SKILL.template.md](templates/SKILL.template.md).

```yaml
---
name: skill-slug
description: >-
  Quand utiliser cette skill, en une fois : la tâche, les formulations
  typiques, et ce qu'il ne faut pas confondre avec une autre skill.
---
```

`description` est le texte qui fait choisir la skill. Le garder concret, sous 1024 caractères. Le corps du fichier est la marche à suivre. Ne pas y glisser d'autre copie du même mode d'emploi sous un autre nom.

## 3. Fichiers d'aide

Tout ce que la skill ouvre (références, grilles d'évaluation, exemples) reste **à côté** du `SKILL.md` :

```
skills/<categorie>/<skill-slug>/
├── SKILL.md
├── references/
└── evals/
```

Les liens internes sont relatifs (`references/note.md`), pour que le dossier reste déplaçable.

## 4. Données personnelles et secrets

On ne committe jamais :

- e-mails, noms de personnes, comptes, URLs de connexion propres à une organisation ou à une personne ;
- mots de passe, clés d'API, jetons ;
- chemins de machine (`/workspace/…`, dossier personnel, disque d'un bot) ;
- voyages, journaux de retours ou exports qui identifient quelqu'un.

À la place, un placeholder explicite dans la skill, par exemple `<VOTRE_EMAIL_PERSO>`, `<DOSSIER_DE_TRAVAIL>`, `<URL_CONNEXION_SX>`. Chaque skill qui en a besoin ouvre une section `## À personnaliser` près du début : le placeholder, quoi y mettre, et où le ranger (mémoire ou config locale de l'agent, **jamais** dans le dépôt).

Ensuite, ajouter une ligne au tableau [Réglages personnels](README.md#réglages-personnels) du README : skill → ce que chaque personne doit configurer chez elle.

Les fichiers vraiment locaux portent un suffixe ignoré par git (`retours.local.md`, `*.local.json`) ou vivent sous un dossier déjà dans `.gitignore` (les `voyages/<destination>/` de `montage-vlog`, hors `voyages/exemple/`).

## 5. Mettre à jour l'index

```bash
pip install pyyaml
python3 scripts/validate_skills.py --write-index
python3 scripts/validate_skills.py
```

La deuxième commande doit afficher le nombre de skills valides. Elle contrôle le frontmatter, l'égalité nom / dossier, l'absence d'e-mail et de chemin `/workspace/` dans `skills/`, et la concordance de l'index. Le workflow GitHub Actions lance le même contrôle sur chaque push et chaque pull request.

## 6. Pull request

Branche à part, message de commit qui dit quelle skill est ajoutée ou modifiée. Dans la description de la PR : la skill, la catégorie, et la liste des placeholders s'il y en a. Pas de donnée réelle à la place des placeholders.
