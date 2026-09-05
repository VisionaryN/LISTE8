# Claude Code en terminal — installation et exploitation

Guide de déploiement de Claude Code en ligne de commande, et de ce qu'il faut mettre en place
pour en tirer réellement parti. Les fichiers cités en exemple existent dans ce dépôt.

> Les commandes évoluent. En cas de doute, `claude --help` en shell et `/help` dans la session
> font foi ; la documentation officielle est sur <https://code.claude.com/docs>.

---

## 1. Installation

### macOS / Linux / WSL

```bash
curl -fsSL https://claude.com/install.sh | bash
```

L'installeur natif ne demande ni Node ni npm. Il place le binaire dans `~/.local/bin` —
vérifiez que ce répertoire est dans votre `PATH`.

### Windows (PowerShell)

```powershell
irm https://claude.com/install.ps1 | iex
```

Sur Windows, WSL2 reste l'environnement le plus confortable : les outils que Claude Code
manipule (git, grep, make) y sont natifs.

### Via npm

```bash
npm install -g @anthropic-ai/claude-code
```

Nécessite Node.js 18 ou supérieur. À privilégier si vous gérez déjà vos outils par npm.
N'installez **pas** avec `sudo`.

### Vérification

```bash
claude --version   # version installée
claude doctor      # diagnostic : installation, PATH, permissions, connectivité
claude update      # mise à jour
```

`claude doctor` est le premier réflexe devant n'importe quel comportement anormal.

---

## 2. Authentification

Trois voies, exclusives entre elles :

| Voie | Mise en place | Facturation |
|---|---|---|
| Abonnement Claude (Pro / Max) | `claude` puis `/login`, navigateur | Forfait mensuel |
| Clé API Console | `export ANTHROPIC_API_KEY=sk-ant-…` | À l'usage |
| Entreprise | Variables Bedrock (AWS) ou Vertex (GCP) | Via votre cloud |

`/login` et `/logout` gèrent la session depuis le REPL. Ne committez jamais une clé API :
mettez-la dans votre `~/.zshrc` / `~/.bashrc`, ou dans `.claude/settings.local.json`
(ignoré par git dans ce dépôt).

---

## 3. Premiers pas

```bash
cd /chemin/vers/LISTE8
claude                        # session interactive (REPL)
claude "corrige le doublon"   # session interactive avec un prompt initial
claude -p "résume 8LISTE.json"  # mode headless : répond, écrit sur stdout, sort
claude --continue             # reprend la dernière session de ce répertoire
claude --resume               # choisit une session passée dans une liste
```

Le mode headless (`-p`) est ce qui rend Claude Code scriptable : il s'enchaîne avec des pipes,
tourne en CI, alimente un `Makefile`.

```bash
git diff | claude -p "résume ce diff en une ligne pour un message de commit"
```

---

## 4. Les quatre leviers de configuration

C'est ici que se joue le « plein potentiel ». Un terminal sans ces fichiers redécouvre le
projet à chaque session et demande une autorisation à chaque action.

### 4.1 Mémoire projet — `CLAUDE.md`

Chargée automatiquement au démarrage de chaque session. Contient le contexte que vous ne
voulez plus jamais retaper : rôle du projet, format des données, invariants, conventions.

- `CLAUDE.md` à la racine → partagé par l'équipe, versionné.
- `~/.claude/CLAUDE.md` → vos préférences personnelles, tous projets confondus.
- Un `CLAUDE.md` dans un sous-répertoire est chargé quand on y travaille.

`/init` en génère un premier jet à partir du code existant.
Le raccourci `#` en début de message écrit directement dans la mémoire.

**Gardez-le court** : il est relu à chaque tour. Le détail va dans `docs/`.

Exemple : [`CLAUDE.md`](../CLAUDE.md) à la racine de ce dépôt.

### 4.2 Permissions — `settings.json`

Hiérarchie, du plus faible au plus fort :

```
~/.claude/settings.json           réglages personnels, tous projets
.claude/settings.json             réglages du projet, versionnés
.claude/settings.local.json       réglages locaux, non versionnés
réglages entreprise               imposés par l'organisation
```

Sans allowlist, vous validez manuellement chaque `git diff`. C'est le principal facteur de
lenteur en usage réel. Pré-autorisez ce qui est sans effet de bord, refusez explicitement ce
qui est destructeur.

Exemple : [`.claude/settings.json`](../.claude/settings.json).

`/permissions` affiche et modifie les règles actives depuis la session.

### 4.3 Sous-agents — `.claude/agents/*.md`

Un sous-agent tourne dans **sa propre fenêtre de contexte**, avec son prompt système et une
liste d'outils restreinte. Il ne renvoie au fil principal que sa conclusion.

Deux bénéfices distincts : le travail volumineux (fouiller, relire, tester) ne pollue pas la
conversation principale, et plusieurs agents peuvent travailler en parallèle.

```markdown
---
name: explorateur
description: À utiliser dès qu'il faut localiser quelque chose dans le dépôt…
tools: Read, Grep, Glob
model: sonnet
---

<prompt système>
```

Trois points font la différence entre un agent utile et un agent ignoré :

