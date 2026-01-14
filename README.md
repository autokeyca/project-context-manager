# Project Context Manager

A tool for onboarding projects into Elle's two-tier context system. Automatically creates project-specific context directories with journals, documentation, and rules.

## Purpose

This tool helps you:
- **Onboard new projects** with standardized `.claude/` context structure
- **Create project journals** for tracking development work
- **Maintain separation** between personal (global) and project (work) context
- **Ensure consistency** across all your projects

## Two-Tier Context System

**Global Context** (`~/.claude/.context/core/`)
- Personal information (identity, family, preferences)
- Cross-project rules and workflows
- Global journal tracking all sessions
- Lives in private GitHub repo: `autokeyca/elle-context`

**Project Context** (`<project>/.claude/`)
- Project-specific documentation and decisions
- Tech stack, architecture, integrations
- Project-specific rules and gotchas
- Project journal tracking work sessions
- Lives in each project's git repo (can be shared with team)

## Quick Start

### Onboard a New Project

```bash
cd /home/ja/projects/project-context-manager
python3 onboard.py /path/to/your/project
```

The script will:
1. Ask project-specific questions (purpose, tech stack, architecture)
2. Create `.claude/` directory structure
3. Generate initial documentation files
4. Create project journal directory
5. Initialize git tracking (if not already tracked)

### Interactive Mode

```bash
python3 onboard.py
```

Will prompt you for the project path.

### Skip Existing Files

```bash
python3 onboard.py /path/to/project --skip-existing
```

Won't overwrite existing `.claude/` files.

## What Gets Created

After onboarding, your project will have:

```
your-project/
├── .claude/
│   ├── CLAUDE.md              # Quick reference - project overview
│   ├── context.md             # Architecture, decisions, patterns
│   ├── tech-stack.md          # Dependencies, integrations, tools
│   ├── rules.md               # Project-specific rules and gotchas
│   ├── next-steps.md          # Prioritized roadmap
│   ├── session.md             # Current work state (ephemeral)
│   └── journal/               # Daily work logs
│       ├── README.md          # Journal format guide
│       └── YYYY-MM-DD.md      # Daily entries (created as needed)
├── .gitignore                 # Updated to exclude session.md
└── [your project files...]
```

## Project Onboarding Questions

The script asks **project-specific** questions (NOT personal questions):

1. **Project name** - What's this project called?
2. **Purpose** - What does it do? What problem does it solve?
3. **Status** - Development stage? Deployed? Planned?
4. **Tech stack** - Languages, frameworks, libraries?
5. **Architecture** - How is it structured?
6. **Integrations** - External services, APIs, databases?
7. **Environment** - Where does it run? What dependencies?
8. **Key gotchas** - Important quirks or issues to remember?

## File Descriptions

### CLAUDE.md
Quick reference file with:
- Project purpose
- Quick start commands
- Key file locations
- Important notes

### context.md
Comprehensive project documentation:
- Architecture overview
- Design decisions and reasoning
- Code patterns and conventions
- Integration details

### tech-stack.md
Technical specifications:
- Languages and versions
- Frameworks and libraries
- External services
- Development tools

### rules.md
Project-specific rules:
- Development guidelines
- Testing requirements
- Deployment procedures
- Things NOT to do (learned from mistakes)

### next-steps.md
Prioritized roadmap:
- Immediate tasks
- Short-term goals
- Long-term plans
- Technical debt to address

### session.md (ephemeral)
Current work state:
- What you're working on right now
- Temporary notes and TODOs
- Context for current session
- **Not committed to git** (in .gitignore)

### journal/
Daily work logs:
- One file per day (YYYY-MM-DD.md)
- Session summaries
- Decisions made
- Problems solved
- Things to remember

## Usage Patterns

### Daily Workflow

1. **Start working on a project:**
   ```bash
   cd /path/to/project
   # Claude Code automatically loads .claude/ context
   ```

2. **Update session.md as you work:**
   - Current task
   - Blockers
   - Questions to answer

3. **End of day - update journal:**
   - Summarize what you accomplished
   - Document decisions made
   - Note things to remember

### When Claude Code Works on Project

Claude Code automatically:
1. Loads global context from `~/.claude/.context/core/`
2. Loads project context from `.claude/`
3. Has full context about both you AND the project
4. Updates journal entries as work progresses

### Opt-Out

To exclude a project from context tracking:
```bash
echo "/path/to/project" >> ~/.claudeignore
```

## Git Integration

### What Gets Committed

