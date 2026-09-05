# LISTE8

Registre de numéros de série d'appareils, au format EUI-64.

## Données

Source unique : `8LISTE.json`.

```json
{
  "serialNumbers": [
    "E0:04:01:53:08:C3:76:42"
  ]
}
```

- Clé racine `serialNumbers`, tableau de chaînes.
- Chaque entrée : 8 octets hexadécimaux **majuscules**, séparés par `:`.
- Regex de référence : `^([0-9A-F]{2}:){7}[0-9A-F]{2}$`

### Invariants à ne jamais casser

1. Aucun doublon (comparaison insensible à la casse).
2. Hexadécimal en majuscules.
3. Ordre stable — on ajoute en fin de tableau, on ne réordonne pas sans raison explicite.
4. JSON indenté à 2 espaces, newline finale.

Toute modification de `8LISTE.json` doit être vérifiée avec `/verifier-liste` avant commit.

## Conventions

- Messages de commit en français, à l'impératif (« Ajoute… », « Corrige… »).
- Jamais de push direct sur `main` — travailler sur une branche.
- Pas de dépendance ajoutée sans nécessité : le projet est volontairement minimal.

## Sous-agents disponibles

| Agent | Quand l'utiliser |
|---|---|
| `explorateur` | Localiser du code ou comprendre une partie du dépôt, en lecture seule. |
| `relecteur` | Relire un diff avant commit, chercher les bugs de correction. |
| `testeur` | Écrire ou exécuter des tests. |
| `gardien-donnees` | Valider ou corriger `8LISTE.json`. |
| `redacteur-doc` | Rédiger ou mettre à jour README, CLAUDE.md, `docs/`. |
| `rnd-volumetrique` | R&D en audiovisuel volumétrique, et le périmètre de la Plateforme Volumetric. |
| `ajm-renaissance` | La relance de l'AJM : comité, pôles, 40 ans, fédération, droit monégasque. |
| `arts-digitaux` | L'Association Monégasque des Arts Digitaux et la Digital Art Week 2027. |
| `identite-vn8` | Identité visuelle et direction artistique — gardien du test Palais / maillot de bain. |
| `studio-web` | ajm.studio en production. Toute livraison vérifiée en mobile. |
| `fabrication-3d` | Impression résine, chaîne STL → .goo, calibration. |
| `entreprise-prod` | L'entreprise de production. Commence par demander le secteur, ne le devine jamais. |
| `mise-en-ligne` | Publier et rendre un lien partageable. Fini seulement quand le lien est rendu. |

Les cinq premiers servent le code. Les huit suivants sont **les agents de Noah**, un par
chantier. Chacun lit `docs/contexte/` et son fichier `docs/chantiers/<nom>.md` avant d'agir, et
y réécrit son état en fin de tour.

## Commandes

- `/verifier-liste` — contrôle d'intégrité de `8LISTE.json`.
- `/revue` — revue du diff courant.
- `/veille [axe]` — session de veille volumétrique.
- `/piste "…"` — capture une piste de recherche.
- `/tableau` — republie le tableau de bord volumétrique.
- `/tour [agent]` — un tour : chaque agent de domaine avance son chantier d'un pas.
- `/tableau-agents` — republie la vision d'ensemble des agents.

## Mes agents

Un agent par chantier, et du travail en continu.

- Vision d'ensemble : https://claude.ai/code/artifact/1a69e5fc-7256-4307-bc97-a5915733d729
  Interactive : Noah y répond aux questions ouvertes, laisse des consignes, et parle à chaque
  agent. Tout est enregistré (`db`, collections `reponses` et `consignes`) et repris par
  l'étape zéro de `/tour`. Parler, c'est immédiat ; agir, c'est au tour.
- Mémoire partagée : `docs/contexte/` — `handoff.md` (la source), `ouvert.md` (les questions
  sans réponse : chacune se pose **une fois**), `lexique.md` (sigles et déformations de dictée).
- État des chantiers : `docs/chantiers/` — un fichier par agent, plus `journal-des-tours.md`.
- Direction artistique : `docs/direction-artistique.md` — **négociable**, sauf le test
  Palais / maillot de bain et la réserve du terre cuite aux blocages.
- Routine « Tour des agents — chaque matin » : tire à 04:00 UTC (06:00 Monaco) dans une
  session neuve, fait un `/tour`, republie la vision d'ensemble, commit, push, notifie le
  téléphone. Se met en pause depuis la liste des routines de Noah.
- Installation globale : double-clic sur `installer-agents.command`.

Règles pour tout agent de Noah : montrer, pas expliquer · court, aéré, le résultat d'abord ·
agir plutôt que demander · corriger les déformations de dictée en silence · il teste tout sur
son téléphone.

## R&D — audiovisuel volumétrique

Chantier de recherche au long cours, distinct du registre `8LISTE.json`.

- Base de connaissances : `docs/rnd-volumetrique/` — voir son `README.md`.
- Tableau de bord : https://claude.ai/code/artifact/cf493b42-a4dd-4ecb-b5f0-1284f4159fee
- Règle non négociable : **rien n'entre dans la base sans source datée**, avec son niveau
  de confiance (`[A]` vérifié · `[B]` sourcé · `[C]` piste). Ne jamais affirmer de mémoire
  sur ce domaine : recherche web, ou silence explicite.

## Documentation

- `docs/claude-code-terminal.md` — installer et exploiter Claude Code en terminal.
- `docs/rnd-volumetrique/` — base de veille sur la capture et la projection volumétriques.
