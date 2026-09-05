---
description: Republie la vision d'ensemble des agents à partir de l'état des chantiers
allowed-tools: Read, Grep, Glob, Write, Edit, Bash, Artifact
argument-hint: ""
---

État courant :

!`grep -H -A2 "^\*\*Statut\*\*" docs/chantiers/*.md | head -60`

Republie la vision d'ensemble **Mes Agents**.

URL de l'artifact : <https://claude.ai/code/artifact/1a69e5fc-7256-4307-bc97-a5915733d729>
Passe-la en paramètre `url` de l'outil `Artifact` — sans elle, la republication crée une
**nouvelle** page au lieu de mettre à jour celle-ci.

Procédure :

1. Relis les huit fichiers de `docs/chantiers/` : statut, prochaine action, blocage.
2. Régénère `dashboard/mes-agents.html` à partir de ces fichiers. Rien en dur : ce qui
   s'affiche vient des fichiers.
3. Republie sur le **même chemin de fichier**, sans passer `favicon`.

Direction artistique : `docs/direction-artistique.md`. Elle est **négociable** — mais le terre
cuite `#b4694c` reste réservé aux blocages, et le test Palais / maillot de bain s'applique.

Vérifie le rendu à **390 px** avant de publier. Noah teste sur son téléphone.

Aucune donnée sensible sur la page : les noms du bureau, les numéros de téléphone et les
contacts restent dans le dépôt.
