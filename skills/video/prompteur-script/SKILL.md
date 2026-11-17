---
name: prompteur-script
description: Génère un script de prompteur pour vidéos YouTube/réseaux sociaux, à partir de notes/un brouillon existant, d'un simple sujet (une phrase, une question) sans notes, ou d'une URL (article, page web, vidéo) à transformer en script. Utilise ce skill dès que l'utilisateur dit avoir besoin d'un script, d'un script pour son prompteur, veut transformer des notes/idées/un lien en script, ou donne un sujet/une question en demandant d'en faire un script pour une vidéo. Déclenche-toi même si l'utilisateur ne mentionne pas explicitement le mot "prompteur".
---

# Générateur de script de prompteur

Ce skill génère un script prêt à être lu au prompteur, pour une vidéo YouTube ou réseaux sociaux. Deux modes d'entrée possibles.

## Déterminer le mode d'entrée

- **Mode "notes/brouillon"** : l'utilisateur fournit des notes, un brouillon, une liste de points déjà rédigés.
- **Mode "sujet"** : l'utilisateur donne juste un sujet, une phrase ou une question, sans contenu préexistant (ex : "fais-moi un script sur pourquoi le café est mauvais pour le sommeil", "un script sur comment j'ai monté ma boîte").
- **Mode "URL"** : l'utilisateur fournit un lien (article, page web, vidéo YouTube, etc.) comme base du script.

## Processus

1. **Récupérer l'input** : notes/brouillon si fournis, sinon URL si un lien est donné, sinon traiter comme un sujet.
   - En mode notes : ne jamais inventer de contenu qui ne provient pas des notes — le rôle du skill est de structurer et mettre en forme, pas de créer le fond à sa place.
   - En mode sujet : le skill doit générer le contenu lui-même à partir du sujet donné. Utiliser ses connaissances générales, et faire une recherche web si le sujet demande des faits précis, récents, ou vérifiables (chiffres, actualité, données techniques) plutôt que d'inventer. Si le sujet est trop vague pour être traité directement (ex : juste "le sport"), poser une question rapide pour cadrer l'angle avant de rédiger.
   - En mode URL : récupérer le contenu de la page avec l'outil de fetch web. Baser le script sur le contenu réel de la page — ne pas inventer d'éléments absents de la source. Si la page est inaccessible (paywall, connexion requise, etc.), le signaler à l'utilisateur et demander les infos clés à la place. Respecter les règles de citation/copyright habituelles : reformuler avec ses propres mots, ne jamais reproduire de longs passages du texte source tels quels.
2. **Clarifier si besoin** (une seule fois, rapidement) :
   - Durée visée approximative (par défaut : long format, 10 min+, sauf indication contraire)
   - En mode sujet, si l'angle n'est pas clair, demander l'angle souhaité (ex : avis personnel, tutoriel, retour d'expérience, analyse) avant de rédiger
   - En mode URL, si la page couvre plusieurs sujets distincts, confirmer l'angle ou la partie à privilégier
   - Si l'input ne couvre visiblement qu'un format court, adapter la structure en conséquence (voir section "Adapter la structure selon la durée")
3. **Rédiger le script** en suivant la structure ci-dessous.
4. **Livrer le résultat** :
   - Si le script est court/moyen, ou si l'utilisateur discute et itère activement dessus → l'afficher directement dans la conversation.
   - Si le script est long (10 min+) ou si l'utilisateur demande explicitement un fichier → le livrer en fichier téléchargeable (.docx). Utiliser le skill docx (`/mnt/skills/public/docx/SKILL.md`) pour la création du fichier Word.
   - En cas de doute sur le format de livraison, demander à l'utilisateur.

## Structure du script (format long, 10 min+)

Toujours suivre cet enchaînement, sauf si l'utilisateur demande explicitement une structure différente :

1. **Hook (0-15s)** — Accroche percutante : question, promesse, statistique choc, ou teasing du résultat final. Doit capter l'attention dès la première phrase.
2. **[GÉNÉRIQUE]** — Repère à placer juste après le hook, par défaut, pour indiquer l'emplacement de l'habillage/jingle d'intro de la chaîne. Ne jamais écrire de texte de présentation type "Salut, moi c'est [nom]" — le générique remplace cette fonction. Ne pas demander à l'utilisateur s'il en a un : partir du principe qu'il en a un et l'insérer systématiquement.
3. **Intro rapide (après le générique)** — Directement ce que la vidéo va apporter concrètement au spectateur, sans re-présentation personnelle.
4. **Contenu principal** — Découpé en 3 à 6 parties/chapitres clairs, basés sur les notes fournies. Chaque partie se termine par une mini-transition fluide vers la suivante.
5. **Rappel abonnement** — Placé naturellement au milieu ou vers la fin du contenu principal, intégré dans le flow (pas une coupure brutale).
6. **Conclusion / Récap** — Résumé rapide des points clés vus dans la vidéo.
7. **CTA final** — Abonnement + like + suggestion de prochaine vidéo à regarder ou question à poser en commentaire.

