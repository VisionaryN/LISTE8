# Glossaire

Français, avec l'équivalent anglais consacré. Les termes marqués `[C]` sont des définitions
d'usage à recouper.

---

**Champ lumineux** — *light field*
Description de la lumière traversant un volume, en tenant compte de la direction des rayons et
pas seulement de leur intensité en un point. Un écran à champ lumineux restitue des images
différentes selon l'angle de vue, d'où la 3D sans lunettes.

**Champ de radiance** — *radiance field*
Représentation continue d'une scène comme fonction donnant la couleur et la densité en tout
point de l'espace et dans toute direction. Famille qui englobe NeRF et le splatting gaussien.

**Splatting gaussien** — *Gaussian splatting*, *3DGS*
Représentation d'une scène par un très grand nombre de primitives gaussiennes anisotropes
projetées à l'écran. Rendu rapide, temps réel possible. `4DGS` en est l'extension temporelle,
pour le volumétrique animé.

**Vidéo volumétrique** — *volumetric video*
Captation d'un sujet par plusieurs caméras, reconstruite en modèle 3D visible sous n'importe
quel angle — par opposition à une image plate.

**Nuage de points** — *point cloud*
Ensemble de points 3D, chacun avec position et attributs (couleur, normale). Représentation
brute typique en sortie de capteurs de profondeur.

**6DoF** — *six degrees of freedom*
Liberté de se déplacer dans une scène selon trois translations et trois rotations. S'oppose au
3DoF, où l'on ne peut que tourner la tête depuis un point fixe. Le 6DoF est ce qui distingue
une vraie captation volumétrique d'une vidéo 360°.

**Ambisonie** — *Ambisonics*
Représentation du champ sonore par décomposition en harmoniques sphériques, indépendamment du
dispositif de restitution. `HOA` (*Higher Order Ambisonics*) = ordres supérieurs, plus précis
spatialement.

**Audio par objets** — *object-based audio*
Le son est décrit comme des sources positionnées dans l'espace plutôt que comme des canaux
fixes. Le rendu s'adapte au dispositif d'écoute.

**V-PCC** — *Video-based Point Cloud Compression*
Compression de nuages de points par projection sur des plans 2D, puis encodage avec des codecs
vidéo existants. ISO/IEC 23090-5.

**G-PCC** — *Geometry-based Point Cloud Compression*
Compression opérant directement sur la structure 3D, sans passer par la 2D. `E-G-PCC` en est
l'édition enrichie.

**V3C** — *Visual Volumetric Video-based Coding*
Cadre de codage général dont V-PCC est une instanciation.

**Affichage à volume balayé** — *swept-volume display* `[C]`
Écran volumétrique où une surface en mouvement rapide (rotation ou translation) compose, par
persistance rétinienne, un volume perçu.

**Affichage à volume statique** — *static volume display* `[C]`
Matrice de voxels émissifs, sans pièce en mouvement.

**Voxel aérien** — *aerial voxel* `[C]`
Point lumineux créé directement dans l'air, typiquement par plasma induit par laser
femtoseconde. Sans support matériel.

**Piégeage photophorétique** — *photophoretic trapping* `[C]`
Maintien d'une particule microscopique par un faisceau laser, déplacée rapidement pour tracer
une image dans l'espace.

**Photogrammétrie** — *photogrammetry*
Reconstruction 3D à partir de photographies multiples, par mise en correspondance de points de vue.

**Rig** — *rig*
Ensemble physique des caméras et capteurs synchronisés d'un banc de captation.
