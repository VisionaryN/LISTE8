# Pistes

Hypothèses, expériences à mener, questions ouvertes.
Statuts : `ouverte` · `en cours` · `close`.

**Une piste close reste dans ce fichier.** Savoir qu'une voie a été explorée et abandonnée,
et pourquoi, vaut mieux que de la redécouvrir dans six mois.

---

## P-001 — Promouvoir les entrées `[B]` en `[A]` · `ouverte` · 2026-09-05

L'amorçage de la base a été fait sans accès direct aux pages web : recherche possible, ouverture
des URL bloquée. Toutes les entrées sont en `[B]` ou `[C]`.

**À faire** : depuis un terminal avec accès web, ouvrir les URL de `etat-de-lart.md` axe par axe,
confirmer ou corriger, passer en `[A]`. Prioriser l'axe 3 (compression) : c'est celui où une
affirmation fausse coûte le plus cher en décisions d'architecture.

---

## P-002 — Le profil V-PCC pour splats gaussiens existe-t-il vraiment ? · `ouverte` · 2026-09-05

Axe 3. Un amendement définirait un profil V-PCC spécialisé pour les splats gaussiens `[B]`.

**Pourquoi c'est décisif** : si c'est confirmé, la représentation dominante entre dans le cadre
normatif MPEG, et une chaîne capture → transport → restitution standardisée devient possible.
Si c'est faux, le splatting reste un format d'écosystème et le choix de pipeline se pose
autrement.

**À faire** : compte rendu officiel de la réunion MPEG 152, numéro exact de l'amendement, stade.

---

## P-003 — CoherentRaster : splatting gaussien sur écran à champ lumineux · `ouverte` · 2026-09-05

Croisement axes 2 et 4. Papier SIGGRAPH 2026 `[C]` : *CoherentRaster: Efficient 3D Gaussian
Splatting for Light Field Displays*.

C'est littéralement le raccord entre ce qu'on capture et ce sur quoi on le projette.

**À faire** : trouver le papier, lire la méthode, évaluer le coût de rendu réel et la
compatibilité avec le matériel Looking Glass.

---

## P-004 — Quel capteur pour un premier banc de captation ? · `ouverte` · 2026-09-05

Axe 1. Question pratique, pas théorique. Les éléments connus `[B]` : Orbbec Femto Bolt en
successeur d'Azure Kinect, Gemini 335 au meilleur rapport prix/performance, RealSense en
maintenance seule, LiDAR iPhone en entrée de gamme crédible.

**Question ouverte** : combien de capteurs pour quelle qualité utile ? Le saut 4 → 8 → 16 caméras
n'est pas linéaire en résultat, et personne ne publie la courbe.

**À faire** : chiffrer un banc à 4 et à 8 capteurs, matériel et synchronisation comprises.

---

## P-005 — La projection volumétrique littérale est-elle exploitable ? · `ouverte` · 2026-09-05

Axe 4. Plasma laser femtoseconde et piégeage photophorétique `[C]` produisent de la lumière
*dans l'air*, sans support. C'est le seul « projection volumétrique » au sens propre — tout le
reste est un écran.

**Hypothèse à tester** : cette famille reste hors d'atteinte pour un usage scénique
(résolution, volume, sécurité, coût), et l'usage réel passera par les écrans à champ lumineux.

**À faire** : chercher une installation publique réelle, pas une démonstration de laboratoire.
Si aucune n'existe en 2026, clore la piste et le noter — ça évite d'y revenir.

---

## P-006 — L'audio suit-il l'image ? · `ouverte` · 2026-09-05

Axe 5. MPEG-I Immersive Audio couvre le 6DoF `[B]`, l'ambisonie distribuée existe `[B]`.

**Question ouverte** : existe-t-il une chaîne où captation volumétrique visuelle et captation
sonore 6DoF sont réellement synchronisées et alignées spatialement, ou est-ce systématiquement
recollé en post-production ?

**Pourquoi ça compte** : si c'est toujours recollé, c'est un manque de la chaîne — donc
potentiellement un sujet de R&D propre plutôt qu'un simple choix d'outil.
