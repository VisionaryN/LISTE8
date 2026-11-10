# Bouchons de valve « croix » (valve Schrader moto, filetage 8V1 0.305″-32 UNEF)

Le filetage est logé tout en haut de la branche verticale (1,5 mm sous le sommet).
Le bas de la croix est un manchon presque droit (Ø int 11 → 12, paroi 1,4) qui descend jusqu'à 2 mm de la jante.

| Fichier | Hauteur de tige H (haut de valve → jante) | Dimensions (mm) | Masse résine |
|---|---|---|---|
| `bouchon_croix_H22.stl` | 22 à 31 mm (TR412) | 21,5 × 14,8 × 21,5 | ≈ 2,0 g |
| `bouchon_croix_H32.stl` | 32 mm et plus (TR413) | 26 × 14,8 × 31,5 | ≈ 3,2 g |

- Valve supposée à corps droit, Ø ≤ 10,4 mm sous la collerette.
- Unités : millimètres, échelle 100 %. Ne pas redimensionner (taraudage au pas réel 0,794 mm).
- Orientation : ouverture vers le haut, sommet du bouchon à z = 0. Surélever de 3 à 5 mm sur supports dans le slicer.
- Taraudage : Ø 8,00 fond / Ø 7,15 sommet (jeu ≈ 0,25 mm au diamètre pour la résine).
- Autre hauteur de tige : `pip install manifold3d numpy`, modifier `version_v3(H)` dans `model.py`, puis `python model.py <dossier>`.

![aperçu](apercu.png)
