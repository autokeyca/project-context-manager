# Project Context Manager - Context

## Purpose

This tool manages project context for Elle's two-tier context system. It's a meta-project: a context manager that manages its own context!

## Architecture

### Single Script Design

- **onboard.py** - Standalone Python script with no external dependencies
- Uses only Python stdlib (pathlib, datetime, argparse)
- Interactive CLI with multiline input support
- Creates standardized project structure

### Template System

- **PROJECT-CONTEXT-TEMPLATE.md** - Reference template from global context
- Script generates files programmatically based on user answers
- Consistent structure across all onboarded projects

### File Generation

Each onboarded project gets:
1. CLAUDE.md - Quick reference (function: `create_claude_md`)
2. context.md - Comprehensive docs (function: `create_context_md`)
3. tech-stack.md - Tech specs (function: `create_tech_stack_md`)
4. rules.md - Project rules (function: `create_rules_md`)
5. next-steps.md - Roadmap (function: `create_next_steps_md`)
6. session.md - Ephemeral state (function: `create_session_md`)
7. journal/README.md - Journal guide (function: `create_journal_readme`)

### Git Integration

- Updates .gitignore to exclude session.md
- Non-destructive with `--skip-existing` flag
- Compatible with existing repositories

## Design Decisions

### Why Standalone Script?

- **No dependencies** - Easy to use anywhere
- **Self-contained** - Single file deployment
- **Simple** - No build process or packaging needed

### Why Interactive Prompts?

- **Context gathering** - Ensures complete project documentation
- **Consistency** - Same questions for all projects
- **Flexibility** - Can skip optional sections

### Why Separate Files?

- **Modularity** - Each file has clear purpose
- **Git-friendly** - Easy to see what changed
- **Selective loading** - Claude can load specific files as needed
- **Team sharing** - Different files for different audiences

## Integration Points

### Global Context

- Reads template from `~/.claude/.context/PROJECT-CONTEXT-TEMPLATE.md`
- Compatible with global context system
- Maintains separation between personal and project context

### Claude Code

- Creates structure Claude Code auto-detects
- Files loaded when working on project
- Journal format matches daily journal pattern

## Known Limitations

- No validation of project paths
- Assumes Python 3.8+ available
- No batch mode (processes one project at a time)
- Manual editing required for complex customization

## Future Enhancements

- Batch onboarding mode
- Template customization
- Context validation/linting
- Auto-update journals from git commits
- Integration with project initialization (git init, etc.)