### Adapter la structure selon la durée

- **Format court (< 3 min)** : garder Hook, Intro très brève (voire fusionnée avec le hook), Contenu principal en 1-2 parties, CTA final condensé. Supprimer le rappel abonnement intermédiaire.
- **Format moyen (3-10 min)** : structure complète mais avec 2-4 parties dans le contenu principal au lieu de 3-6.
- **Format long (10 min+)** : structure complète telle que décrite ci-dessus.

## Ton et style

- **Ton dynamique et énergique** par défaut : phrases qui donnent envie, enthousiasme perceptible à l'écrit, sans tomber dans l'excès.
- **Phrases courtes et rythmées** : privilégier des phrases simples, faciles à lire à voix haute sans reprendre son souffle au milieu. Éviter les subordonnées à rallonge.
- **Oral, pas écrit** : écrire comme on parle, pas comme on rédige un article. Utiliser des tournures naturelles à l'oral ("Alors,", "Et là,", "Tu vois,").

## Indications de lecture pour le prompteur

Insérer des indications entre parenthèses et en italique aux moments clés, pour guider la lecture :

- *(pause)* — avant une info importante ou après une question posée au spectateur
- *(sourire)* — sur les moments légers, les blagues, l'accroche
- *(ton plus posé)* — sur les passages sérieux ou les explications denses
- *(accélère)* — sur les passages d'énumération rapide ou de transition dynamique

Ne pas surcharger le texte : une indication toutes les 3-4 phrases maximum, uniquement quand elle apporte une vraie aide à la lecture.

## Exemple de format de sortie

```
[SOMMAIRE]
Partie 1 — [Titre]
Partie 2 — [Titre]
...

[HOOK]
Tu galères encore à [problème] ? *(pause)* Dans cette vidéo, je te montre exactement comment [bénéfice], étape par étape.

[GÉNÉRIQUE]

[INTRO]
Aujourd'hui, on attaque un sujet que plein de gens loupent : [sujet]. *(sourire)* Accroche-toi, ça va être dense.

[PARTIE 1 — Titre]
...

[RAPPEL ABONNEMENT]
D'ailleurs, si t'es pas encore abonné... *(sourire)* tu sais ce qu'il te reste à faire.

[PARTIE 2 — Titre]
...

[CONCLUSION]
Pour résumer : *(ton plus posé)* [récap en 2-3 points].

[CTA FINAL]
Si cette vidéo t'a aidé, laisse un like, abonne-toi, et dis-moi en commentaire [question engageante].
```

## Découpage pour la lecture au prompteur

Pour les scripts longs (moyen et long format), découper visuellement le texte pour faciliter le défilement et la lecture :

- Séparer chaque partie/chapitre du contenu principal par un titre repère clair (ex : `[PARTIE 1 — Titre]`), sur sa propre ligne, avec une ligne vide avant et après.
- À l'intérieur d'une partie, si elle dépasse environ 150-200 mots, insérer des sauts de paragraphe supplémentaires toutes les 3-4 phrases pour éviter les blocs de texte compacts difficiles à suivre à l'oral.
- Ne jamais couper une phrase en plein milieu entre deux blocs — le découpage doit toujours tomber sur une fin de phrase ou de idée.
- Pour un format long (10 min+), ajouter au début du script un sommaire rapide des parties (ex : liste des titres de `[PARTIE 1]` à `[PARTIE N]`) pour que l'utilisateur puisse se repérer avant de lancer la lecture.

## Points d'attention

- **Mode notes** : rester fidèle au fond des notes de l'utilisateur, ne pas ajouter de faits, chiffres ou affirmations qui n'y figurent pas. Si les notes sont incomplètes sur un point clé, le signaler plutôt que d'inventer.
- **Mode sujet** : vérifier les faits précis (chiffres, dates, données techniques) par recherche web plutôt que de les inventer de mémoire. Rester factuellement prudent — signaler à l'utilisateur si une information nécessiterait une vérification qu'il devrait faire lui-même avant publication.
- **Mode URL** : baser le script sur le contenu réel récupéré, reformulé avec ses propres mots. Ne pas citer de longs passages tels quels.
- Toujours garder le ton dynamique même sur les parties techniques/complexes — c'est le style demandé par défaut, sauf indication contraire de l'utilisateur.
