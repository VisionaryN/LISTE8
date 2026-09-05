# Veille — sources suivies

Ce qu'on surveille, et **pourquoi**. Une source sans raison d'être suivie est une source à retirer.

## Conférences

| Source | Rythme | Pourquoi |
|---|---|---|
| SIGGRAPH / SIGGRAPH Asia | annuel (août) | Où sortent les papiers qui deviennent les outils de l'année suivante. Suivre la liste tenue par realtimerendering. → <https://www.realtimerendering.com/kesen/sig2026.html> |
| CVMP (ACM SIGGRAPH European Conference on Visual Media Production) | annuel | Plus proche de la production réelle que SIGGRAPH. C'est là qu'ont paru les pipelines de captation. |
| Réunions MPEG (WG3 / WG7) | ~trimestriel | Rythme les standards de compression volumétrique. Les comptes rendus donnent les passages d'étape. → <https://www.mpeg.org/> |
| SID Display Week | annuel (mai) | L'affichage. C'est là qu'a été primé le HLD de Looking Glass en 2026. |

## Suivi des champs de radiance

| Source | Pourquoi |
|---|---|
| radiancefields.com | Agrégateur dédié aux champs de radiance et au splatting. Le point d'entrée le plus dense de l'axe 2. → <https://radiancefields.com/research> |
| arXiv cs.CV / cs.GR | Source primaire. Filtrer sur *gaussian splatting*, *volumetric video*, *light field display*. |

## Acteurs industriels

| Acteur | Axe | Pourquoi le suivre |
|---|---|---|
| Evercoast (+ Depthkit) | 6 | Consolidation du secteur ; définit de fait le pipeline de référence. → <https://www.depthkit.tv/depthkit-studio> |
| Volucap | 1 | Captation haut de gamme, référence européenne. |
| Looking Glass | 4 | Le seul acteur avec une gamme d'écrans à champ lumineux réellement achetable. → <https://lookingglassfactory.com/> |
| Samsung (Spatial Signage) | 4 | Entrée d'un industriel de masse sur l'affichage 3D sans lunettes. Change l'échelle du marché. |
| Orbbec | 1 | Successeur de fait d'Azure Kinect ; conditionne les choix de capteurs. → <https://www.orbbec.com/> |
| Zylia | 5 | Ambisonie 6DoF, un des rares à outiller l'axe audio. → <https://www.zylia.co/zylia-6dof.html> |

## Normalisation

| Norme | Statut connu au 2026-09-05 | À surveiller |
|---|---|---|
| ISO/IEC 23090-5 (V3C / V-PCC) | `[B]` FDIS, 4ᵉ édition, oct. 2025 | Publication effective. |
| Amendement profil V-PCC pour splats gaussiens | `[B]` en cours | **Le point le plus important de la veille normative.** |
| ISO/IEC 23090-10 (portage V3C) | `[B]` 2ᵉ éd., CD | FDIS attendu fin 2026. |
| ISO/IEC 23090-38 (E-G-PCC) | `[B]` en développement | Prédiction temporelle pour le dynamique. |
| ISO/IEC 23090-40 (conformance E-G-PCC) | `[B]` CD | — |
| ISO/IEC 23090-4 (MPEG-I Immersive Audio) | `[B]` publié ? | Statut exact à confirmer. |

## Angles morts assumés

Ce qu'on ne suit **pas**, et pourquoi — à réévaluer si le projet change de nature :

- Casques VR/AR grand public : consommateurs de volumétrique, pas producteurs.
- Génération 3D par IA à partir de texte : sujet voisin mais distinct de la captation du réel.
- Télé-présence temps réel : dépend des mêmes briques mais impose des contraintes de latence
  qui changent tous les arbitrages.
