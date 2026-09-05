---
description: Enregistre une nouvelle piste de recherche dans la base volumétrique
allowed-tools: Read, Edit, Bash
argument-hint: "<description de la piste>"
---

Pistes existantes (pour numéroter la suivante et détecter les doublons) :

!`grep -n "^## P-" docs/rnd-volumetrique/pistes.md`

Date du jour :

!`date +%Y-%m-%d`

Ajoute une piste à `docs/rnd-volumetrique/pistes.md` à partir de : `$ARGUMENTS`

Format à respecter, identique aux pistes existantes :

```
## P-00N — <titre court> · `ouverte` · <date>

<le contexte, l'axe concerné, ce que la base dit déjà du sujet>

**À faire** : <l'action concrète qui ferait avancer la piste>
```

Deux règles :

- **Vérifie d'abord qu'une piste équivalente n'existe pas.** Si c'est le cas, enrichis-la au
  lieu d'en créer une seconde, et dis-le.
- Si la description est trop vague pour qu'on sache quoi faire dans six mois, demande une
  précision plutôt que d'écrire une piste inexploitable.

N'ajoute pas d'entrée au journal : une piste capturée n'est pas une session de travail.
