---
name: experteam-design
description: Design system Experteam (by everience) pour créer des sites, landing pages et présentations interactives HTML. À utiliser dès que l'utilisateur demande une page, un site, un deck ou un webinaire "aux couleurs d'Experteam", "dans le même style que la présentation Initiation à l'IA", ou réutilise ce design. Fournit palette, typographies, composants, patterns d'interaction et règles de contenu.
---

# Design Experteam

Style issu de la présentation interactive « Initiation à l'IA » (webinaire interne Experteam). Sobre, bleu marine et cyan, typographie géométrique, interactions pédagogiques. À appliquer tel quel sur tout nouveau site ou présentation, sauf instruction contraire de l'utilisateur.

## 1. Identité

- **Marque :** Experteam by everience. Logo blanc (SVG) sur fond marine, logo couleur sur fond clair. Ne jamais déformer, recolorer ni ajouter d'effet.
- **Ton :** professionnel, direct, pédagogique. Tutoiement ou vouvoiement selon le contexte, phrases courtes, verbes d'action.
- **Langue :** français, typographie française (espace avant `:` `?` `!`, guillemets « », apostrophe typographique ’).

## 2. Palette (tokens CSS)

```css
:root{
  --navy:#0C3E73;      /* couleur de marque, titres, fonds de section */
  --navy-deep:#072348; /* fond sombre profond, dégradés */
  --cyan:#2CAFCF;      /* accent unique : chiffres, liens actifs, barres */
  --cyan-soft:#E6F5FA; /* fond de callout, surbrillance */
  --slate:#4F6479;     /* texte secondaire, labels */
  --coral:#D6705C;     /* alertes, "à retenir", points d'attention */
  --amber:#E3A857;     /* niveau intermédiaire */
  --mint:#96CDB6;      /* succès doux */
  --paper:#F7FAFC;     /* fond de page */
  --card:#FFFFFF;      /* cartes */
  --line:#D6E4F2;      /* bordures, séparateurs */
  --ink:#10263F;       /* texte principal */
}
```

Règles : un seul accent (cyan). Le corail sert uniquement aux alertes et risques. Vert `#2E8B62` réservé aux validations. Fond sombre : dégradé `radial-gradient(120% 90% at 85% 10%, #165291 0%, var(--navy) 45%, var(--navy-deep) 100%)`.

## 3. Typographie

Google Fonts, avec fallbacks réels :

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
```

```css
--f-display:"Montserrat","Mont","Segoe UI",system-ui,sans-serif; /* titres, chiffres */
--f-body:"Source Sans 3","Source Sans Pro","Segoe UI",system-ui,sans-serif; /* texte */
--f-mono:"JetBrains Mono",ui-monospace,Menlo,monospace; /* labels, horaires, indices */
```

| Rôle | Réglage |
|---|---|
| H2 de slide | Montserrat 800, `clamp(26px,3.6vw,44px)`, navy, `text-wrap:balance` |
| H3 | Montserrat 700, `clamp(17px,1.6vw,20px)`, navy |
| Grand chiffre / année | Montserrat 800, cyan, `clamp(56px,9vw,120px)`, `tabular-nums` |
| Eyebrow | Montserrat 700, 12px, majuscules, `letter-spacing:.14em`, slate (partie section en cyan) |
| Lead | Source Sans 3, `clamp(18px,1.8vw,22px)`, slate, 62ch max |
| Indice d'interaction | JetBrains Mono 12px, préfixe `↳` cyan |

## 4. Structure d'une présentation

- Une slide = un écran. Plein cadre, `.inner` centré `max-width:1180px`, gap `clamp(16px,2.4vw,28px)`.
- Alternance : slides claires (`--paper`) pour le contenu, slides navy dégradé pour couverture, séparateurs de section et conclusion.
- **Couverture :** logo blanc, pastille mono « Webinaire interne · n sur N », H1 géant (`clamp(46px,8vw,104px)`) avec le mot clé en cyan, auteurs.
- **Séparateur de section :** gros numéro cyan (`03`), H2 blanc, sous-titre `#CFE0F0`.
- **Chaque slide de contenu :** eyebrow `SECTION · SUJET` → H2 → contenu → callout de conclusion → indice d'interaction.
- **Rail de navigation en bas :** marque, barre de progression segmentée cliquable (séparateurs aux changements de section), compteur `01 / 20`, boutons vue d'ensemble, plein écran, précédent, suivant.
- **Raccourcis :** ← → Espace, `G` vue d'ensemble, `F` plein écran, `Échap` ferme, `Home`/`End`. Swipe sur mobile. Hash `#n` pour lier une slide.
- Transition : fondu + glissement 24px, 0,35 s. Respecter `prefers-reduced-motion`.

## 5. Composants

