# État de l'art

Dernière révision : **2026-09-05**.
Niveaux de confiance : `[A]` vérifié · `[B]` sourcé, page non ouverte · `[C]` piste non recoupée.
Voir `README.md` pour la règle.

---

## 1. Capture

**`[B]` Le vide laissé par l'arrêt d'Azure Kinect a été comblé par Orbbec.** La Femto Bolt est
présentée comme le successeur direct ; les séries Gemini et Femto sont décrites comme
matures et exploitables en production en 2025-2026. À noter pour le choix de capteurs :
Intel RealSense est décrit comme en maintenance seule, Orbbec comme activement développé.
→ <https://www.orbbec.com/> · <https://www.roboticscenter.ai/blog/best-depth-cameras-robotics>

**`[B]` Le LiDAR des iPhone Pro est devenu une entrée de gamme crédible.** Disponible depuis
l'iPhone 12 Pro, il remplit le rôle de matériel de profondeur qui coûtait auparavant plusieurs
milliers d'euros. Écosystème logiciel : Polycam, Scaniverse, 3D Scanner App, Canvas.
Intégration temps réel dans TouchDesigner via TDLidar — intéressant pour un usage scénique.
→ <https://derivative.ca/community-post/tutorial/tdlidar-%E2%80%94-your-iphone-depth-camera-3d-scanner-and-sensor-rig-touchdesigner>

**`[C]` Captation haut de gamme : rigs de 8 à 42 caméras.** Volucap est cité avec un système
de 42 caméras produisant plus de 3 000 mégapixels par image. Chiffre non recoupé.

---

## 2. Représentation

**`[B]` Le splatting gaussien 3D est en train de devenir le format de fait.** Trajectoire décrite
par les analystes du secteur : 2023 la vitesse, 2024 la précision géométrique et le mobile,
2025 la standardisation, 2026 la maturation des workflows de production. La formule employée est
« un moment JPEG pour l'informatique spatiale » — c'est une formule d'analyste, pas un fait
technique, mais elle situe l'état d'esprit du secteur.
→ <https://web.volinga.ai/2025-turning-point-and-2026-trends-blog/>

**`[B]` Le 4D Gaussian Splatting porte le volumétrique dynamique.** C'est l'extension temporelle
du splatting : le sujet central pour de la vidéo volumétrique, par opposition au scan statique.

**`[C]` Travaux à examiner sur la représentation streamable :**
- *EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation*
  → <https://arxiv.org/pdf/2503.05162>
- *V³: Viewing Volumetric Videos on Mobiles via Streamable 2D Dynamic Gaussians*
  → <https://arxiv.org/pdf/2409.13648>
- *Detail Enhanced Gaussian Splatting for Large-Scale Volumetric Capture*
  → <https://arxiv.org/pdf/2511.21697>

Aucun de ces papiers n'a été lu. Titres et URL issus de résultats de recherche.

---

## 3. Compression & transport

**`[B]` V3C / V-PCC (ISO/IEC 23090-5) serait passé au stade FDIS en octobre 2025**, à la réunion
MPEG 152, en quatrième édition. FDIS = dernière étape avant publication.
→ <https://www.mpeg.org/meetings/mpeg-152/>

**`[B]` Un amendement définirait un profil V-PCC spécialisé pour les splats gaussiens.**
C'est l'information la plus structurante de cet axe : elle signifie que le splatting gaussien
entre dans le cadre normatif MPEG au lieu de rester un format d'écosystème. À vérifier en
priorité.

**`[B]` E-G-PCC (Enhanced G-PCC) en développement**, avec prédiction temporelle améliorée pour
le dynamique (23090-38). La partie 40 (conformance et logiciel de référence) serait passée au
stade CD.

**`[B]` ISO/IEC 23090-10** (portage des données V3C) — 2ᵉ édition passée CD à la 151ᵉ réunion,
FDIS attendu fin 2026.

**`[B]` PackUV** : méthode de compression/streaming du volumétrique 4D qui projette les données
de splatting gaussien en images 2D compatibles avec les codecs vidéo standard. Découpage en
segments pour le suivi d'objets sur longue durée, jusqu'à 30 minutes de séquence.
L'idée directrice — *réutiliser les codecs 2D existants plutôt que d'en inventer un* — est le
schéma récurrent de tout cet axe.
→ <https://techxplore.com/news/2026-05-scientists-path-stream-3d-volumetric.html>

---

## 4. Restitution & projection

**`[B]` Looking Glass a reçu le SID Display of the Year 2026 (avril 2026)** pour sa technologie
Hololuminescent Display (HLD). Principe annoncé : des *light field embeddings* générés
logiciellement sont fusionnés directement dans la pile optique de dalles 2D conventionnelles.
Vision de groupe sans lunettes, sans casque, sans eye tracking. Trois formats annoncés :
16", 27", 86".
→ <https://blog.lookingglassfactory.com/looking-glass-receives-sid-2026-display-of-the-year-award-for-hololuminescenttm-display-technology/>
→ <https://lookingglassfactory.com/displays-overview>

