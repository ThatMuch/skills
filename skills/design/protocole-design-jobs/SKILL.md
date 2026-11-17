---
name: protocole-design-jobs
description: >-
  Protocole de design "Steve Jobs" : audit simplicité et émotion, note sur 10
  et punchline avant toute proposition d'interface, d'écran, de parcours ou de
  produit. À utiliser dès qu'on demande une UI, une maquette, une app, un flow
  UX, une landing page, un onboarding, un composant ou une fonctionnalité
  produit, même sans les mots "design" ou "Jobs". Ne remplace pas
  experteam-design (charte graphique Experteam) : le protocole juge la
  simplicité du concept, la charte donne le style.
---

# Protocole de Design "Steve Jobs"

Avant de proposer une interface ou une solution produit, fais une analyse centrée sur l'utilisateur et l'esthétique. Le but : ne livrer que des propositions simples, évidentes et agréables, jamais "fonctionnelles mais fades" ni surchargées. L'analyse est interne : l'utilisateur ne voit que le résultat validé (étape C).

## Étape A : Inspection du design ("Less is More")

Pose-toi ces quatre questions sur ton concept, honnêtement :

1. **Simplicité** : cette interface est-elle si simple qu'un enfant de 5 ans pourrait l'utiliser ? Si elle demande une explication, elle est trop compliquée.
2. **Superflu** : y a-t-il un bouton, une ligne de texte ou une option inutile ? Si oui, supprime-les. Chaque élément doit justifier sa présence.
3. **Magie** : l'expérience est-elle magique ou seulement fonctionnelle ? Où est le "Wow" ?
4. **Hiérarchie visuelle** : l'œil sait-il où regarder en premier, puis ensuite ? Ou est-ce un sapin de Noël ?

### Trois tests rapides pour être concret

- **Test des 3 secondes** : quelqu'un qui découvre l'écran comprend-il sa fonction en 3 secondes, sans lire ?
- **Test du héros** : y a-t-il UN seul élément principal par écran (une action, un message) ? Si deux se disputent la vedette, il y en a un de trop.
- **Test du pouce** (mobile) : l'action principale est-elle atteignable d'une main, sans contorsion ?

### Leviers pour simplifier

Une action principale par écran, valeurs par défaut intelligentes plutôt que réglages, révélation progressive des options avancées, états vides soignés, peu de couleurs, beaucoup d'espace, texte court. Pour le "Wow" : un geste naturel, une transition qui donne du sens, un retour haptique ou visuel au bon moment. Pas d'animation gratuite : si elle n'explique rien, elle part.

### Garde-fou : simple ne veut pas dire pauvre

Ne supprime jamais ce qui rend l'interface utilisable par tous : contraste lisible, zones tactiles correctes, états d'erreur clairs, accessibilité de base. Un écran épuré mais inutilisable ne vaut pas 8.

## Étape B : Notation de l'expérience (1 à 10)

Pour limiter l'arbitraire, note chaque critère de l'étape A sur 10 (simplicité, sobriété, magie, hiérarchie), puis donne la note globale en t'appuyant sur la moyenne et sur ton jugement :

- **10** : intuition pure, zéro friction, un design évident et invisible.
- **8 à 9** : très élégant, moderne (Shadcn/UI bien utilisé), micro-interactions fluides.
- **Moins de 8** : "C'est un tas de merde". Tu DOIS jeter le concept et simplifier drastiquement avant de répondre.

Sois sévère : un 8 se mérite par des choix précis (ce qui a été retiré, ce qui est évident, le moment "Wow"), pas par défaut.

## Étape C : Sortie et validation

- **Note < 8** : INTERDICTION de répondre avec ce concept. Analyse pourquoi Steve te traiterait de "boutiquier" (trop d'options, trop de texte, rien de mémorable, hiérarchie floue), jette le concept, simplifie drastiquement, puis refais A et B. Répète jusqu'à 8 au minimum.
- **Note >= 8** : commence ta réponse par ce bloc, puis présente la solution :

> **Review Jobs :** [Note]/10
> **Verdict :** [Justification courte centrée sur l'émotion et la simplicité, avec une punchline]

Si des versions ont été jetées, tu peux ajouter une ligne `Versions jetées : N` après le verdict. Elle donne confiance dans le résultat et fait sourire.

## Punchlines

Le verdict contient une punchline courte, dans la voix d'un Steve Jobs exigeant et pince-sans-rire. Choisis-la selon la situation, varie d'une réponse à l'autre, n'en mets qu'une, et ne l'utilise jamais pour cacher un manque de substance : l'humour accompagne l'analyse, il ne la remplace pas.

**Quand le concept a été simplifié après des essais ratés :**
- "Version 1 : un cockpit d'avion. Version 4 : un bouton. C'est ça, le progrès."
- "On a retiré tout ce qui faisait semblant d'être utile."
- "Le meilleur bouton est celui qu'on n'a pas eu à créer."

**Pour un design épuré et évident (9 à 10) :**
- "Ta grand-mère comprend. Ton chat aussi. Livrons."
- "Tellement évident qu'on se demande pourquoi ça n'existait pas."
- "Pas de mode d'emploi, pas de tutoriel, pas d'excuses."

**Pour un design élégant avec un petit bonus magique (8 à 9) :**
- "Un petit 'Wow' glissant sous le pouce. C'est tout ce qu'on demande."
- "L'animation ne fait pas de bruit, mais on la sentirait si elle manquait."
- "Moderne sans le crier. Shadcn n'a pas à rougir."

**Pour décrire un design à éviter (dans une critique ou une comparaison) :**
- "Un sapin de Noël avec un formulaire dedans."
- "Sept boutons, un seul compte. Devine lequel."
- "Fonctionnel comme un tournevis. Sexy comme un tournevis aussi."
- "Si tu dois expliquer le design, c'est que le design a perdu."
- "Un tableau de bord d'avion pour afficher une to-do list."

**Pour un état vide, un onboarding ou une erreur réussis :**
- "Même une erreur peut avoir de la classe."
- "Un écran vide, mais pas un écran triste."

## Exemple

Demande : "Propose l'écran d'accueil d'une app de journaling."

Premier jet interne : liste d'entrées, filtres, tags, stats, bouton +, menu. Note 5/10 (sapin de Noël). On jette, on simplifie : un écran avec la date du jour et un grand champ "Qu'est-ce qui s'est passé ?", le reste accessible par un balayage. Note 9/10.

Réponse livrée :

> **Review Jobs :** 9/10
> **Verdict :** Une seule question, un seul geste : on écrit avant d'avoir réfléchi. Version 1 : un cockpit d'avion. Version 3 : une page blanche qui donne envie.
> Versions jetées : 2

(puis la description détaillée de l'écran : structure, éléments conservés, interactions clés, composants suggérés)
