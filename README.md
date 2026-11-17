# Skills THATMUCH

Bibliothèque de skills pour les agents de l'équipe. Chaque skill est un dossier avec un `SKILL.md` (format [Agent Skills](https://agentskills.io) : frontmatter `name` + `description`, puis les instructions). Le même dossier sert à Cursor, Claude Code, Codex, un Grok Bot ou un autre agent : on lui montre le fichier, ou on copie le dossier dans son répertoire de skills.

Les instructions d'origine sont conservées. Les noms de dossier sont en kebab-case et identiques au champ `name`. Les valeurs propres à une personne (e-mail, clé, chemin, identité) n'y figurent pas : voir [Réglages personnels](#réglages-personnels).

## Arborescence

```
skills/
├── admin/
│   └── sx-note-de-frais-ligne/
├── ai/
│   └── llm-council/
├── design/
│   ├── experteam-design/
│   ├── pptx-vers-presentation-interactive/
│   └── protocole-design-jobs/
├── marketing/
│   ├── ai-seo/             # + evals/, references/
│   ├── analytics/          # + references/, evals/
│   ├── cold-email/         # + evals/, references/
│   ├── emails/             # + evals/, references/
│   ├── ma-banque-pro-articles/
│   ├── product-marketing/  # + evals/
│   ├── programmatic-seo/   # + evals/, references/
│   ├── seo-audit/          # + references/, evals/
│   ├── social/
│   └── substack-editor/
└── video/
    ├── montage-vlog/       # + retours.md (exemple), voyages/exemple/
    ├── podcast-to-vertical-shorts/
    ├── prompteur-script/
    └── video/              # + evals/, references/
templates/SKILL.template.md
scripts/validate_skills.py
```

Une catégorie regroupe les skills. Le dossier que l'agent charge est celui du slug (`seo-audit/`), pas la catégorie.

## Index

<!-- skills-index:start -->
| Skill | Catégorie | Description |
| --- | --- | --- |
| [sx-note-de-frais-ligne](skills/admin/sx-note-de-frais-ligne/SKILL.md) | admin | Ajouter une ligne de frais (train, taxi, hôtel, repas) avec justificatif dans la note de frais Everwin SX de l'organisation. |
| [llm-council](skills/ai/llm-council/SKILL.md) | ai | When the user wants several LLMs' opinions on a question, a decision cross-checked by a 'council' of models, or asks to run the LLM… |
| [experteam-design](skills/design/experteam-design/SKILL.md) | design | Design system Experteam (by everience) pour créer des sites, landing pages et présentations interactives HTML. À utiliser dès que… |
| [pptx-vers-presentation-interactive](skills/design/pptx-vers-presentation-interactive/SKILL.md) | design | Transforme un PowerPoint (.pptx) en présentation web interactive (HTML publiée en Artifact), en gardant le contenu d'origine et en… |
| [protocole-design-jobs](skills/design/protocole-design-jobs/SKILL.md) | design | Protocole de design "Steve Jobs" : audit simplicité et émotion, note sur 10 et punchline avant toute proposition d'interface, d'écran, de… |
| [ai-seo](skills/marketing/ai-seo/SKILL.md) | marketing | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the… |
| [analytics](skills/marketing/analytics/SKILL.md) | marketing | When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking,"… |
| [cold-email](skills/marketing/cold-email/SKILL.md) | marketing | Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails,… |
| [emails](skills/marketing/emails/SKILL.md) | marketing | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use… |
| [ma-banque-pro-articles](skills/marketing/ma-banque-pro-articles/SKILL.md) | marketing | Rédige des articles de blog SEO pour ma-banque.pro, comparateur de banques professionnelles et néobanques. Utilise ce skill dès que… |
| [product-marketing](skills/marketing/product-marketing/SKILL.md) | marketing | When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,'… |
| [programmatic-seo](skills/marketing/programmatic-seo/SKILL.md) | marketing | When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO,"… |
| [seo-audit](skills/marketing/seo-audit/SKILL.md) | marketing | When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO,"… |
| [social](skills/marketing/social/SKILL.md) | marketing | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, or Facebook,… |
| [substack-editor](skills/marketing/substack-editor/SKILL.md) | marketing | Use when turning a topic or a finished text into a Substack post ready to paste, or when putting an article into the Substack editor as a… |
| [montage-vlog](skills/video/montage-vlog/SKILL.md) | video | À utiliser pour monter un vlog de voyage à partir de rushs bruts (DJI, iPhone, GoPro), d'une journée test jusqu'au film complet. |
| [podcast-to-vertical-shorts](skills/video/podcast-to-vertical-shorts/SKILL.md) | video | When cutting a long podcast or interview video (e.g. YouTube) into viral vertical shorts for TikTok, Reels or YouTube Shorts. |
| [prompteur-script](skills/video/prompteur-script/SKILL.md) | video | Génère un script de prompteur pour vidéos YouTube/réseaux sociaux, à partir de notes/un brouillon existant, d'un simple sujet (une phrase,… |
| [video](skills/video/video/SKILL.md) | video | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. Also use when the user… |
<!-- skills-index:end -->

L'index est produit par `python3 scripts/validate_skills.py --write-index`. La description est le début du champ `description` (en français ou en anglais, selon la skill).

## Installer et utiliser

Copier ou lier **le dossier de la skill** (celui qui contient `SKILL.md` et ses fichiers d'aide). Le nom du lien doit rester le slug.

```bash
# Une skill pour Claude Code
mkdir -p ~/.claude/skills
ln -sfn "$PWD/skills/marketing/seo-audit" ~/.claude/skills/seo-audit

# Les mêmes skills pour Cursor
mkdir -p ~/.cursor/skills
while IFS= read -r dir; do
  ln -sfn "$PWD/$dir" "$HOME/.cursor/skills/$(basename "$dir")"
done < <(find skills -mindepth 2 -maxdepth 2 -type d)
```

| Agent | Où les poser |
| --- | --- |
| Claude Code | `~/.claude/skills/<slug>/` ou `.claude/skills/<slug>/` dans le projet |
| Cursor | `~/.cursor/skills/<slug>/` ou `.cursor/skills/<slug>/` dans le projet |
| Codex et autres agents « skills » | souvent `.agents/skills/<slug>/` ou un dossier `skills/` à la racine du projet |
| N'importe quel agent | donner le chemin du `SKILL.md` et demander de suivre ce fichier |

Dans un projet, on peut aussi versionner un lien vers la skill dont l'équipe a besoin, plutôt que de coller une copie qui vieillit.

## Grok Bot et bots Cursor

Un bot Cursor (y compris un Grok Bot) consomme les skills au même format : un dossier par skill, avec `SKILL.md`. Pour lui en donner :

- lier ou copier les dossiers voulus dans les skills du bot ou du dépôt qu'il ouvre (`.cursor/skills/<slug>/`) ;
- ou citer dans ses instructions le chemin `skills/<catégorie>/<slug>/SKILL.md` de ce dépôt.

Le bot choisit une skill d'après `name` et `description`. On ne met dans ses instructions versionnées ni clé, ni e-mail, ni chemin de machine : ces réglages vont dans la mémoire du bot ou dans ses variables d'environnement. Le détail par skill est dans la section suivante, et dans le `## À personnaliser` des skills concernées.

## Réglages personnels

Certaines skills ont besoin d'une valeur que seule la personne connaît. Cette valeur se range dans la **mémoire ou la config locale de l'agent**, jamais dans un commit. Le dépôt ne contient que des placeholders (`<VOTRE_EMAIL_PERSO>`, etc.).

| Skill | Ce que chaque personne ajoute chez elle |
| --- | --- |
| `sx-note-de-frais-ligne` | `<VOTRE_EMAIL_PERSO>`, `<VOTRE_COMPTE_SNCF>`, `<DOSSIER_DE_TRAVAIL>`, `<URL_CONNEXION_SX>`, `<ORGANISATION>`, `<AFFAIRE_PAR_DEFAUT>` |
| `montage-vlog` | `<CHARTE_GRAPHIQUE>`, `<PROJET_RUSH>`, `<DOSSIER_RETOURS>`, `<MACHINE_RUSH>`, `<DESTINATION>`, `<LANGUE_PAROLE>`, `<DOSSIER_OUTILS_MIX>`, `<DOSSIER_DRIVE>`, plus le nom de l'auteur, de la chaîne et du monteur (le texte dit « l'auteur ») |
| `llm-council` | `OPENROUTER_API_KEY` dans l'environnement de l'agent |
| `ai-seo`, `analytics`, `cold-email`, `emails`, `experteam-design`, `ma-banque-pro-articles`, `pptx-vers-presentation-interactive`, `product-marketing`, `programmatic-seo`, `prompteur-script`, `seo-audit`, `social`, `substack-editor`, `podcast-to-vertical-shorts`, `video` | rien |

Règle : **pas de donnée personnelle ni de secret dans git.** Pas d'e-mail, de mot de passe, de clé, de jeton, de chemin `/workspace/…` propre à un bot, de compte, d'URL de connexion interne, ni de voyage réel. Les journaux de retours et les `voyage.json` réels de `montage-vlog` restent locaux (`retours.local.md`, `voyages/<destination>/`, ignorés par git). `voyages/exemple/` est un exemple fictif.

## Provenance

Pas de `LICENSE` à la racine : les origines diffèrent. Le détail et le texte MIT des skills `analytics`, `seo-audit` et `social` sont dans [NOTICE.md](NOTICE.md).

## Vérifier

```bash
pip install pyyaml
python3 scripts/validate_skills.py
```

Le contrôle vérifie le frontmatter (`name`, `description`, slug = dossier), refuse les e-mails et les chemins `/workspace/` dans les skills, et compare l'index ci-dessus aux fichiers. La même commande tourne sur chaque push et chaque pull request.
