# R&D — Audiovisuel volumétrique

Base de connaissances vivante sur la capture et la projection volumétriques.
Maintenue par le sous-agent `rnd-volumetrique`, consultable dans le tableau de bord
**Atelier Volumétrique** : <https://claude.ai/code/artifact/cf493b42-a4dd-4ecb-b5f0-1284f4159fee>

## Comment s'en servir

| Fichier | Quand l'ouvrir |
|---|---|
| `etat-de-lart.md` | « Où en est-on sur … ? » — le fond technique, par axe. |
| `veille.md` | « Qu'est-ce qu'on surveille ? » — sources, équipes, standards suivis. |
| `pistes.md` | « Qu'est-ce qu'on pourrait tenter ? » — hypothèses, expériences, questions ouvertes. |
| `journal.md` | « Qu'est-ce qui a changé depuis la dernière fois ? » — antéchronologique. |
| `glossaire.md` | Vocabulaire du domaine, FR ↔ EN. |

En terminal : `/veille [axe]` pour une session de veille, `/piste "…"` pour capturer une idée,
`/tableau` pour republier le tableau de bord.

## Les six axes

1. **Capture** — acquisition du réel : photogrammétrie, rigs multi-caméras, capteurs de profondeur.
2. **Représentation** — comment on stocke le volume : nuages de points, maillages animés,
   champs de radiance, splatting gaussien, champs lumineux.
3. **Compression & transport** — rendre diffusable ce qui est massif par nature.
4. **Restitution & projection** — redonner le volume à voir : écrans à champ lumineux,
   affichages volumétriques, projection.
5. **Audio spatial** — le pendant sonore. Une captation volumétrique sans son spatialisé
   n'est qu'à moitié faite.
6. **Chaîne de production** — outils, formats d'échange, pipeline de bout en bout.

## Échelle de confiance

Chaque affirmation de cette base porte un niveau. **La règle est stricte : rien n'entre sans
source datée.**

| Niveau | Signification |
|---|---|
| `[A]` | **Vérifié** — source primaire réellement ouverte et lue. |
| `[B]` | **Sourcé** — issu d'une recherche web, URL identifiée, page **non ouverte**. À promouvoir en `[A]`. |
| `[C]` | **Piste** — mention non recoupée. À confirmer ou à écarter. |

### État de l'amorçage (2026-09-05)

L'amorçage a été fait depuis un environnement où l'accès web direct était bloqué : la recherche
fonctionnait, l'ouverture des pages non. **Toutes les entrées initiales sont donc en `[B]` ou
`[C]`, aucune en `[A]`.**

Premier travail utile à faire depuis un terminal avec accès web : ouvrir les URL citées et
promouvoir les entrées en `[A]`, ou les corriger. C'est la piste `P-001`.
