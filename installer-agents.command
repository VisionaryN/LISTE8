#!/bin/bash
# Installe les agents de Noah pour qu'ils soient disponibles dans TOUS ses projets.
# Double-clic, ça marche. Volontairement non signé : Gatekeeper rejette les signatures ad-hoc.

set -e
DEPOT="$HOME/N8/liste8"
URL="https://github.com/VisionaryN/LISTE8"
BRANCHE="claude/deploy-claude-code-terminal-5ob47r"
CIBLE="$HOME/.claude/agents"

echo
echo "  ∞  Agents VN.8"
echo

# 1. Le dépôt : c'est là que vit la mémoire partagée (contexte, chantiers, DA).
if [ -d "$DEPOT/.git" ]; then
  echo "  → mise à jour du dépôt"
  git -C "$DEPOT" pull --quiet origin "$BRANCHE"
else
  echo "  → récupération du dépôt dans $DEPOT"
  mkdir -p "$(dirname "$DEPOT")"
  git clone --quiet --branch "$BRANCHE" "$URL" "$DEPOT"
fi

# 2. Les agents, copiés globalement, avec leurs chemins pointés vers le dépôt.
#    Une seule mémoire : les agents globaux écrivent dans $DEPOT/docs/, jamais ailleurs.
mkdir -p "$CIBLE"
n=0
for f in "$DEPOT"/.claude/agents/*.md; do
  nom=$(basename "$f")
  sed "s#\`docs/#\`$DEPOT/docs/#g; s# docs/# $DEPOT/docs/#g" "$f" > "$CIBLE/$nom"
  n=$((n+1))
done

echo "  → $n agents installés dans $CIBLE"
echo
echo "  Mémoire partagée : $DEPOT/docs/"
echo "  Ne touche pas à ~/.claude/settings.json — rien n'a été écrasé."
echo
echo "  Dans n'importe quel dossier :  claude   puis   /agents"
echo "  Pour un tour de tous les agents, dans $DEPOT :  /tour"
echo
read -n 1 -s -r -p "  Appuie sur une touche pour fermer."
echo
