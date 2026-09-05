---
description: Un tour de tous les agents — chacun avance son chantier d'un pas et écrit son état
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Task, WebSearch, WebFetch, Artifact
argument-hint: "[nom d'un agent, pour ne faire tourner que celui-là]"
---

État des chantiers :

!`grep -H "^\*\*Statut\*\*" docs/chantiers/*.md | sed 's|docs/chantiers/||;s|\.md:\*\*Statut\*\* : |  →  |'`

Questions encore sans réponse :

!`grep "^### Q-" docs/contexte/ouvert.md`

Date du jour :

!`date +%Y-%m-%d`

---

Fais tourner un **tour**. Cible : `$ARGUMENTS` — si vide, tous les agents de domaine.

Lance les agents concernés **en parallèle**, dans un seul message. Chacun reçoit la même
consigne :

1. Lis ton fichier `docs/chantiers/<toi>.md`. Reprends à la prochaine action qui y est écrite.
2. **Avance d'un pas.** Un seul. Un tour n'est pas une session de travail complète : c'est un
   pas concret et fini, qui laisse le chantier dans un état meilleur qu'au début.
3. Si tu es bloqué, ne tourne pas à vide : vérifie si le blocage peut être levé **sans Noah**
   (une recherche, un email à écrire, une vérification technique). S'il ne peut pas l'être,
   dis-le en une ligne et arrête-toi. Ne réinvente pas du travail pour paraître occupé.
4. Réécris ton fichier d'état : statut, avancée datée, **une seule** prochaine action, blocage.

Ensuite, dans le fil principal :

- Republie la vision d'ensemble avec `/tableau-agents`.
- Écris le récapitulatif du tour dans `docs/chantiers/journal-des-tours.md`, en tête.
- Commit et push.

## Ce qu'on rend à Noah

Court. Aéré. Ce qui a bougé, ce qui bloque, rien d'autre.

```
## Tour du <date>

<agent> — <ce qui a avancé, une ligne>
<agent> — <…>

## Bloqué
<agent> — <ce qui manque>

## Une question, si vraiment nécessaire
<une seule, ou rien>
```

**Aucun agent ne pose deux questions dans le même tour.** Et jamais une question déjà présente
dans `ouvert.md`.