- **Carte :** fond blanc, bordure 1px `--line`, rayon 12px, padding 20px. Pas d'ombre. Ne pas multiplier les cartes imbriquées.
- **Callout :** `border-left:4px solid cyan`, fond `--cyan-soft`, texte navy 600, rayon `0 8px 8px 0`. Variante `warn` : bordure corail, fond `#FBEDEA`, texte `#7A2E1F`.
- **Bouton :** pilule, bordure 1.5px navy, fond blanc ; au survol fond navy. Variante `primary` : fond navy, survol cyan.
- **Chip / pastille de date :** fond `--cyan-soft`, rayon 10px, date en gras navy, horaire en mono slate.
- **Liste numérotée :** chiffre Montserrat 800 cyan à gauche, texte à droite. Numéroter seulement quand l'ordre a un sens.
- **Frise :** points sur une ligne `--line`, remplissage cyan progressif, point courant agrandi avec contour navy.
- **Illustrations animées :** cadre 16/9, 320px max, fond dégradé navy, rayon 10px, légende mono 11px « (illustration) ».
- **Icônes :** SVG au trait, 2px, `stroke-linecap:round`, couleur navy. Pas d'emoji comme marqueurs de section.

## 6. Patterns d'interaction (à privilégier)

Toujours rendre la slide interactive quand le contenu s'y prête, sans casser la lecture au repos :

| Contenu | Interaction |
|---|---|
| Liste de choix, étapes | Cartes cliquables qui ouvrent un panneau de détail |
| Chronologie | Frise cliquable + flèches ↑ ↓ ; média associé à la date |
| Hiérarchie de concepts | Cercles imbriqués cliquables |
| Catégories | Exercice de tri ou de classement avec score et retour immédiat |
| Fait vs invention | Quiz vrai/faux avec explication |
| Définitions | Cartes retournables (question au recto, réponse au verso) |
| Bonnes pratiques | Liste à cocher avec jauge de progression |
| Comparaison A/B | Bascule à deux boutons qui change les valeurs |
| Check-list de sécurité | Questions oui/non qui débloquent un bouton final |
| Mécanisme technique | Démo pas à pas (ex. prédiction du mot suivant) |

Règles : état initial déjà rempli (jamais de coquille vide), retour visible à chaque clic, focus clavier visible, nettoyer les `setInterval` au changement d'état.

## 7. Contraintes techniques (pages publiées en Artifact)

- Fichier unique `.html`, `<title>` court (2 à 4 mots), pas de `<html>`/`<head>`/`<body>`.
- Scripts externes uniquement depuis cdnjs, jsdelivr, unpkg ; styles uniquement Google Fonts. **Toute image, GIF ou logo doit être intégré en `data:` URI** (les images distantes sont bloquées sans erreur).
- Pas de `alert`/`confirm`, pas de téléchargement par lien, pas d'iframe externe.
- Mobile : gouttière ≥16px, grilles `repeat(auto-fit,minmax(min(100%,260px),1fr))`, aucun scroll horizontal.
- Thème : tokens sur `:root`, `body` avec fond explicite. La présentation d'origine est claire par défaut ; pour un site, ajouter les blocs sombres (`prefers-color-scheme` + `[data-theme]`) en redéfinissant seulement les tokens.
- Médias tiers : demander l'accord avant tout téléchargement, créditer la source en légende, préférer une illustration créée plutôt qu'une capture de marque.

## 8. Adapter à un site web

- **Navigation :** barre fine blanche, logo à gauche, liens Montserrat 700 13px, CTA pilule navy.
- **Hero :** fond navy dégradé, H1 Montserrat 800 avec un mot en cyan, une phrase d'appui, un CTA. Hauteur selon le contenu, pas `100vh`.
- **Sections :** alterner `--paper` et blanc, titres avec eyebrow, grilles de cartes 3 colonnes qui passent à 1 sur mobile.
- **Preuve / chiffres :** grands chiffres cyan Montserrat en tête de carte, seulement si ce sont les messages clés.
- **Pied de page :** fond `--navy-deep`, logo blanc, liens `#A9C3DD`.

## 9. À éviter

- Dégradés violet/bleu génériques, fond crème + serif, accents multiples.
- Texte centré partout, rayon identique sur tous les blocs, ombres décoratives.
- Emoji comme puces, numérotation sans ordre réel.
- Texte légal ou chiffre inventé présenté comme réel : toute donnée illustrative est marquée « exemple » ou « illustration ».

## 10. Check-list avant publication

1. Palette et polices viennent des tokens ci-dessus.
2. Chaque slide a eyebrow, H2, contenu, indice d'interaction si pertinent.
3. Logo présent en couverture et conclusion, intégré en data URI.
4. Navigation clavier, tactile et barre de progression fonctionnent.
5. Rendu vérifié à 400px de large, sans scroll horizontal.
6. Dates, noms et chiffres relus contre la source fournie par l'utilisateur.
7. Chaque interaction testée au moins une fois (clic sur chaque élément).
