---
name: montage-vlog
description: >-
  À utiliser pour monter un vlog de voyage à partir de rushs bruts (DJI,
  iPhone, GoPro), d'une journée test jusqu'au film complet.
---
# Montage vlog

Objectif : transformer des rushs de voyage en un vlog fini, dans la grammaire des vidéos
déjà publiées par l'auteur : face caméra très présente, plans de coupe
qui illustrent ce qui est dit, chapitres courts nommés par lieu, deux rythmes alternés
(longues prises parlées / rafales de montage en musique), une musique par séquence.
La skill ne contient **aucune donnée de destination** : tout ce qui dépend du voyage vit dans
`voyages/<destination>/voyage.json` (§2), en local. Le dépôt ne garde que l'exemple fictif
`voyages/exemple/`.

## À personnaliser

Ces valeurs restent dans la mémoire ou la config locale de l'agent. On ne les committe pas
(voir `.gitignore` : `retours.local.md`, `voyages/*` hors `voyages/exemple/`).

| Placeholder | Quoi mettre | Où |
| --- | --- | --- |
| `<CHARTE_GRAPHIQUE>` | Couleurs et règles de marque de l'auteur. Neutre tant qu'elles ne sont pas validées. | mémoire / config locale |
| `<PROJET_RUSH>` | Projet (Frame.io ou équivalent) qui contient les rushs, un dossier par destination | mémoire / config locale |
| `<DOSSIER_RETOURS>` | Dossier de relecture où déposer le montage et lire les commentaires minutés | mémoire / config locale |
| `<MACHINE_RUSH>` | Dossier des rushs sur la machine de l'auteur | mémoire / config locale |
| `<DESTINATION>` | Nom du dossier du voyage en cours | fichier local `voyage.json`, non versionné |
| `<LANGUE_PAROLE>` | Langue parlée dans les rushs, pour la transcription | mémoire / config locale |
| `<DOSSIER_OUTILS_MIX>` | Dossier des scripts de mix (crossfade, pedalboard, venv) | mémoire / config locale |
| `<DOSSIER_DRIVE>` | Dossier de livraison de la vidéo | mémoire / config locale |
| (sans placeholder) | Nom de l'auteur, nom de chaîne, monteur habituel : le texte dit « l'auteur » | mémoire de l'agent, jamais dans le dépôt |

## 0. Règles non négociables (validées avec l'auteur, ne pas rediscuter)

- **Aucun sous-titre de dialogue dans un vlog.** L'habillage, oui : titres de chapitres
  design, textes mis en avant, design sonore. Les sous-titres de paroles, jamais.
- **Ne jamais appliquer `<CHARTE_GRAPHIQUE>` tant que l'auteur ne l'a pas validée.** Habillage neutre par défaut (texte blanc, ombre/outline
  sombre), conservé dans un fichier de design séparé et paramétrable : toute retouche
  (couleur, titres, minutages) se fait en régénérant ce fichier, sans retoucher au montage.
- **Le livrable par défaut est la vidéo seule**, pas un pack autour.
- **Annoncer une temporalité estimée dès qu'un travail part en arrière-plan**, et
  prévenir si elle glisse.
- Quand l'utilisateur parle, **on doit le voir quand même, mais le paysage doit se
  voir** : superposition = paysage plein écran + visage en incrustation bordée
  (haut-droite), jamais l'inverse qui écrase le lieu, jamais de plan parlé sans
  illustration quand un plan du lieu existe.
- **Laisser respirer les plans, pas de plafond de durée** (un vlog : on regarde le paysage et on écoute les voix) : une journée dure le temps que le contenu justifie (repère 8–12 min, jamais
  compressée pour tenir une cible) ; paysages de 4–10 s et moments où le paysage
  respire seul en musique ; échanges parlés intéressants gardés en entier ; seules les
  longueurs vides sont coupées.
