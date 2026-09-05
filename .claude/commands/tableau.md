---
description: Republie le tableau de bord Atelier Volumétrique à partir de l'état courant de la base
allowed-tools: Read, Grep, Glob, Write, Edit, Bash, Artifact
argument-hint: ""
---

État courant de la base :

!`wc -l docs/rnd-volumetrique/*.md`

Republie le tableau de bord **Atelier Volumétrique**.

URL de l'artifact : <https://claude.ai/code/artifact/cf493b42-a4dd-4ecb-b5f0-1284f4159fee>
Passe-la en paramètre `url` de l'outil `Artifact` — sans elle, la republication crée un
**nouveau** tableau au lieu de mettre à jour celui-ci.

Procédure, dans l'ordre :

1. **Relire les captures faites sur la page.** `Artifact` avec `action: "read_db"` sur les
   collections `pistes` et `captures`. Ce sont les notes prises directement dans le navigateur,
   qui n'existent pas encore dans le dépôt.
2. **Curer.** Pour chaque capture pertinente, l'intégrer à `pistes.md` (numérotée) ou à l'axe
   correspondant de `etat-de-lart.md`. Une capture qui n'apporte rien est laissée en base, pas
   promue — mais dis lesquelles tu as écartées et pourquoi.
3. **Régénérer** `dashboard/atelier-volumetrique.html` depuis les fichiers Markdown à jour.
4. **Republier** avec `Artifact` sur le **même chemin de fichier**, pour conserver l'URL.
   Ne passe pas `favicon` : l'artifact garde son icône.
5. **Journaliser** l'opération dans `journal.md` si des captures ont été curées.

Le contenu affiché vient exclusivement de la base. Aucune donnée en dur, aucun exemple inventé
pour remplir un axe vide : un axe vide s'affiche comme vide.
