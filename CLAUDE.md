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
| `rnd-volumetrique` | Toute question de R&D en audiovisuel volumétrique : capture, représentation, compression, projection, audio spatial. |

## Commandes

- `/verifier-liste` — contrôle d'intégrité de `8LISTE.json`.
- `/revue` — revue du diff courant.
- `/veille [axe]` — session de veille volumétrique.
- `/piste "…"` — capture une piste de recherche.
- `/tableau` — republie le tableau de bord.

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
