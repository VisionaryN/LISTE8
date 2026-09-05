---
description: Session de veille sur un axe du volumétrique — lit la base, cherche le nouveau, rapporte le delta
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Write, Edit, Bash, Task
argument-hint: "[capture|representation|compression|projection|audio|production]"
---

Dernière entrée du journal :

!`head -30 docs/rnd-volumetrique/journal.md`

Pistes actuellement ouvertes :

!`grep -n "· \`ouverte\` ·" docs/rnd-volumetrique/pistes.md`

Date du jour :

!`date +%Y-%m-%d`

Délègue à l'agent `rnd-volumetrique` une session de veille.

Axe demandé : `$ARGUMENTS` — si vide, balaie les six axes en surface ; si un axe est nommé,
creuse celui-là seul et en profondeur.

Consignes à lui transmettre :

1. Lire l'axe correspondant dans `docs/rnd-volumetrique/etat-de-lart.md` **avant** de chercher.
2. Ne rapporter que le **delta** : ce qui n'est pas déjà dans la base. Une confirmation de ce
   qui y figure déjà se traduit par une promotion de niveau (`[B]` → `[A]`), pas par une
   nouvelle entrée.
3. Vérifier si une piste ouverte trouve sa réponse. Si oui, la clore avec sa conclusion.
4. Écrire dans la base avant de rendre : entrée datée dans `journal.md`, mises à jour d'axe,
   pistes créées ou closes.

Restitue le rapport de l'agent tel quel.
