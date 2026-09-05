---
description: Contrôle d'intégrité de 8LISTE.json (format EUI-64, doublons, casse, JSON)
allowed-tools: Read, Bash, Task
argument-hint: "[corriger]"
---

Contenu actuel du fichier :

!`cat 8LISTE.json`

Délègue à l'agent `gardien-donnees` la validation complète de `8LISTE.json` :
JSON valide, structure, format EUI-64 de chaque entrée, doublons insensibles à la casse,
et statistiques de préfixes.

Argument reçu : `$ARGUMENTS`

- Si l'argument vaut `corriger`, demande à l'agent d'appliquer les correctifs sûrs
  (normalisation de la casse, suppression des doublons stricts) puis de revalider.
- Sinon, rapport en lecture seule uniquement — aucune modification du fichier.

Restitue le rapport de l'agent tel quel, sans le reformuler.