- **Ne jamais couper l'auteur en pleine phrase.** Chaque segment parlé sort après la fin de la phrase (ponctuation
  finale + dernier mot de `word_timestamps`) + **0,5 s de marge** (repère 0,4–0,8 s :
  réaction, rire, souffle) puis un fondu audio. La parole prime sur les cibles de
  rythme : si une phrase est trop longue, on la garde entière et on raccourcit un
  plan d'illustration voisin, ou on fait un jump cut **entre** deux phrases, jamais
  dedans. **Piège du QC** : une ponctuation de Whisper suivie d'une pause < 0,5 s
  n'est pas une fin de phrase si la suite du même rush n'est pas reprise dans l'EDL
  (souvent une même pensée, mal découpée par la transcription). Le détecteur doit
  signaler ces coupes nettes, pas les classer « OK_COURTE ».
- **Pas d'accroche par journée** : les journées sont assemblées en un seul
  film long, donc une journée commence directement par la carte « JOUR N » puis le récit.
  Une seule accroche, en tête du film complet.

- **À conserver tel quel (validé à l'écoute par l'auteur : musique, sons, voix, LUT)** : choix et
  transitions musicales (§8–9), chaîne son/voix et design sonore (§10), LUT et
  étalonnage (§5). Ne modifier ces réglages que sur demande explicite.


- **Cohérence de la parole.** Une séquence parlée vient d'UN SEUL moment continu : ne jamais coller deux prises de parole tournées à des moments différents comme si c'était la même phrase. Pour changer de moment, intercaler un plan de paysage ou une transition. Enlever les « euh » et hésitations marquées (coupes propres, fondus audio de 20 à 40 ms). Les images suivent l'ordre de la parole (rien ne montre un événement avant la phrase qui l'annonce). Supprimer les promesses d'information non tenues (par exemple « je vous dirai le tarif »), sauf si l'info vérifiée est ajoutée. Illustrer chaque sujet par le plan qui le montre.
- **Voix toujours nettement au-dessus de la musique.** Un écart voix–musique p10 ≥ 10 dB sur chaque passage parlé (médiane ≥ 15 dB, §10). Baisser le lit et ducker plus fort partout, pas seulement au commentaire. Une voix inaudible est remontée, légèrement débruitée ou déventée si c'est le vent/la cascade, et la musique est baissée ; vérifier tous les autres passages faibles. La chaîne voix validée (RNNoise, EQ, compresseur) reste le défaut ; seul l'équilibre et un traitement léger des plans ventés changent, sur demande ou constat d'inaudibilité.
- **Numérotation des chapitres continue sur tout le film** : les journées s'assemblent en un seul film, donc le jour N reprend la numérotation après le dernier chapitre du jour N-1 (jamais « Chapitre 1 » à chaque jour). Lire le nombre de chapitres des jours précédents avant de titrer. Appliquer le numéro continu aux cartes à l'écran, aux titres, aux chapitres YouTube et aux métadonnées / crédits. Exemple de suite : jour 1 = chapitres 1–8, le jour 2 reprend à 9.

- **Retours minutés.** Chaque montage pleine qualité est envoyé dans `<DOSSIER_RETOURS>` et son lien est donné à l'auteur, qui commente à la seconde près. Lire tous les commentaires, faire correspondre chaque timecode (hh:mm:ss:images) à l'EDL de la version commentée, corriger, généraliser au reste de la vidéo et livrer la vN+1 au même endroit.

## 1. Ingestion des rushs

- **Un jour à la fois** (espace disque de la machine de montage : vérifier `df -h` avant chaque jour,
  garder ≥ 15 Go libres) : télécharger, faire les proxys, puis supprimer les originaux
  du jour une fois les proxys et WAV vérifiés.
