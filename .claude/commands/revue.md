---
description: Revue du diff courant à la recherche de bugs de correction
allowed-tools: Read, Grep, Glob, Bash, Task
argument-hint: "[fichier ou zone à cibler]"
---

État du dépôt :

!`git status --short`

Diff non indexé :

!`git diff`

Diff indexé :

!`git diff --staged`

Délègue à l'agent `relecteur` la revue de ces changements.

Ciblage demandé : `$ARGUMENTS` — s'il est vide, relis l'intégralité du diff ;
sinon, concentre la revue sur cette zone.

Rappelle à l'agent les invariants de `CLAUDE.md`, en particulier ceux qui portent sur
`8LISTE.json` (format EUI-64, majuscules, absence de doublon, indentation 2 espaces).

Restitue le verdict et les findings tels quels. N'applique aucune correction sans
validation explicite.
