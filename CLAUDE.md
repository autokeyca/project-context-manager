# Project Context Manager

## Purpose

Tool for onboarding projects into Elle's two-tier context system. Creates standardized `.claude/` directory structure with documentation, rules, and journals for any project.

## Quick Start

```bash
cd /home/ja/projects/project-context-manager

# Onboard a project
python3 onboard.py /path/to/project

# Interactive mode
python3 onboard.py

# Skip existing files (don't overwrite)
python3 onboard.py /path/to/project --skip-existing
```

## Key Files

- **onboard.py** - Main onboarding script (executable)
- **PROJECT-CONTEXT-TEMPLATE.md** - Template reference (from global context)
- **README.md** - Comprehensive documentation and usage guide
- **CLAUDE.md** - This file (quick reference)

## What It Does

1. **Asks project-specific questions** (not personal questions):
   - Project name and purpose
   - Tech stack and architecture
   - Integrations and environment
   - Known gotchas

2. **Creates `.claude/` directory** with:
   - `CLAUDE.md` - Quick reference
   - `context.md` - Comprehensive docs
   - `tech-stack.md` - Technical specifications
   - `rules.md` - Project-specific rules
   - `next-steps.md` - Prioritized roadmap
   - `session.md` - Current work (ephemeral)
   - `journal/` - Daily work logs

3. **Updates .gitignore** to exclude `session.md`

## Two-Tier Context System

**Global**: `~/.claude/.context/core/` - Personal context (you, family, preferences)
**Project**: `<project>/.claude/` - Work context (architecture, tech, decisions)

Both are loaded by Claude Code when working on a project.

## Usage Patterns

### Onboard New Project

```bash
python3 onboard.py /home/ja/projects/new-project
# Follow prompts
# Result: new-project/.claude/ created
```

### Batch Onboard

```bash
# Onboard all projects in a directory
for dir in /home/ja/projects/bots/*/; do
    python3 onboard.py "$dir" --skip-existing
done
```

### Update Existing Context

Just edit the files:
```bash
cd /path/to/project
nano .claude/context.md  # Update architecture
nano .claude/rules.md    # Add new rule
```

## Git Integration

**Commits to project repo**:
- All `.claude/` files EXCEPT `session.md`
- `session.md` excluded via `.gitignore`

**Can be shared with team**:
- Project context in project repo
- Personal context stays in private repo

## Requirements

- Python 3.8+
- No external dependencies (uses only stdlib)
- Git (optional, for tracking changes)

## Integration with Claude Code

When Claude Code works on a project:
1. Auto-detects `.claude/` directory
2. Loads global context from `~/.claude/.context/`
3. Loads project context from `.claude/`
4. Has full two-tier context available

## Development

This project uses its own context system:
- `.claude/` directory tracks its own development
- Project journal documents changes
- Meta: A context manager that manages itself!

## Important Notes

- **Project questions only** - Script doesn't ask personal questions
- **Non-destructive** - Use `--skip-existing` to avoid overwriting
- **Template-based** - Creates consistent structure across all projects
- **Flexible** - Edit any file after creation to customize

## Example Projects

Already onboarded with this tool:
- Elle Bot (`/home/ja/projects/bots/elle_bot`)
- More to come...