- **Voies de transfert, par ordre de préférence** :
  1. **Frame.io (ou l'outil indiqué par `<PROJET_RUSH>`) dans le navigateur de la machine de montage**, un dossier par
     destination : téléchargement **fichier par fichier** = OK (original 4K complet et
     lisible, vérifié). **« Download All » cale** sur Frame.io : ne pas l'utiliser. Vérifier taille
     et `ffprobe` de chaque fichier arrivé.
  2. **La machine de l'auteur** (ex. `<MACHINE_RUSH>/<DESTINATION>`) : fiable, mais elle
     doit rester allumée et connectée.
  3. **Connecteur Drive** : s'il refuse les fichiers > 100 Mo, ne l'utiliser que pour les petits
     fichiers (iPhone courts, musiques, images).
- Inventaire d'abord : fichiers, durées, tailles, résolutions, fps, appareil (ffprobe),
  par journée/dossier.
- **Métadonnées date/heure/GPS** (`ffprobe -show_entries format_tags`, `exiftool -n
  -GPSLatitude -GPSLongitude -CreateDate`) :
  - **ordonner la journée** sur l'heure de prise (corriger le fuseau : les DJI/GoPro
    écrivent souvent en UTC ou à l'heure de l'appareil ; recaler sur un iPhone de la même
    scène) ;
  - **situer les lieux** : regrouper les plans par position (rayon ~300 m) et par trou
    temporel (> 20 min = nouveau segment), puis géocodage inverse (Nominatim/OSM, 1
    requête/s) pour nommer le lieu ;
  - **nommer les chapitres et étiquettes de lieu** à partir de ces noms, croisés avec ce
    qui est dit (transcription) ; orthographe vérifiée sur une source web.
  - Sans GPS (GoPro sans GPS, iPhone sans localisation) : ordre par heure, lieu déduit du
    plan voisin ou de la parole ; le noter comme « déduit » dans `voyage.json`.
- Proxys locaux 1080p pour tout le travail : `ffmpeg -vf scale=1920:1080 -c:v libx264
  -preset veryfast -crf 26` (les originaux 4K H.265 sont trop lents à traiter en
  série ; vérifier le chemin complet sur UN fichier, transcodage compris, avant de
  promettre un délai sur un lot).
- Extraire un WAV par plan. Transcrire avec faster-whisper (modèle medium, langue `<LANGUE_PAROLE>`, VAD). Piège connu : conflit de version PyAV/faster-whisper
  (`av.open() got an unexpected keyword argument 'metadata_errors'`) ; contournement :
  décoder le WAV en numpy via le module `wave` de la stdlib et passer le tableau
  à `model.transcribe`.
- Extraire 3 images par plan (10 %, 50 %, 90 %) et une planche contact : c'est la
  base de la classification visuelle.

## 2. Paramètres du voyage (`voyages/<destination>/voyage.json`)

Créé au début de chaque projet, lu par le montage, `design.ass` et le mix. Rien de
spécifique à une destination ailleurs.

```json
{
  "destination": "…", "pays": "…", "dates": ["AAAA-MM-JJ", "…"],
  "jours": [{"n": 1, "date": "…", "source": "<PROJET_RUSH>/<dossier>/<jour>", "duree_cible_s": null}],
  "lieux": [{"nom": "…", "lat": 0, "lon": 0, "source": "gps|déduit", "verifie": true}],
  "ambiance_musicale": {"mots_cles": ["…"], "par_role": {"accroche": "…", "decouverte": "…", "emotion": "…", "fete": "…", "nuit": "…"}},
  "morceaux": [{"titre": "…", "artiste": "…", "licence": "CC BY 4.0", "lien": "…", "credit": "…", "valide_par_auteur": false, "utilisations": 0}],
  "etalonnage": {"teinte_ombres": "teal", "teinte_lumieres": "chaud", "saturation": 1.28},
  "duree_film_cible_s": 3600
}
```

Exemple de format, fictif : `voyages/exemple/`.

## 3. Analyse et structure

- Croiser : (a) le contenu parlé par plan (qui parle, de quoi, phrases réutilisables,
  gags), (b) la classification visuelle des plans muets (lieux, ambiances, péripéties),
  (c) l'heure et le lieu (§1).
- **Audit parole au mot près** avant de fixer les coupes : retranscrire les plans
  parlés avec `word_timestamps=True` et vérifier chaque point d'entrée/sortie.
  Deux fautes à éviter, vécues : couper un mot, et couper une phrase avant sa fin
  (la fin peut arriver 25 s plus tard dans le même plan, après un silence : soit
  on prend la phrase entière, soit on la referme en jump cut interne).
