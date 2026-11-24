---
name: sx-note-de-frais-ligne
description: >-
  Ajouter une ligne de frais (train, taxi, hôtel, repas) avec justificatif dans
  la note de frais Everwin SX de l'organisation.
---
# Ajouter une ligne de note de frais dans Everwin SX

## À personnaliser

Ne rien committer ici. Ranger ces valeurs dans la mémoire ou la config locale de l'agent.

| Placeholder | Quoi mettre | Où |
| --- | --- | --- |
| `<VOTRE_EMAIL_PERSO>` | Adresse qui reçoit les factures (hôtel et autres) | mémoire / config de l'agent, jamais dans le dépôt |
| `<VOTRE_COMPTE_SNCF>` | Compte ou e-mail qui reçoit les justificatifs SNCF Connect | mémoire / config de l'agent, jamais dans le dépôt |
| `<DOSSIER_DE_TRAVAIL>` | Dossier local où enregistrer les PDF de justificatifs | mémoire / config de l'agent, jamais dans le dépôt |
| `<URL_CONNEXION_SX>` | URL de connexion de l'instance Everwin SX | mémoire / config de l'agent, jamais dans le dépôt |
| `<ORGANISATION>` | Organisation dont on saisit la note de frais | mémoire / config de l'agent, jamais dans le dépôt |
| `<AFFAIRE_PAR_DEFAUT>` | Affaire proposée par défaut (code et libellé) | mémoire / config de l'agent, jamais dans le dépôt |

## Déroulé

Saisie pour `<ORGANISATION>`.

Inputs: date, affaire (default: `<AFFAIRE_PAR_DEFAUT>`), type, objet, montant TTC, receipt PDF.

Find receipts first: mail connectors (invoices in `<VOTRE_EMAIL_PERSO>`). Train trips are often not in that mailbox: SNCF Connect https://www.sncf-connect.com/trips > trip > "Obtenir le justificatif par e-mail" (goes to `<VOTRE_COMPTE_SNCF>`) then ask the person to forward it to the bot inbox. Save PDFs to `<DOSSIER_DE_TRAVAIL>`.

1. Open `<URL_CONNEXION_SX>` in a NEW tab. If a login page shows, only the user types the password: hand over the screen.
2. Left sidebar: Ressources Humaines > "Notes de frais" (current month's note opens).
3. In "Frais", click "+": "Edition" modal. Fill Date, Affaire, Type, Objet, Montant unitaire (Quantité 1). Click "Ajouter" (or "Ajouter et Nouveau").
4. Types: Autres Frais (use for hôtel, no hotel type), Frais de déplacement (Taxi, Billet de train), Frais de mission, parking, péage, kilométriques, carburant, Repas midi/soir (+ invitation / à l'étranger).
5. Receipt: open the line's full form (pen icon / double-click), click "Justificatif" next to "Mettre à jour" at the bottom; the OS dialog may not open, so set the file on the page's hidden file input. Then "Mettre à jour". Paperclip turns grey (red = Document manquant).

Rules: SX is laggy, mouse clicks on screen; never click "Validation Collaborateur" (the person validates); confirm uncertain values first.