1. **La `description` est un déclencheur, pas un CV.** C'est elle que le modèle principal lit
   pour décider de déléguer. Écrivez « À utiliser dès que… », pas « Expert en… ».
2. **Restreignez `tools`.** Champ omis ⇒ l'agent hérite de tout. Un agent de lecture privé
   d'écriture ne peut rien casser.
3. **Imposez un format de sortie.** Sans ça, le retour est verbeux et inexploitable.

Les cinq agents de ce dépôt sont dans [`.claude/agents/`](../.claude/agents/).
`/agents` liste ceux que le CLI a effectivement chargés.

### 4.4 Commandes slash — `.claude/commands/*.md`

Un fichier = une commande `/nom`. Le corps est un prompt, avec deux mécanismes :

- `$ARGUMENTS` (ou `$1`, `$2`) — les paramètres passés à la commande ;
- `` !`commande` `` — injecte la sortie d'un shell dans le contexte avant exécution.

Exemple : [`.claude/commands/revue.md`](../.claude/commands/revue.md) injecte `git diff`
puis délègue à l'agent `relecteur`.

**Commande, agent, skill — la différence :** une commande est déclenchée *explicitement* par
vous ; un agent est choisi *par le modèle* d'après sa `description` ; une skill se charge
*automatiquement* quand le contexte correspond.

---

## 5. Modes de permission

| Mode | Comportement |
|---|---|
| `default` | Demande confirmation à la première utilisation de chaque outil |
| `acceptEdits` | Accepte les modifications de fichiers sans demander |
| `plan` | Analyse et propose un plan, sans rien modifier |
| `bypassPermissions` | Ne demande plus rien |

Le mode plan est le bon réflexe pour tout changement non trivial : vous validez l'approche
avant qu'une ligne soit écrite.

`--dangerously-skip-permissions` désactive toutes les vérifications. À réserver à un
conteneur isolé et jetable, sur un dépôt dont vous acceptez la perte. Jamais sur votre poste.

---

## 6. Extensions

### Hooks

Des commandes shell déclenchées par des événements du cycle de vie : `PreToolUse`,
`PostToolUse`, `SessionStart`, `Stop`, entre autres. Déclarés dans `settings.json`,
configurables via `/hooks`.

Usage typique : formater automatiquement après chaque écriture, bloquer une commande
interdite, charger un contexte au démarrage de session.

Différence essentielle avec une instruction dans `CLAUDE.md` : un hook est exécuté par le
harnais, de façon déterministe. Une instruction est une consigne que le modèle peut oublier.

### Serveurs MCP

MCP (Model Context Protocol) branche Claude Code sur des outils externes : bases de données,
issue trackers, API internes.

```bash
claude mcp add <nom> -- <commande du serveur>          # transport stdio
claude mcp add --transport http <nom> <url>            # transport HTTP
claude mcp list
```

Portées : `local` (vous seul, ce projet), `project` (versionné dans `.mcp.json`, partagé),
`user` (vous, tous projets). `/mcp` gère les connexions en session.

### Intégrations

- **IDE** — extensions VS Code et JetBrains ; `/ide` connecte la session au diagnostic
  de l'éditeur.
- **Claude Code sur le web** — <https://claude.ai/code>, sessions dans un conteneur distant
  sur un clone du dépôt.
- **GitHub Actions** — Claude Code en CI, sur les PR et les issues.
- **Agent SDK** — pour construire vos propres agents sur le même moteur.

---

## 7. Ergonomie du terminal

| Raccourci / commande | Effet |
|---|---|
| `/terminal-setup` | Configure Shift+Entrée pour le retour à la ligne |
| `@chemin/fichier` | Mentionne un fichier — l'ajoute au contexte |
| `#` en début de message | Écrit la ligne dans la mémoire projet |
| `Échap` | Interrompt Claude en cours de réponse |
| `Échap` `Échap` | Revient sur un message précédent pour le modifier |
| `Ctrl+B` | Bascule une commande longue en arrière-plan |
| Coller une image | Analyse directe (capture d'écran, maquette) |
| `/vim` | Édition modale dans le prompt |
| `/clear` | Vide le contexte — nouvelle tâche, session propre |
| `/compact` | Résume le contexte pour continuer une session longue |
| `/model` | Change de modèle en cours de session |
| `/context` | Montre ce qui occupe la fenêtre de contexte |
| `/cost`, `/usage` | Consommation de la session, quota |
| `/rewind` | Revient à un état antérieur de la conversation |
| `/status` | État de la session : compte, modèle, répertoire |

Deux réflexes qui changent tout au quotidien : `/clear` entre deux tâches sans rapport
(un contexte encombré dégrade les réponses), et le mode plan avant les changements risqués.

---

## 8. Vérifier que le dépôt est bien configuré

```bash
cd /chemin/vers/LISTE8
claude
```

Puis, en session :

```
/agents            → les cinq agents du dépôt apparaissent
/permissions       → les règles de .claude/settings.json sont chargées
/verifier-liste    → le rapport de gardien-donnees s'affiche
/context           → CLAUDE.md est bien présent dans le contexte
```

Si l'un de ces points échoue, `claude doctor` puis vérifiez que vous avez lancé `claude`
depuis la racine du dépôt — les fichiers `.claude/` sont résolus par rapport au répertoire
de travail.
