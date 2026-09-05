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

## Étape zéro — ce que Noah a dit sur la page

Avant de lancer quoi que ce soit, relis la base de la page **Mes Agents**
(<https://claude.ai/code/artifact/1a69e5fc-7256-4307-bc97-a5915733d729>) avec l'outil `Artifact`, `action: "read_db"` :

1. Collection `reponses` — chaque document non `traite` est une réponse à une question ouverte.
   Déplace la question de `docs/contexte/ouvert.md` vers la section **Répondu**, avec la
   réponse telle quelle et la date. Puis `write_db` `update` sur le document : `traite: true`.
2. Collection `consignes` — chaque document non `traite` est une consigne pour un agent.
   Ajoute-la en tête du fichier `docs/chantiers/<agent>.md`, sous un titre **Consigne de Noah
   (date)**. L'agent la lira avant d'avancer. Puis `traite: true`.

Ne supprime jamais un document : marqué traité, il reste lisible. Rapporte en une ligne
combien de réponses et de consignes ont été reprises.

## Le tour

Fais tourner un **tour**. Cible : `$ARGUMENTS` — si vide, tous les agents de domaine.

Lance les agents concernés **en parallèle**, dans un seul message. Chacun reçoit la même
consigne :

1. Lis ton fichier `docs/chantiers/<toi>.md`. S'il y a une **Consigne de Noah** en tête, elle
   prime sur la prochaine action prévue. Sinon, reprends à la prochaine action.
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