**DO commit** to project repo:
- `.claude/CLAUDE.md`
- `.claude/context.md`
- `.claude/tech-stack.md`
- `.claude/rules.md`
- `.claude/next-steps.md`
- `.claude/journal/` (all journal entries)

**DON'T commit**:
- `.claude/session.md` (ephemeral, added to .gitignore)

### Sharing with Team

Project context can be shared with your team:
- They get full project documentation
- They can contribute to context files
- Journal shows project evolution
- Rules capture team learnings

**Personal context stays private** in `~/.claude/.context/` (separate private repo).

## Examples

### Onboard Elle Bot

```bash
cd /home/ja/projects/project-context-manager
python3 onboard.py /home/ja/projects/bots/elle_bot

# Follow prompts to describe the project
# Result: elle_bot/.claude/ directory created
```

### Onboard Multiple Projects

```bash
# Onboard all projects in a directory
for dir in /home/ja/projects/bots/*/; do
    python3 onboard.py "$dir"
done
```

### Update Existing Project Context

Just edit the files directly:
```bash
cd /home/ja/projects/your-project
nano .claude/context.md  # Update architecture docs
nano .claude/rules.md    # Add new rule learned today
```

Claude Code automatically loads updated files on next session.

## Maintenance

### Keep Context Fresh

- **Update as you learn** - Don't wait until you "finish"
- **Document decisions** - Capture the "why" not just the "what"
- **Add rules immediately** - When something goes wrong, add a rule
- **Archive completed tasks** - Keep next-steps.md relevant

### Journal Best Practices

- **One entry per day minimum** if you worked on the project
- **Include session time** (morning, afternoon, evening)
- **Document what changed** - code, decisions, learnings
- **Note blockers** - What stopped you? How resolved?
- **Link to commits** - Reference git commits for context

## Integration with Claude Code

This tool is designed to work seamlessly with Claude Code CLI:

1. **Automatic loading** - Claude Code detects `.claude/` and loads it
2. **Personal assistant mode** - Uses output style from `~/.claude/.context/`
3. **Two-tier context** - Both global and project context available
4. **Auto-journaling** - Claude can update journals as it works

## Project Structure

```
project-context-manager/
├── README.md                  # This file
├── onboard.py                 # Main onboarding script
├── PROJECT-CONTEXT-TEMPLATE.md # Template for new projects
├── CLAUDE.md                  # Quick reference for this project
└── .claude/                   # This project's own context
    ├── CLAUDE.md
    ├── context.md
    └── journal/
```

## Journal Auto-Summary (NEW)

When you end a Claude Code session, the journal can now **automatically summarize what was accomplished** — not just log session metadata.

### What It Captures

- **Files created** - New files you wrote
- **Files modified** - Existing files you edited
- **Significant commands** - git commits, deploys, test runs, etc.
- **Session topics** - When no file changes, captures what you discussed

### Example Journal Entry

Before (metadata only):
```markdown
## 14:30 - Session [elle_bot]
- Session ID: c30e55e4
- Working directory: /home/ja/projects/bots/elle_bot
```

After (with auto-summary):
```markdown
## 14:30 - Session [elle_bot]
- Session ID: c30e55e4
- Working directory: /home/ja/projects/bots/elle_bot

### Changes
- Created `telegram-reply.sh`
- Created `process-actions.py`
- Modified `elle_bot.py`
- Modified `settings.local.json`
- Restarted service
```

### Setup

1. **Install the hooks:**
   ```bash
   cd /home/ja/projects/project-context-manager
   ./install-hooks.sh
   ```

2. **Enable in Claude Code settings** (`~/.claude/settings.json`):
   ```json
   "hooks": {
     "Stop": [{
       "hooks": [{
         "type": "command",
         "command": "~/.local/bin/claude-session-end 2>/dev/null || true"
       }]
     }]
   }
   ```

### How It Works

1. Claude Code fires `Stop` hook after each session
2. Hook receives transcript path in JSON payload
3. `journal-summarize` parses the JSONL transcript
4. Extracts tool calls (Write, Edit, Bash) and summarizes
5. Appends meaningful summary to daily journal

### Files

- `scripts/journal-summarize` - Python script that parses transcripts
- `scripts/claude-session-end` - Bash hook that writes journal entries
- `install-hooks.sh` - Installer for the hook scripts

---

## Requirements

- Python 3.8+
- Git (optional, for auto-commit features)
- Claude Code CLI (for using the contexts)
- `jq` (for parsing JSON in hooks)

## License

Personal use by Jerry. Not for distribution.

---

**Questions?** This tool is itself managed as a project with its own `.claude/` context!
