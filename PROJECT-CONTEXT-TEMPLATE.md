# Project Context Template

This template is used to initialize project-specific context in any project directory.

## Directory Structure

```
<project-dir>/.claude/
├── CLAUDE.md              # Project overview & Elle's instructions
├── context.md             # Project context (architecture, decisions, patterns)
├── rules.md               # Project-specific rules & conventions
├── session.md             # Current working session (ephemeral)
├── tech-stack.md          # Technologies, dependencies, integrations
└── journal/
    ├── README.md          # Journal format guide
    └── YYYY-MM-DD.md     # Daily work logs
```

## File Templates

### CLAUDE.md
```markdown
---
project_name: [PROJECT NAME]
purpose: [One-line description]
status: [active | maintenance | deprecated]
created: YYYY-MM-DD
---

# [PROJECT NAME]

## Purpose
[What problem does this solve? What's the goal?]

## Quick Start
[How to get started working on this project]

## Key Locations
- Main entry point:
- Configuration:
- Tests:
- Documentation:

## Important Notes
[Anything Elle should know before working on this project]
```

### context.md
```markdown
---
name: Project Context
description: Architecture, decisions, and patterns for this project
---

## Architecture Overview
[High-level structure - how is this organized?]

## Key Decisions
[Important architectural/technical decisions made]

## Patterns & Conventions
[Coding patterns, naming conventions, organization principles]

## Data Model
[If applicable - database schema, key entities]

## Integration Points
[External systems, APIs, services this connects to]

## Known Issues & Gotchas
[Things to watch out for, common pitfalls, quirks]
```

### rules.md
```markdown
---
name: Project Rules
description: Project-specific rules learned from corrections and best practices
---

## Coding Standards
[Language-specific conventions, style guides]

## Testing Requirements
[When to write tests, what to test, how to run them]

## Deployment Rules
[How/when to deploy, what to check first]

## Do Not
[Things to never do in this project]
```

### tech-stack.md
```markdown
---
name: Tech Stack
description: Technologies, dependencies, and integrations
---

## Languages & Frameworks
- **Language**:
- **Framework**:
- **Version**:

## Dependencies
### Core
[Main dependencies this project relies on]

### Development
[Dev-only dependencies]

## External Services
[APIs, databases, cloud services, etc.]

## Environment
- **Runtime**:
- **Deployment**:
- **Hosting**:

## Configuration
[Environment variables, config files, secrets management]
```

### session.md
```markdown
---
name: Session Context
description: Current working session for this project
---

## Current Focus
[What we're working on right now]

## Active Tasks
[Tasks in progress]

## Decisions Pending
[Choices that need to be made]

## Blockers
[What's preventing progress]

## Quick Wins Available
[Small tasks that could be done quickly]

## Notes for Next Session
[Context to carry forward]
```

### journal/README.md
```markdown
# Project Journal

Daily work logs for this project.

## Format
Each day gets its own file: `YYYY-MM-DD.md`

## What to Capture
- Work sessions (what was accomplished)
- Technical decisions made
- Bugs fixed and how
- Features implemented
- Architectural changes
- Lessons learned
- Performance improvements
- Refactorings

## Template
\`\`\`markdown
---
date: YYYY-MM-DD
day: [DayOfWeek]
---

# Work Log: YYYY-MM-DD

## Sessions

### Session 1
**Time**: [time range]
**Focus**: [what we worked on]

**Accomplished**:
- [key accomplishments]

**Technical Details**:
- [important implementation notes]

**Decisions Made**:
- [architectural or technical decisions]

**Issues Encountered**:
- [problems and how they were solved]

**Next Steps**:
- [what to work on next]
\`\`\`
```

## Onboarding Process

When initializing a new project, ask these questions:

1. **What is this project?** (name, one-line purpose)
2. **What problem does it solve?**
3. **What's the tech stack?** (languages, frameworks, main tools)
4. **How is it architected?** (high-level structure)
5. **What does it integrate with?** (databases, APIs, services)
6. **Where does it run?** (environment, deployment)
7. **What's the current status?** (active dev, production, etc.)
8. **Any gotchas or things to watch out for?**

Capture answers in the appropriate files, keeping it concise.

## Git Integration

**Add to project's `.gitignore`:**
```
# Ephemeral Elle session state
.claude/session.md
```

**Commit to git:**
```
.claude/CLAUDE.md
.claude/context.md
.claude/rules.md
.claude/tech-stack.md
.claude/journal/
```

This way project context is shared with the team!
