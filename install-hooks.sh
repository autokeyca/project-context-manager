#!/bin/bash
# Install journal auto-summary hooks for Claude Code
#
# This script installs:
# - journal-summarize: Extracts meaningful summaries from Claude transcripts
# - claude-session-end: Session end hook that journals with auto-summaries
#
# Run from the project-context-manager directory:
#   ./install-hooks.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="$HOME/.local/bin"

echo "Installing journal auto-summary hooks..."
echo "Source: $SCRIPT_DIR/scripts"
echo "Target: $INSTALL_DIR"
echo

# Create target directory if needed
mkdir -p "$INSTALL_DIR"

# Install journal-summarize
echo "Installing journal-summarize..."
cp "$SCRIPT_DIR/scripts/journal-summarize" "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/journal-summarize"
echo "  ✅ Installed: $INSTALL_DIR/journal-summarize"

# Check if claude-session-end exists and offer to update
if [ -f "$INSTALL_DIR/claude-session-end" ]; then
    echo
    echo "⚠️  claude-session-end already exists at $INSTALL_DIR/claude-session-end"
    read -p "   Overwrite with new version? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp "$SCRIPT_DIR/scripts/claude-session-end" "$INSTALL_DIR/"
        chmod +x "$INSTALL_DIR/claude-session-end"
        echo "  ✅ Updated: $INSTALL_DIR/claude-session-end"
    else
        echo "  ⏭️  Skipped: $INSTALL_DIR/claude-session-end"
    fi
else
    cp "$SCRIPT_DIR/scripts/claude-session-end" "$INSTALL_DIR/"
    chmod +x "$INSTALL_DIR/claude-session-end"
    echo "  ✅ Installed: $INSTALL_DIR/claude-session-end"
fi

echo
echo "Installation complete!"
echo
echo "To enable auto-journaling, add this to ~/.claude/settings.json:"
echo
cat << 'EOF'
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "~/.local/bin/claude-session-end 2>/dev/null || true"
      }]
    }]
  }
EOF
echo
echo "Journal entries will now include auto-generated summaries of:"
echo "  - Files created/modified"
echo "  - Significant commands run"
echo "  - Session topics (when no file changes)"