- **Structure d'une journée (durée libre, règle 0)**, destinée à être assemblée dans le film :
  1. **Pas d'accroche** (règle 0). Ouverture : carte **« JOUR N »** (3–4 s) sur un plan
     large du premier lieu, en musique, puis récit immédiat (≤ 0:08).
  2. (Seulement pour une vidéo publiée seule, sur demande explicite : accroche 15–30 s,
     une phrase forte COMPLÈTE + 6 à 12 flashs de 1–2 s, titre entre 0:15 et 0:26.)
  3. **Chapitres chronologiques**, nommés par **lieu ou moment** (« Arrivée à … »,
     « Perdus à la gare »). Durée libre selon le matériau, typiquement de l'ordre
     de 45 s à 3–4 min : sur un film de référence déjà validé, sans plafond de
     durée, les chapitres narratifs durent **46–207 s**
     (un plan de fin peut être bien plus court). L'ancienne cible 45–90 s
     (médiane ~60 s) était trop serrée ; ne pas compresser un chapitre pour
     tenir 90 s. Rôles génériques : trajet/arrivée, lieu/visite, repas,
     activité, péripétie, debrief face caméra, soirée/nuit.
  4. **Fin** : phrase de clôture du créateur + 10–20 s de plans en musique.
- **Film complet** : **trailer d'accroche** monté à la toute fin, quand toutes les journées sont faites (sur demande de l'auteur) : 30–60 s, meilleures phrases complètes et plus beaux plans de tout le voyage, en ouverture du film ; petite **carte animée du trajet** du jour (points GPS du §1, fond de carte OSM, 3–5 s) avec la carte **« JOUR N »** ; **fondu musical** de 4–8 s d'une journée à l'autre, pour que le film s'enchaîne sans rupture (validé par l'auteur) ; carte « JOUR N » (dernier :
  « DERNIER JOUR ») en tête de chaque journée ; debrief face caméra quand il existe.
  Densité observée sur les jours 1–4 validés : 5–8 chapitres pour 10–12 min, pas
  ~1 chapitre/min. Chapitres + temps dans `chapters.txt` (fichier de
  travail, généré depuis l'EDL, non livré sauf demande).
- Constituer la liste de montage (EDL) : pour chaque segment, fichier, in, out,
  durée, rôle, chapitre, lieu. La durée totale est un contrat : toute modification d'un
  segment est compensée sur un plan d'illustration voisin pour ne pas décaler la suite.

## 4. Rythme et transitions (cibles mesurées sur des vlogs de référence)

- **Prises parlées** : 4–8 coupes/min ; une prise face caméra peut tenir **40–70 s** si
  la parole porte ; au-delà de 20 s sur un même cadre, insérer un plan de coupe ou un
  jump cut.
- **Rafales de montage** (sans parole, en musique) : 20–35 coupes/min, plans **1–2 s**,
  calés sur le tempo ; 5–30 s.
- **Moyenne d'une journée** : 9–13 coupes/min ; plan médian 2–3 s ; **médiane pondérée
  par la durée 8–18 s** ; répartition du temps : 15–20 % en plans < 3 s, 25–40 % entre 3
  et 10 s, 40–55 % au-delà de 10 s.
- **Transitions** : coupe franche par défaut (~95 %). Aux **changements de chapitre /
  sauts de temps** : flou de mouvement ou de zoom de 8–12 images (0,3–0,5 s), whoosh
  léger possible, au plus un par frontière. Utiliser les volets naturels (passant,
  mur). Fondu court 0,5 s seulement pour l'émotion ou la fin de journée. Jamais de
  longs fondus en série. Jump cuts internes pour les hésitations, en respectant la fin
  de phrase.

## 5. Montage image

- Segments normalisés 1920×1080, 30 fps, yuv420p. Plans verticaux (iPhone portrait) :
  fond flouté plein écran + plan net centré.
- **Étalonnage par LUT générée** (les rushs DJI sont plats) : courbe en S
  `v = x + 0.20 * sin((x - 0.5) * pi)` (ombres approfondies, hautes lumières
  relevées ; VÉRIFIER LE SIGNE numériquement : 0,25 doit descendre vers 0,11 et
  0,75 monter vers 0,89, sinon la courbe est inversée et aplatit l'image),
  saturation ×1,28, split tone léger (par défaut ombres teal, lumières chaudes ;
  réglable dans `voyage.json` selon la lumière du pays). Écrire un fichier `.cube` 33
  points, l'appliquer via `lut3d`, et contrôler le résultat sur des images avant le
  rendu complet. Même LUT pour toutes les journées d'un voyage.

## 6. Face caméra et plans de coupe

- **Règle de l'auteur (§0, validée sur un test)** : quand un plan du lieu existe pendant
  que l'auteur parle, paysage plein écran + visage en incrustation (≈ 700 px de large, cadre
  blanc fin, haut-droite), jamais l'inverse qui écrase le lieu.
- **Repères de ses vidéos publiées** : face caméra 43–62 % du temps total, en alternance
  J-cut/L-cut avec les plans du lieu (la voix continue 2–5 s sur l'image). Le face caméra
  plein écran sert quand aucun plan du lieu n'existe (voiture, tente, réaction à chaud)
  ou pour un moment d'émotion court ; dès qu'un plan du lieu existe, repasser en
  incrustation ou en plan de coupe.
- À faire trancher par l'auteur : passer ou non au plein écran illustré par défaut, comme
  dans les anciens vlogs. Ne pas changer la règle §0 sans accord.
- **Encart photo/vidéo** quand il dit « je vous mets la photo » : image dans un cadre
  blanc fin, ~35 % de la largeur, 3–5 s (+ déclencheur, §7).

## 7. Habillage (design) et textes à l'écran

- Fichier ASS séparé (`design.ass`), généré par script depuis l'EDL, les chapitres et
  `voyage.json`. Style neutre : blanc, outline/ombre sombre, fond semi-transparent
  derrière les titres. Aucune couleur de marque.
- Éléments :
  - **Titre d'ouverture** et **cartes « JOUR N »** : grand texte centré, 1,5–3 s, sur
    plan d'illustration.
  - **Cartes chapitres** (barre + « CHAPITRE n » + titre du lieu) ou, plus léger,
    **étiquette de lieu** : bas-gauche, petite icône + nom en petites capitales, dans les
    **4 premières secondes** d'un chapitre qui découvre un lieu nommé, **3–4 s**,
    entrée/sortie 0,2 s. **Cible : ≥ 1 chapitre sur 2.**
  - **Textes mis en avant** sur les phrases fortes (un prix, une distance, une
    exclamation, la phrase de clôture).
  - **Commentaires du monteur** (ironie, précision : « *Ou pas… ») : **au plus 1 toutes
    les 2–3 min**, 2–3 s. Test : s'il répète ce qu'on entend, c'est un sous-titre →
    interdit.
  - **Cartes d'info** (date, chiffre, fait) : seulement vérifiées, source notée dans les
    fichiers de travail.
- **Interdits par défaut** (`<CHARTE_GRAPHIQUE>`, règle 0) : pastille
  « S'ABONNER », bandeau réseaux sociaux, carte « SUBSCRIBE ». Activables seulement après
  validation de l'auteur, via les paramètres de `design.ass`.
- Orthographe de chaque nom de lieu vérifiée (source web).
- Effets sonores (banque Earshot) : sting sur le titre, whoosh aux chapitres et sur les
  flous de transition, riser avant le moment fort, pop sur les textes mis en avant, et
  le gag récurrent : **déclencheur d'appareil photo** (`shutter/dslr`) à la seconde où
  le créateur dit « je vous mets la photo ».

## 8. Musique : choix selon la destination

1. **Fiche d'ambiance** dans `voyage.json` : 3–5 mots-clés culturels/sonores de la
   destination (ex. « oud, percussions », « synthés urbains », « cordes nordiques,
   ambient ») et, par chapitre, rôle + énergie (calme / moyenne / festive).
2. **Uniquement de la musique libre de droits à licence vérifiée** sur la page de
   l'artiste ou de la banque (CC BY ou équivalent ; banque payante seulement si l'auteur
   fournit l'accès). Pour chaque morceau : titre, artiste, licence, lien, **crédit à
   mettre en description** à la publication.
3. **Proposer avant d'appliquer** sur une nouvelle destination : 2–3 extraits de 20 s
   par ambiance ; attendre la validation de l'auteur avant le mix.
4. **Une musique par chapitre/séquence**, changement au chapitre suivant (§9). Deux
   chapitres adjacents **peuvent** partager le même morceau quand ils forment une
   seule séquence (exemple : deux paires de chapitres adjacents partagent un
   morceau, soit 4 pistes pour 6 chapitres). **Aucun morceau utilisé plus de 2 fois dans un
   film** (compteur `utilisations`), pas deux fois dans la même journée.
5. **Niveaux** : sous la parole, musique ducée (voir §10) ; en accroche et rafales de
   montage, musique pleine sans ducking. Part de musique seule observée sur les
   jours 1–4 validés : **22–32 %** (QC : J1 25,6 %, J2 21,6 %, J3 22,9 %,
   J4 32,1 %). C'est la plage à viser, plutôt que l'ancienne cible 10–20 %.
   Garder des respirations sans musique quand l'ambiance du lieu raconte
   (foule, vagues, vent, musiciens).

## 9. Transitions musicales (lit musical)

- **Assembler le lit musical en WAV séparé** (48 kHz stéréo, 24 bit), avant le mix avec
  la voix ; jamais dans le graphe vidéo.
- **Égaliser les volumes à la médiane** : mesurer chaque morceau (LUFS intégré), ramener
  chacun à la médiane des morceaux du lit par un simple gain.
- **Fondu croisé equal-power** `acrossfade` courbes `hsin`, **2 à 6 s** (2 s par défaut
  aux frontières de chapitre, jusqu'à 6 s entre deux ambiances calmes) :
  `<DOSSIER_OUTILS_MIX>/crossfade_two.sh a.wav b.wav <durée_s> sortie.wav`.
- **Tempo** : pas d'étirement de tempo sur l'orchestral/ambient. Étirement **≤ 8 %**
  seulement si les deux morceaux ont un vrai rythme marqué ; **refus au-delà de 15 %**
  (changer de morceau ou de point de raccord).
- **Pedalboard (optionnel)**, sur chaque morceau avant le volume et le ducking :
  `<DOSSIER_OUTILS_MIX>/venv/bin/python <DOSSIER_OUTILS_MIX>/pedalboard_music.py in.wav out.wav`
  (EQ doux, compresseur, **BrickwallLimiter**). **Jamais `pedalboard.Limiter`** (gain
  de compensation auto + écrêtage à 0 dBFS).
- **Pas de loudnorm sur le lit seul** : le loudnorm final du mix complet reste la
  référence.
- pyCrossfade : testé, **non retenu**.

## 10. Son : la chaîne validée (le point critique)

Le premier mix (dénoise FFT fort, `afftdn` nr=13) a été jugé « dégueulasse » :
voix étouffée, effet sous l'eau, présence mesurée à −29,9 dB. Ne plus jamais
traiter la voix comme ça. La chaîne retenue, validée par tests A/B/C/D écoutés
par l'auteur sur son téléphone :

1. **Modèle neuronal RNNoise** via le filtre ffmpeg `arnndn` : modèle `sh.rnnn`
   (dépôt GregorR/rnnoise-models, dossier somnolent-hogwash-2018-09-01),
   `arnndn=m=sh.rnnn:mix=0.85` pour garder le corps de la voix.
2. Puis : `highpass=f=80`, EQ de présence `+5 dB à 2,8 kHz`, `+3 dB à 5,2 kHz`
   (largeur 1,2 octave), compresseur doux (seuil 0,12, ratio 2,5), **voix +5 dB**.
3. Musiques (lit du §9) : volume 0,48 (abaissé après un retour d'écoute, ex-0,62) ;
   ducking sidechain `threshold=0.008, ratio=12, attack=15, release=500`, clé = la
   voix traitée (seuil bas pour ducker aussi les paroles faibles). Contrôle :
   écart voix/musique pendant la parole **médiane ≥ 15 dB et p10 ≥ 10 dB** (sinon
   baisser encore le volume de base du lit ou renforcer le ducking).
4. Effets sonores aux minutages de l'EDL (délais en ms, volumes 0,30 à 0,80).
5. Normalisation finale : `loudnorm=I=-14:TP=-1.5:LRA=11` (ou `TP=-2.0` si un
   essai à −1,5 dépasse encore), puis limiteur **true-peak** avant l'encodage AAC,
   puis `aresample=48000`. Ne pas se fier au seul `TP=-1.0` de loudnorm : des
   masters AAC de journées déjà livrées sont déjà sortis à −0,2 et −0,3 dBTP, et
   leurs versions légères à +0,8 dBTP. Cible de livraison : true peak **≤ −1,0 dBTP**
   sur **chaque** fichier livré (master, version légère, version Drive), mesuré
   **après** l'encodage (`ebur128=peak=true`). Présence autour de −21 dB, clarté
   (brightness) > 1 100 Hz (Earshot).
6. **Homogénéité** : niveau médian court terme de chaque chapitre à **±3 LU** de la
   médiane de la journée ; aucun chapitre parlé > 10 % du temps sous −35 LUFS
   momentané (sauf silence voulu). Mêmes réglages pour toutes les journées, stockés dans
   `mix.json` versionné.

Itération : produire des **extraits de test de 60 s** et faire valider à l'écoute avant
le mix complet. Un mix validé se réassemble à l'image existante par simple mux, sans
nouveau rendu vidéo.

## 11. Assemblage et pièges d'encodage (tous vécus, tous coûteux)

- **Mixer l'audio en WAV séparé, puis assembler** (mux `-c:v copy`). Mélanger
  audio dans le même graphe que la vidéo a produit une piste audio aux
  timestamps étirés (325 s pour 175 s d'image) : toujours vérifier la durée
  de CHAQUE flux après encodage (`ffprobe -show_entries stream=duration`).
- **Jamais deux ffmpeg sur le même fichier de sortie** en parallèle : fichier
  corrompu garanti.
- **Vérifier la durée de chaque segment** après son encodage : un segment
  tronqué (reste d'un encodage tué) raccourcit silencieusement tout
  l'assemblage (3 min 40 devenues 1 min 31). Lister les durées attendues et
  obtenues, supprimer et régénérer tout segment fautif.
- Rendu final en **deux passes détachées** (`setsid`, fichier de statut avec
  code de sortie) : passe image (LUT + habillage + fondu), puis mux avec le
  mix WAV. Le rendu monolithique est mort une fois en plein milieu, sans
  erreur, probablement sur un pic mémoire.
- Ne jamais tuer un processus par motif (`pkill -f`) quand la commande
  elle-même contient le motif : on se tue soi-même. Tuer par PID vérifié.
- La machine de montage est partagée : lancer les gros calculs en `nice`, un lourd à la fois.

## 12. Contrôle qualité avant livraison (obligatoire, mesuré)

- Durées vidéo et audio du fichier final (≈ égales, à la durée cible).
- Décodage complet sans erreur (`ffmpeg -i fichier -f null -`).
- Images témoins : titre, chaque début de chapitre, chaque texte mis en avant, une
  prise parlée avec plan de coupe (et une incrustation si utilisée). Vérifier :
  habillage neutre (aucune DA), aucun sous-titre de dialogue, étalonnage contrasté.
- Mesure Earshot / ffmpeg : LUFS ≈ −14, true peak **≤ −1,0 dBTP** sur le
  fichier mesuré, présence et clarté cohérentes avec le §10 ; homogénéité par
  chapitre (±3 LU). Ce contrôle true peak est **obligatoire après chaque
  encodage** (master AAC, version légère, version Drive), pas seulement sur le
  mix WAV.
- Écoute des jointures de phrases sur les plans parlés (audit §3).
- **Métriques de style**, notées dans `qc.json` :
  - coupes/min, plan médian, médiane pondérée, répartition des durées (PySceneDetect
    ContentDetector seuil 27) → cibles §4 ;
  - part du temps avec visage ≥ 12 % de la largeur (YuNet, 1 image/s) → cible §6 ;
  - étiquettes de lieu / chapitres (≥ 1/2), nombre de commentaires, aucun texte =
    transcription ;
  - part de musique seule (repère observé 22–32 %), écart voix/musique pendant
    la parole (p10 ≥ 10 dB, médiane ≥ 15 dB, §10) ;
  - ouverture : carte JOUR N présente, pas d'accroche, début du récit ≤ 0:08 ;
  - **fins de phrases** : pour chaque segment parlé, le point de sortie est ≥ 0,5 s après
    le dernier mot d'une phrase terminée (ponctuation finale) ; signaler aussi une
    **suite du même rush non reprise** si le mot suivant commence moins de 0,5 s après
    et n'est pas pris par le segment parlé suivant (sauf nouvelle phrase typée « oh / bon / allez ») ;
    lister dans `qc.json` tout segment qui ne respecte pas la règle, à corriger avant
    livraison (cible : 0) ;
  - utilisations par morceau (≤ 2 par film).

## 13. Livraison

- **Vidéo seule** (règle 0). Pièce jointe **< 200 Mo** et/ou **lien Drive** (UploadFile
  vers `<DOSSIER_DRIVE>`). Si l'original dépasse, exporter une version compressée pour
  l'envoi (x264 CRF 23–26, 1080p) et garder l'original sur la machine de montage ; le dire en une
  phrase.
- Annoncer : durée, chapitres en une ligne, ce qui reste à valider à l'écoute.

## 14. Boucle d'amélioration continue (après chaque journée livrée)

1. **Recueillir le retour** : avec la vidéo, livrer 2 extraits d'écoute de 60 s (un
   parlé, un en musique) et demander en 3 questions max : ce qu'il **aime** (à garder),
   ce qu'il **critique** (rythme, son/musique, habillage/textes, structure, étalonnage),
   un moment à couper ou à rallonger.
2. **Consigner** dans `retours.local.md` (à côté de cette skill, non versionné) : date, journée, citation
   exacte, positif/négatif, catégorie, action décidée, paramètre modifié (avant → après).
   `retours.md` dans le dépôt n'est qu'un exemple de format.
3. **Mettre à jour la skill avant la journée suivante** : un retour → réglage dans
   `design.ass` / `mix.json` / `voyage.json` / cibles §4, et la règle correspondante
   ici. Une correction explicite (« jamais… », « toujours… ») ou un retour répété 2 fois
   devient une règle ; une correction forte va en section 0. Ce que l'auteur aime est
   noté aussi, comme règle « à conserver ». Ne pas committer de citation, de date de
   voyage ni de nom : la règle versionnée reste générique, le journal reste local.
4. **Appliquer** à la journée suivante par paramètres, jamais par retouche manuelle ;
   ne refaire une journée livrée que sur demande.
5. **Mesurer** : comparer `qc.json` avant/après chaque changement.
6. **À l'assemblage du film**, réappliquer les réglages finaux à toutes les journées
   (même mix, même habillage, même LUT) pour la cohérence.

## 15. Estimations (repères)

- Test 6,6 Go (une demi-journée) : ≈ 1 h 30 du téléchargement à la vidéo finie, rendu
  compris. Le transfert et l'analyse dominent ; extrapoler au volume réel du jour et
  annoncer l'estimation dès le lancement (règle 0).
- Avant de promettre un délai sur un lot : chronométrer le chemin complet sur UN fichier.

## 16. Outils

ffmpeg/ffprobe ; exiftool ; faster-whisper ; PySceneDetect ; OpenCV YuNet ; Demucs
(contrôle) ; Earshot (banque d'effets `sfx render`, mesures `measure`) ; RNNoise
(`arnndn` + `sh.rnnn`) ; Pedalboard (`<DOSSIER_OUTILS_MIX>/venv`) ; helpers
`<DOSSIER_OUTILS_MIX>/crossfade_two.sh`, `<DOSSIER_OUTILS_MIX>/pedalboard_music.py` ;
skills associées : editor, edl-edit, cutting-rhythm, audio-edit, color-grade,
assembly-and-delivery, video-qa, reframe-social (déclinaisons verticales).