**`[B]` Samsung a annoncé Spatial Signage le 5 juillet 2026** : dalle commerciale 85", optique
« 3D Plate » brevetée, traitement d'image par IA, restitution 3D sans lunettes. Cible : retail
premium, musées, lieux de spectacle. Signal important — l'affichage volumétrique sort du
laboratoire vers la signalétique commerciale.

**`[C]` Familles techniques de l'affichage volumétrique**, à documenter proprement :
- *swept-volume* — surface en mouvement rapide (rotation ou translation) qui compose un volume perçu ;
- *static volume* — matrice de voxels émissifs ;
- *plasma laser femtoseconde* — voxels aériens, sans support matériel, projetables par miroirs
  paraboliques ; travaux historiques « Fairy Lights in Femtoseconds »
  → <https://arxiv.org/pdf/1506.06668> ;
- *piégeage photophorétique* — une particule de cellulose de quelques microns piégée par un
  faisceau 405 nm et déplacée pour tracer l'image
  → <https://arxiv.org/pdf/2512.09401>.

Cette famille est la plus proche de « projection volumétrique » au sens littéral : de la lumière
dans l'air, sans écran. C'est aussi la moins mature.

---

## 5. Audio spatial

**`[B]` MPEG-I Immersive Audio (ISO/IEC 23090-4)** couvre création, stockage, transmission et
rendu de scènes sonores immersives en 6DoF. Le format décrit l'acoustique de la scène : sources
sonores et géométrie acoustiquement pertinente. C'est le pendant sonore direct du volumétrique
visuel — même granularité de problème, même logique de scène 3D.
→ <https://www.ericsson.com/en/blog/2026/3/heterogeneous-sound-sources>

**`[B]` Sources sonores hétérogènes.** Le signal multicanal d'une source hétérogène peut
représenter le champ sonore en HOA (Higher Order Ambisonics), ce qui permet de décrire des
sources *intérieures* — typiquement l'enregistrement multicanal du son à l'intérieur d'une forêt,
là où une source ponctuelle n'a pas de sens.

**`[B]` Captation 6DoF par ambisonie distribuée** : plusieurs microphones ambisoniques répartis
dans la scène, identification et suivi des positions de sources, isolation des signaux par
beamformers, puis interpolation du champ entre les sphères. Zylia commercialise une approche de
ce type (interpolation entre sphères ambisoniques d'ordre 3).
→ <https://www.zylia.co/zylia-6dof.html>

---

## 6. Chaîne de production

**`[B]` Evercoast a racheté Depthkit.** Consolidation majeure du secteur : Depthkit est intégré
à l'écosystème cloud Evercoast, de la captation au rendu. Pour quiconque outille une chaîne
volumétrique, c'est le fait industriel le plus structurant à connaître.
→ <https://www.awn.com/news/evercoast-acquires-depthkit-volumetric-capture-company>
→ <https://www.broadcastnow.co.uk/post-and-vfx/evercoast-acquires-depthkit-to-spur-genai-3d-video-production/5194630.article>

**`[C]` Captation hybride.** Evercoast 2026 mélangerait données de studio (8+ caméras
synchronisées) et profondeur d'un simple scan LiDAR iPhone, la texture haute résolution du
téléphone servant à peindre la géométrie du rig. Si c'est exact, c'est un abaissement net du
ticket d'entrée. À vérifier.

**`[C]` Rendu cloud** : upload des données capteur brutes, traitement sur ferme de serveurs,
plus de station de travail coûteuse requise.

**`[B]` Pipeline de référence académique** : *A Fast Volumetric Capture and Reconstruction
Pipeline for Dynamic Point Clouds and Gaussian Splats*, CVMP 2025 (22ᵉ ACM SIGGRAPH European
Conference on Visual Media Production).
→ <https://dl.acm.org/doi/full/10.1145/3756863.3769713>

---

## Croisements notables

Ce que la lecture par axe fait manquer :

**`[C]` CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays** (SIGGRAPH 2026)
relie directement l'axe 2 et l'axe 4 : rendre du splatting gaussien *sur* un écran à champ
lumineux. C'est exactement le point de jonction capture → projection. À lire en priorité.
→ <https://www.realtimerendering.com/kesen/sig2026.html>

**`[B]` La convergence normative** : si le profil V-PCC pour splats gaussiens (axe 3) se
confirme, alors la représentation dominante (axe 2), le transport (axe 3) et les moteurs de
rendu (axe 4) convergent sur un même objet. C'est la condition d'une vraie chaîne de bout en bout.
