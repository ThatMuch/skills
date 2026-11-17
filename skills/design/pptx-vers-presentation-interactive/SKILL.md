---
name: pptx-vers-presentation-interactive
description: Transforme un PowerPoint (.pptx) en présentation web interactive (HTML publiée en Artifact), en gardant le contenu d'origine et en ajoutant des interactions pédagogiques (frise, quiz, tri, cartes retournables, comparaisons, check-lists). À utiliser quand l'utilisateur fournit un .pptx et demande une "présentation interactive", "version web", "version code" ou "transforme mes slides". S'appuie sur le skill experteam-design pour le style.
---

# PowerPoint vers présentation interactive

Méthode éprouvée sur la présentation « Initiation à l'IA » (20 slides). Elle produit un seul fichier `.html`, publié avec l'outil Artifact.

## Principes

1. **Le contenu d'origine ne bouge pas.** Tous les textes, dans le même ordre. L'interaction s'ajoute, elle ne remplace pas.
2. **Tout ce que tu inventes est signalé.** Quiz, exemples, légendes, schémas : mention « illustration » ou « exemple » sur la page, et liste récapitulative à l'utilisateur à la fin.
3. **Aucun téléchargement sans accord.** Annoncer nom du fichier, source et taille, attendre un oui explicite, à chaque média.
4. **Les données de l'utilisateur font foi.** Dates, noms, chiffres : reprendre ses captures et textes, signaler toute incohérence au lieu de trancher seul.

## Étapes

### 1. Extraire le PowerPoint

```bash
mkdir x && cd x && unzip -q -o "fichier.pptx"
```

- **Ordre réel des slides** : lire `ppt/presentation.xml` (liste des `r:id`) et `ppt/_rels/presentation.xml.rels`. Les noms `slideN.xml` ne reflètent pas l'ordre.
- **Texte** : extraire les `<a:t>` de chaque slide, paragraphe par paragraphe.
- **Notes du présentateur** : `ppt/notesSlides/` si présent, à reprendre dans le contenu ou à signaler.
- **Couleurs et polices** : compter les `srgbClr` des slides et lire `ppt/theme/theme1.xml`.
- **Logo** : regarder `ppt/media/` (SVG en priorité, PNG sinon). Ouvrir l'image pour vérifier ce que c'est. Un logo blanc SVG sert sur fond sombre.

Si la charte est celle d'Experteam, appliquer le skill `experteam-design`. Sinon, déduire une palette de 4 à 6 tokens des couleurs réellement utilisées et deux polices.

### 2. Plan des slides

Faire une table interne : numéro, section, titre, type de contenu, interaction choisie. Regrouper par section (sommaire, parties, conclusion). Une slide de titre de section devient un séparateur sombre.

Choix de l'interaction selon le contenu :

| Contenu de la slide | Interaction |
|---|---|
| Liste d'étapes ou d'épisodes | Cartes cliquables + panneau de détail |
| Dates, historique | Frise cliquable avec média par date |
| Concepts emboîtés | Cercles imbriqués cliquables |
| Deux catégories d'exemples | Exercice de tri avec score |
| Erreurs, pièges, mythes | Quiz vrai/faux avec explication |
| Définitions, biais | Cartes retournables |
| Bonnes pratiques | Liste à cocher + jauge |
| Comparaison A/B | Bascule à deux boutons |
| Niveaux (public/interne/sensible) | Classement d'items avec retour immédiat |
| Check-list de contrôle | Oui/non qui débloque un bouton final |
| Processus technique | Démo pas à pas |
| Texte simple (objectifs, garanties) | Mise en page soignée, pas d'interaction forcée |

Ne pas forcer une interaction : une slide qui se lit bien reste statique. Ne pas répéter un même élément de pied de slide sur toutes les variantes d'un composant (une phrase de conclusion liée à une seule date ne s'affiche que pour cette date).

### 3. Construire le HTML

- Un seul fichier, écrit dans le dossier du projet. Structure : `<title>`, `<style>`, `<div class="deck">` (slides + rail de navigation), vue d'ensemble, `<script>`.
- Navigation : flèches, Espace, `G` vue d'ensemble, `F` plein écran, swipe, hash `#n`, barre de progression cliquable.
- Chaque slide a des tokens de style communs, un eyebrow `SECTION · SUJET`, un H2, le contenu, éventuellement un callout et un indice d'interaction.
- État initial toujours rempli (premier élément sélectionné par défaut).
- Un `setInterval` d'animation doit être arrêté quand l'utilisateur change d'état.
- Médias : tout en `data:` URI (les images distantes sont bloquées par la politique de sécurité des Artifacts). Logo SVG inline de préférence.

### 4. Médias demandés par l'utilisateur

1. Si l'utilisateur donne une URL ou un code d'intégration : expliquer que l'image doit être intégrée au fichier, demander l'accord (fichier, source, taille), puis `curl` dans le dossier temporaire, vérifier avec `file`, encoder en base64.
2. Si l'utilisateur demande « trouve des images » : chercher, mais si aucun lien direct fiable n'apparaît, proposer une illustration animée créée (SVG/CSS/JS) plutôt que de télécharger au hasard. Éviter les captures de produits de marque.
3. Toujours une légende : source ou « illustration ».
4. Si un GIF dépasse quelques Mo, le signaler avant de l'intégrer. Le fichier final doit rester sous 16 Mo.

### 5. Vérifier

- Contrôle de syntaxe du script : extraire le contenu de `<script>` dans un fichier et lancer `node --check`.
- Dans le navigateur d'aperçu : cliquer chaque élément interactif et comparer l'affichage au contenu attendu (boucler sur les boutons avec `javascript_tool`). Un fichier qui contient des médias lourds peut ne pas s'ouvrir dans l'aperçu : le dire à l'utilisateur plutôt que de prétendre l'avoir testé.
- Largeur mobile (≈400px) : pas de scroll horizontal.
- Relire dates, noms et chiffres contre la source fournie.
- Erreur classique : une virgule oubliée dans un tableau de données JS fait échouer tous les éléments suivants sans message visible. Tester chaque entrée, pas seulement la première.

### 6. Publier et rendre compte

- Publier avec l'outil Artifact. Pour modifier : même chemin de fichier, ce qui garde le lien.
- Le lien est privé : prévenir que les autres personnes ne peuvent l'ouvrir qu'après partage depuis le menu Partager.
- Réponse finale : lien, liste des interactions par slide, **liste de ce qui a été inventé** (quiz, exemples, légendes, schémas), ce qui n'a pas pu être testé, incohérences repérées dans la source.

## Itérations fréquentes

- Ajouter des dates ou des liens : demander les URLs d'inscription avant d'ajouter des boutons.
- Changer un ordre : mettre à jour cartes, données, textes de renvoi (ex. « sujet du webinaire 4 ») et rejouer le test de chaque élément.
- Supprimer un champ de saisie prévu pour l'oral : retirer HTML, CSS et JS associés, puis relancer `node --check`.
- Quand l'utilisateur envoie une capture : lire le défaut sur l'image avant de corriger, reproduire par script si possible, corriger la cause et non le symptôme.
