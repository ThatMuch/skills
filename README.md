# Skills THATMUCH

Bibliothèque de skills pour les agents de l'équipe. Chaque skill est un dossier avec un `SKILL.md` (format [Agent Skills](https://agentskills.io) : frontmatter `name` + `description`, puis les instructions). Le même dossier sert à Cursor, Claude Code, Codex, un Grok Bot ou un autre agent : on lui montre le fichier, ou on copie le dossier dans son répertoire de skills.

Les instructions d'origine sont conservées. Les noms de dossier sont en kebab-case et identiques au champ `name`. Les valeurs propres à une personne (e-mail, clé, chemin, identité) n'y figurent pas : voir [Réglages personnels](#réglages-personnels).

## Arborescence

```
skills/
├── agents/           # outils pour travailler avec les agents (skills, CLAUDE.md)
│   ├── claude-md-improver/
│   ├── find-skills/
│   └── skill-creator/
├── ai/               # modèles, agents, SDK d'IA et recherche
│   ├── deep-research/
│   ├── developing-genkit-dart/
│   ├── developing-genkit-go/
│   ├── developing-genkit-js/
│   ├── developing-genkit-python/
│   └── llm-council/
├── design/           # méthodes et outils de design, génériques
│   ├── canvas-design/
│   ├── frontend-design/
│   ├── pptx-vers-presentation-interactive/
│   └── protocole-design-jobs/
├── dev/              # règles, conventions et bonnes pratiques de code
│   ├── antigravity-rules/
│   ├── react-19/
│   ├── review/
│   └── vercel-react-best-practices/
├── documents/        # Word, PDF, PowerPoint, Excel, Google Workspace
│   ├── docx/
│   ├── google-workspace/
│   ├── pdf/
│   ├── pptx/
│   └── xlsx/
├── experteam/        # spécifique Experteam, mis de côté
│   ├── experteam-design/
│   └── sx-note-de-frais-ligne/   # note de frais Everwin SX
├── figma/            # design et code autour de Figma
│   ├── figma-3d-transforms/
│   ├── figma-code-connect/
│   ├── figma-code-workflows/
│   ├── figma-create-design-system-rules/
│   ├── figma-create-new-file/
│   ├── figma-design-to-code/
│   ├── figma-generate-design/
│   ├── figma-generate-diagram/
│   ├── figma-generate-library/
│   ├── figma-generative-plugins/
│   ├── figma-implement-design/
│   ├── figma-implement-motion/
│   ├── figma-shaders/
│   ├── figma-spec/
│   ├── figma-swiftui/
│   ├── figma-use/
│   ├── figma-use-figjam/
│   ├── figma-use-motion/
│   └── figma-use-slides/
├── firebase/         # plateforme Firebase
│   ├── firebase-ai-logic/
│   ├── firebase-app-hosting-basics/
│   ├── firebase-auth-basics/
│   ├── firebase-basics/
│   ├── firebase-data-connect/
│   ├── firebase-firestore-enterprise-native-mode/
│   ├── firebase-firestore-standard/
│   ├── firebase-hosting-basics/
│   └── firestore-security-rules-auditor/
├── git/              # commits et publication de versions
│   ├── git-commit/
│   └── release-publisher/
├── marketing/        # stratégie, mesure, e-mailing, réseaux
│   ├── analytics/                # + references/, evals/
│   ├── cold-email/               # + evals/, references/
│   ├── emails/                   # + evals/, references/
│   ├── product-marketing/        # + evals/
│   └── social/
├── projet/           # gestion de projet et tickets
│   └── linear/
├── redaction/        # écriture d'articles et de posts
│   ├── ma-banque-pro-articles/
│   └── substack-editor/
├── seo/              # référencement naturel et IA
│   ├── ai-seo/                   # + evals/, references/
│   ├── programmatic-seo/         # + evals/, references/
│   └── seo-audit/                # + references/, evals/
├── supabase/         # base de données et backend Supabase
│   ├── supabase/
│   └── supabase-postgres-best-practices/
├── video/            # production et montage vidéo
│   ├── montage-vlog/             # + retours.md (exemple), voyages/exemple/
│   ├── podcast-to-vertical-shorts/
│   ├── prompteur-script/
│   └── video/                    # + evals/, references/
└── wordpress/        # thèmes et plugins WordPress
    ├── wordpress-pro/
    └── wordpress-themes/
templates/SKILL.template.md
scripts/validate_skills.py
```

Une catégorie regroupe les skills par thème. Le dossier que l'agent charge est celui du slug (`seo-audit/`), pas la catégorie.

`experteam/` met à part les skills propres à Experteam (charte, note de frais Everwin SX). Les autres catégories restent utilisables par n'importe qui : on ne lie `experteam/` que pour un travail destiné à Experteam. `pptx-vers-presentation-interactive` reste dans `design/` : sa méthode vaut pour toute charte, et elle ne cite `experteam-design` que comme option de style.

## Index

<!-- skills-index:start -->
| Skill | Catégorie | Description |
| --- | --- | --- |
| [claude-md-improver](skills/agents/claude-md-improver/SKILL.md) | agents | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for… |
| [find-skills](skills/agents/find-skills/SKILL.md) | agents | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that… |
| [skill-creator](skills/agents/skill-creator/SKILL.md) | agents | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch,… |
| [deep-research](skills/ai/deep-research/SKILL.md) | ai | Use this skill when the user's prompt requires (1) researching a topic across multiple sources, comparing options or alternatives,… |
| [developing-genkit-dart](skills/ai/developing-genkit-dart/SKILL.md) | ai | Generates code and provides documentation for the Genkit Dart SDK. Use when the user asks to build AI agents in Dart, use Genkit flows, or… |
| [developing-genkit-go](skills/ai/developing-genkit-go/SKILL.md) | ai | Develop AI-powered applications using Genkit in Go. Use when the user asks to build AI features, agents, flows, or tools in Go using… |
| [developing-genkit-js](skills/ai/developing-genkit-js/SKILL.md) | ai | Develop AI-powered applications using Genkit in Node.js/TypeScript. Use when the user asks about Genkit, AI agents, flows, or tools in… |
| [developing-genkit-python](skills/ai/developing-genkit-python/SKILL.md) | ai | Develop AI-powered applications using Genkit in Python. Use when the user asks about Genkit, AI agents, flows, or tools in Python, or when… |
| [llm-council](skills/ai/llm-council/SKILL.md) | ai | When the user wants several LLMs' opinions on a question, a decision cross-checked by a 'council' of models, or asks to run the LLM… |
| [canvas-design](skills/design/canvas-design/SKILL.md) | design | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a… |
| [frontend-design](skills/design/frontend-design/SKILL.md) | design | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction,… |
| [pptx-vers-presentation-interactive](skills/design/pptx-vers-presentation-interactive/SKILL.md) | design | Transforme un PowerPoint (.pptx) en présentation web interactive (HTML publiée en Artifact), en gardant le contenu d'origine et en… |
| [protocole-design-jobs](skills/design/protocole-design-jobs/SKILL.md) | design | Protocole de design "Steve Jobs" : audit simplicité et émotion, note sur 10 et punchline avant toute proposition d'interface, d'écran, de… |
| [antigravity-rules](skills/dev/antigravity-rules/SKILL.md) | dev | Règles de l'Agent Antigravity - Stack React 19 + Zustand, including Linus Torvalds code quality and Steve Jobs design protocols. |
| [react-19](skills/dev/react-19/SKILL.md) | dev | React 19 patterns with React Compiler. Trigger: When writing React components - no useMemo/useCallback needed. |
| [review](skills/dev/review/SKILL.md) | dev | Revue de code critique et pragmatique, dans l'esprit de Linus Torvalds : structures de données, complexité, risque de rupture, sécurité,… |
| [vercel-react-best-practices](skills/dev/vercel-react-best-practices/SKILL.md) | dev | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or… |
| [docx](skills/documents/docx/SKILL.md) | documents | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word templates (.dotx). Triggers… |
| [google-workspace](skills/documents/google-workspace/SKILL.md) | documents | Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or changes a Google file. Use… |
| [pdf](skills/documents/pdf/SKILL.md) | documents | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining… |
| [pptx](skills/documents/pptx/SKILL.md) | documents | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks,… |
| [xlsx](skills/documents/xlsx/SKILL.md) | documents | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit,… |
| [experteam-design](skills/experteam/experteam-design/SKILL.md) | experteam | Design system Experteam (by everience) pour créer des sites, landing pages et présentations interactives HTML. À utiliser dès que… |
| [sx-note-de-frais-ligne](skills/experteam/sx-note-de-frais-ligne/SKILL.md) | experteam | Ajouter une ligne de frais (train, taxi, hôtel, repas) avec justificatif dans la note de frais Everwin SX de l'organisation. |
| [figma-3d-transforms](skills/figma/figma-3d-transforms/SKILL.md) | figma | Add or edit 3D transforms — depth, perspective, z-axis rotation, tilt, isometric, and parallax looks that flat 2D rotation cannot express.… |
| [figma-code-connect](skills/figma/figma-code-connect/SKILL.md) | figma | Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code… |
| [figma-code-workflows](skills/figma/figma-code-workflows/SKILL.md) | figma | Import or upload local HTML or project files into Figma, choose editable Design frames, runnable Code Layers or standalone Code (also… |
| [figma-create-design-system-rules](skills/figma/figma-create-design-system-rules/SKILL.md) | figma | Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my… |
| [figma-create-new-file](skills/figma/figma-create-new-file/SKILL.md) | figma | Always use this skill when the user wants to create a new Figma Design, FigJam, or Slides file. You MUST invoke this skill BEFORE every… |
| [figma-design-to-code](skills/figma/figma-design-to-code/SKILL.md) | figma | **MANDATORY prerequisite** — you MUST invoke this skill BEFORE calling the `get_design_context` Figma MCP tool. You MUST trigger this… |
| [figma-generate-design](skills/figma/figma-generate-design/SKILL.md) | figma | Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma.… |
| [figma-generate-diagram](skills/figma/figma-generate-diagram/SKILL.md) | figma | MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading… |
| [figma-generate-library](skills/figma/figma-generate-library/SKILL.md) | figma | Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build… |
| [figma-generative-plugins](skills/figma/figma-generative-plugins/SKILL.md) | figma | **MANDATORY prerequisite** — load this skill before calling `create_generative_plugin` or `update_generative_plugin`. Use when the user… |
| [figma-implement-design](skills/figma/figma-implement-design/SKILL.md) | figma | Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files,… |
| [figma-implement-motion](skills/figma/figma-implement-motion/SKILL.md) | figma | Translates Figma motion and animations into production-ready application code. Use when implementing animation/motion from a Figma design… |
| [figma-shaders](skills/figma/figma-shaders/SKILL.md) | figma | **MANDATORY prerequisite** — load this skill before calling `create_shader` or `update_shader`. Use when the user asks to create, author,… |
| [figma-spec](skills/figma/figma-spec/SKILL.md) | figma | This skill is required to create, read, edit, review, or comment on Figma specs. You must read it when working on a PRD, brief, RFC or any… |
| [figma-swiftui](skills/figma/figma-swiftui/SKILL.md) | figma | SwiftUI ↔ Figma translation. Use whenever the user mentions Swift, SwiftUI, iOS, iPhone, or iPad — in EITHER direction — translating a… |
| [figma-use](skills/figma/figma-use/SKILL.md) | figma | **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without… |
| [figma-use-figjam](skills/figma/figma-use-figjam/SKILL.md) | figma | This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational… |
| [figma-use-motion](skills/figma/figma-use-motion/SKILL.md) | figma | Motion / animation context for the `use_figma` MCP tool — animating Figma nodes via manual keyframes, animation styles, easing, and… |
| [figma-use-slides](skills/figma/figma-use-slides/SKILL.md) | figma | This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational… |
| [firebase-ai-logic](skills/firebase/firebase-ai-logic/SKILL.md) | firebase | Official skill for integrating Firebase AI Logic (Gemini API) into web applications. Covers setup, multimodal inference, structured… |
| [firebase-app-hosting-basics](skills/firebase/firebase-app-hosting-basics/SKILL.md) | firebase | Deploy and manage web apps with Firebase App Hosting. Use this skill when deploying Next.js/Angular apps with backends. |
| [firebase-auth-basics](skills/firebase/firebase-auth-basics/SKILL.md) | firebase | Guide for setting up and using Firebase Authentication. Use this skill when the user's app requires user sign-in, user management, or… |
| [firebase-basics](skills/firebase/firebase-basics/SKILL.md) | firebase | Provides foundational setup, authentication, and project management workflows for Firebase using the Firebase CLI. Use when checking… |
| [firebase-data-connect](skills/firebase/firebase-data-connect/SKILL.md) | firebase | Build and deploy Firebase SQL Connect (aka Firebase Data Connect) backends with PostgreSQL. Use for schema design, GraphQL… |
| [firebase-firestore-enterprise-native-mode](skills/firebase/firebase-firestore-enterprise-native-mode/SKILL.md) | firebase | Comprehensive guide for Firestore enterprise native including provisioning, data model, security rules, and SDK usage. Use this skill when… |
| [firebase-firestore-standard](skills/firebase/firebase-firestore-standard/SKILL.md) | firebase | Comprehensive guide for Firestore Standard Edition, including provisioning, security rules, and SDK usage. Use this skill when the user… |
| [firebase-hosting-basics](skills/firebase/firebase-hosting-basics/SKILL.md) | firebase | Skill for working with Firebase Hosting (Classic). Use this when you want to deploy static web apps, Single Page Apps (SPAs), or simple… |
| [firestore-security-rules-auditor](skills/firebase/firestore-security-rules-auditor/SKILL.md) | firebase | A skill to evaluate how secure Firestore security rules are. Use this when Firestore security rules are updated to ensure that the… |
| [git-commit](skills/git/git-commit/SKILL.md) | git | Execute git commit with conventional commit message analysis, intelligent staging, and message generation. Use when user asks to commit… |
| [release-publisher](skills/git/release-publisher/SKILL.md) | git | Guides publishing release versions of the application using Git flow and Semantic Versioning. Triggers on requests like "publie la… |
| [analytics](skills/marketing/analytics/SKILL.md) | marketing | When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking,"… |
| [cold-email](skills/marketing/cold-email/SKILL.md) | marketing | Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails,… |
| [emails](skills/marketing/emails/SKILL.md) | marketing | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use… |
| [product-marketing](skills/marketing/product-marketing/SKILL.md) | marketing | When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,'… |
| [social](skills/marketing/social/SKILL.md) | marketing | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, or Facebook,… |
| [linear](skills/projet/linear/SKILL.md) | projet | Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear. |
| [ma-banque-pro-articles](skills/redaction/ma-banque-pro-articles/SKILL.md) | redaction | Rédige des articles de blog SEO pour ma-banque.pro, comparateur de banques professionnelles et néobanques. Utilise ce skill dès que… |
| [substack-editor](skills/redaction/substack-editor/SKILL.md) | redaction | Use when turning a topic or a finished text into a Substack post ready to paste, or when putting an article into the Substack editor as a… |
| [ai-seo](skills/seo/ai-seo/SKILL.md) | seo | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the… |
| [programmatic-seo](skills/seo/programmatic-seo/SKILL.md) | seo | When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO,"… |
| [seo-audit](skills/seo/seo-audit/SKILL.md) | seo | When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO,"… |
| [supabase](skills/supabase/supabase/SKILL.md) | supabase | Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron,… |
| [supabase-postgres-best-practices](skills/supabase/supabase-postgres-best-practices/SKILL.md) | supabase | Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this skill BEFORE writing or changing anything that… |
| [montage-vlog](skills/video/montage-vlog/SKILL.md) | video | À utiliser pour monter un vlog de voyage à partir de rushs bruts (DJI, iPhone, GoPro), d'une journée test jusqu'au film complet. |
| [podcast-to-vertical-shorts](skills/video/podcast-to-vertical-shorts/SKILL.md) | video | When cutting a long podcast or interview video (e.g. YouTube) into viral vertical shorts for TikTok, Reels or YouTube Shorts. |
| [prompteur-script](skills/video/prompteur-script/SKILL.md) | video | Génère un script de prompteur pour vidéos YouTube/réseaux sociaux, à partir de notes/un brouillon existant, d'un simple sujet (une phrase,… |
| [video](skills/video/video/SKILL.md) | video | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. Also use when the user… |
| [wordpress-pro](skills/wordpress/wordpress-pro/SKILL.md) | wordpress | Develops custom WordPress themes and plugins, creates and registers Gutenberg blocks and block patterns, configures WooCommerce stores,… |
| [wordpress-themes](skills/wordpress/wordpress-themes/SKILL.md) | wordpress | WordPress custom theme development specialist focused on clean, maintainable code following VIP standards. Includes modular theme… |
<!-- skills-index:end -->

L'index est produit par `python3 scripts/validate_skills.py --write-index`. La description est le début du champ `description` (en français ou en anglais, selon la skill).

## Installer et utiliser

Copier ou lier **le dossier de la skill** (celui qui contient `SKILL.md` et ses fichiers d'aide). Le nom du lien doit rester le slug.

```bash
# Une skill pour Claude Code
mkdir -p ~/.claude/skills
ln -sfn "$PWD/skills/seo/seo-audit" ~/.claude/skills/seo-audit

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

## Ajouter une skill pour tous les agents

Une skill ajoutée ici est utilisable par Claude Code, Cursor, Codex, un Grok Bot ou tout autre agent : le format ne dépend pas de l'agent. La marche à suivre est la même pour une personne et pour un agent. Le détail est dans [CONTRIBUTING.md](CONTRIBUTING.md).

1. **Choisir la catégorie** dans l'[arborescence](#arborescence). Une skill propre à Experteam va dans `skills/experteam/`. Sinon, créer `skills/<categorie>/` en kebab-case.
2. **Créer le dossier** `skills/<categorie>/<slug>/SKILL.md` à partir de [templates/SKILL.template.md](templates/SKILL.template.md). Le slug est identique au champ `name` du frontmatter. `description` dit quand utiliser la skill (sous 1024 caractères) : c'est elle que l'agent lit pour choisir.
3. **Garder les fichiers d'aide à côté** (`references/`, `evals/`, scripts), avec des liens relatifs.
4. **Partir d'une skill déjà installée chez soi** (`~/.claude/skills/`, `.cursor/skills/`, `.agents/skills/`) : copier le dossier entier, puis retirer e-mails, clés, chemins de machine et noms de personnes. Les remplacer par des placeholders (`<VOTRE_EMAIL_PERSO>`) avec une section `## À personnaliser`, et ajouter une ligne au tableau [Réglages personnels](#réglages-personnels).
5. **Noter la provenance** dans [NOTICE.md](NOTICE.md) si la skill vient d'ailleurs : source, licence, ou « licence non identifiée ». Ne pas copier une skill marquée « All rights reserved ».
6. **Mettre à jour l'index et vérifier** :

   ```bash
   pip install pyyaml
   python3 scripts/validate_skills.py --write-index
   python3 scripts/validate_skills.py
   ```

7. **Ouvrir une pull request** : une branche, un message de commit qui nomme la skill, et dans la description sa catégorie et ses placeholders.

À donner tel quel à un agent :

> Ajoute la skill `<slug>` dans `skills/<categorie>/` de ce dépôt en suivant la section « Ajouter une skill pour tous les agents » du README et CONTRIBUTING.md. Pars de `templates/SKILL.template.md`, ne mets aucune donnée personnelle, lance `python3 scripts/validate_skills.py --write-index` puis `python3 scripts/validate_skills.py`, et prépare la pull request sans la fusionner.

Pour qu'un autre agent utilise ensuite la skill, voir [Installer et utiliser](#installer-et-utiliser).

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
