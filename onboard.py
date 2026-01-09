#!/usr/bin/env python3
"""
Project Context Manager - Onboarding Script

Onboards projects into Elle's two-tier context system by creating
standardized .claude/ directory structure with documentation and journals.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

def ask(prompt: str, default: str = "") -> str:
    """Ask user for input with optional default"""
    if default:
        response = input(f"{prompt} [{default}]: ").strip()
        return response if response else default
    return input(f"{prompt}: ").strip()

def ask_multiline(prompt: str) -> str:
    """Ask for multiline input (end with empty line)"""
    print(f"{prompt}")
    print("(Press Enter twice to finish)")
    lines = []
    while True:
        line = input()
        if not line and lines:  # Empty line and we have content
            break
        if line:  # Only add non-empty lines
            lines.append(line)
    return '\n'.join(lines)

def create_directory_structure(project_path: Path, skip_existing: bool = False) -> bool:
    """Create .claude directory structure"""
    claude_dir = project_path / '.claude'
    journal_dir = claude_dir / 'journal'

    # Create directories
    claude_dir.mkdir(exist_ok=True)
    journal_dir.mkdir(exist_ok=True)

    print(f"✅ Created directory structure in {claude_dir}")
    return True

def create_claude_md(project_path: Path, project_info: dict, skip_existing: bool = False) -> None:
    """Create CLAUDE.md quick reference file"""
    file_path = project_path / '.claude' / 'CLAUDE.md'

    if file_path.exists() and skip_existing:
        print(f"⏭️  Skipping {file_path} (already exists)")
        return

    content = f"""# {project_info['name']}

## Purpose

{project_info['purpose']}

## Quick Start

```bash
cd {project_path}
# Add your quick start commands here
```

## Key Locations

- **Main entry point**: (add main file)
- **Configuration**: (add config files)
- **Documentation**: README.md, .claude/context.md
- **Project context**: `.claude/` (context, rules, tech stack, journal)

## Important Notes

### Current Status
{project_info['status']}

### Key Integrations
{project_info['integrations'] if project_info['integrations'] else 'None yet'}

## Development Workflow

```bash
# Common commands
```

## Team Integration

(Add team-specific notes if applicable)

## Current Limitations

(Document known issues or limitations)
"""

    file_path.write_text(content)
    print(f"✅ Created {file_path}")

def create_context_md(project_path: Path, project_info: dict, skip_existing: bool = False) -> None:
    """Create context.md comprehensive documentation"""
    file_path = project_path / '.claude' / 'context.md'

    if file_path.exists() and skip_existing:
        print(f"⏭️  Skipping {file_path} (already exists)")
        return

    content = f"""# {project_info['name']} - Project Context

## Architecture Overview

{project_info['architecture']}

## Design Decisions

### Why This Approach?

(Document key architectural decisions and reasoning)

## Code Structure

(Describe how the codebase is organized)

## Data Flow

(Explain how data moves through the system)

## External Dependencies

{project_info['integrations'] if project_info['integrations'] else 'None documented yet'}

## Configuration

### Environment Variables

(List required environment variables)

### Settings Files

(List configuration files and their purpose)

## Integration Details

(Detailed integration documentation)

## Deployment

### Environment

{project_info['environment']}

### Deployment Process

(Document deployment steps)

## Testing Strategy

(Document testing approach)

## Monitoring & Logging

(Document monitoring and logging setup)

## Security Considerations

(Document security-related decisions)

## Performance Considerations

(Document performance optimizations and constraints)

## Known Issues & Limitations

{project_info['gotchas'] if project_info['gotchas'] else 'None documented yet'}
"""

    file_path.write_text(content)
    print(f"✅ Created {file_path}")

def create_tech_stack_md(project_path: Path, project_info: dict, skip_existing: bool = False) -> None:
    """Create tech-stack.md file"""
    file_path = project_path / '.claude' / 'tech-stack.md'

    if file_path.exists() and skip_existing:
        print(f"⏭️  Skipping {file_path} (already exists)")
        return

    content = f"""# {project_info['name']} - Tech Stack

## Languages & Versions

{project_info['tech_stack']}

## Frameworks & Libraries

(List major frameworks and libraries)

## Development Tools

(List development tools: linters, formatters, test runners)

## External Services

(List external services: APIs, databases, cloud services)

## Infrastructure

### Hosting

(Where does this run?)

### Database

(Database system and schema notes)

### Caching

(Caching strategy if applicable)

### Message Queues

(Message queue system if applicable)

## Development Environment Setup

### Prerequisites

(List what needs to be installed)

### Installation Steps

```bash
# Installation commands
```

### Configuration

(Configuration steps for development)

## Production Environment

### Requirements

(Production requirements)

### Deployment Target

{project_info['environment']}

## Third-Party Dependencies

(List major third-party dependencies with versions)

## Version Compatibility

(Document version requirements and compatibility notes)
"""

    file_path.write_text(content)
    print(f"✅ Created {file_path}")

def create_rules_md(project_path: Path, project_info: dict, skip_existing: bool = False) -> None:
    """Create rules.md file"""
    file_path = project_path / '.claude' / 'rules.md'

    if file_path.exists() and skip_existing:
        print(f"⏭️  Skipping {file_path} (already exists)")
        return

    gotchas_section = ""
    if project_info['gotchas']:
        gotchas_section = f"""

## Known Gotchas

{project_info['gotchas']}
"""

    content = f"""---
name: Project Rules
description: {project_info['name']} specific rules learned from corrections and best practices
---

## Development Rules

### Code Changes
- ✅ ALWAYS (add your rule)
- ❌ NEVER (add your rule)

### Testing
- ✅ ALWAYS test changes before deploying
- ✅ ALWAYS (add your rule)

### Deployment
- ✅ ALWAYS (add your rule)
- ❌ NEVER (add your rule)

## Architecture Rules

(Add architecture-specific rules)

## Security Rules

(Add security-related rules)

## Performance Rules

(Add performance-related rules)
{gotchas_section}

## Communication Rules

(Add rules about communication, documentation, etc.)

## Future-Proofing Rules

(Add rules that help maintain flexibility for future changes)
"""

    file_path.write_text(content)
    print(f"✅ Created {file_path}")

def create_next_steps_md(project_path: Path, project_info: dict, skip_existing: bool = False) -> None:
    """Create next-steps.md file"""
    file_path = project_path / '.claude' / 'next-steps.md'

    if file_path.exists() and skip_existing:
        print(f"⏭️  Skipping {file_path} (already exists)")
        return

    content = f"""# {project_info['name']} - Next Steps

## Priority 1: Immediate Tasks

(Add high-priority tasks that need attention now)

## Priority 2: Short-term Goals

(Add tasks for the next week or two)

## Priority 3: Medium-term Goals

(Add tasks for the next month)

## Future: Long-term Plans

(Add longer-term vision and goals)

## Technical Debt

(Track technical debt that should be addressed)

## Ideas & Explorations

(Track ideas to explore but not committed to yet)
"""

    file_path.write_text(content)
    print(f"✅ Created {file_path}")

def create_session_md(project_path: Path, project_info: dict, skip_existing: bool = False) -> None:
    """Create session.md ephemeral file"""
    file_path = project_path / '.claude' / 'session.md'

    if file_path.exists() and skip_existing:
        print(f"⏭️  Skipping {file_path} (already exists)")
        return

    content = f"""# Current Session

**Started**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## What I'm Working On

(Current task or focus)

## Context

(Relevant context for this session)

## Blockers

(Any blockers or questions)

## TODOs

- [ ] (Add task)

## Notes

(Temporary notes for this session)

---

*This file is ephemeral and not committed to git*
"""

    file_path.write_text(content)
    print(f"✅ Created {file_path}")

def create_journal_readme(project_path: Path, skip_existing: bool = False) -> None:
    """Create journal README"""
    file_path = project_path / '.claude' / 'journal' / 'README.md'

    if file_path.exists() and skip_existing:
        print(f"⏭️  Skipping {file_path} (already exists)")
        return

    content = """# Project Journal

Daily work logs tracking development progress, decisions, and learnings.

## Format

Each day gets its own file: `YYYY-MM-DD.md`

### Structure

```markdown
---
date: YYYY-MM-DD
day: Monday
---

# Work Log: YYYY-MM-DD

## Sessions

### Session 1 (morning/afternoon/evening)
**Time**: ~10am-12pm
**Focus**: What you worked on

**Accomplished**:
- Thing 1
- Thing 2

**Technical Details**:
- Implementation notes
- Code changes

**Decisions Made**:
- Decision and reasoning

**Issues Encountered**:
- Problem and solution

**For Next Time**:
- Things to remember
- Follow-up needed
```

## Best Practices

- **One entry per day minimum** if you worked on the project
- **Multiple sessions per day** is fine (morning, afternoon, evening)
- **Include context** - what led to decisions
- **Document gotchas** - things that weren't obvious
- **Link to commits** - reference git commits for traceability
- **Update as you work** - don't wait until end of day

## Purpose

The journal serves as:
- **Memory** - Remember what you did and why
- **Handoff** - Share context with future you or team
- **Learning** - Track patterns and improvements
- **Accountability** - See progress over time
"""

    file_path.write_text(content)
    print(f"✅ Created {file_path}")

def update_gitignore(project_path: Path) -> None:
    """Add session.md to .gitignore"""
    gitignore_path = project_path / '.gitignore'

    # Read existing gitignore
    existing_lines = []
    if gitignore_path.exists():
        existing_lines = gitignore_path.read_text().splitlines()

    # Check if already has our entries
    session_entry = '.claude/session.md'
    if session_entry in existing_lines:
        print(f"⏭️  .gitignore already configured")
        return

    # Add our entries
    if existing_lines and not existing_lines[-1].strip():
        # Already has trailing newline
        pass
    elif existing_lines:
        existing_lines.append('')  # Add blank line before our section

    existing_lines.extend([
        '# Claude Code project context (ephemeral files)',
        '.claude/session.md'
    ])

    gitignore_path.write_text('\n'.join(existing_lines) + '\n')
    print(f"✅ Updated .gitignore to exclude session.md")

def collect_project_info(project_path: Path) -> dict:
    """Collect information about the project"""
    print("\n" + "="*70)
    print("PROJECT ONBOARDING - Answer questions about this project")
    print("="*70 + "\n")

    # Get project name from directory
    default_name = project_path.name

    info = {
        'name': ask("Project name", default_name),
        'purpose': ask_multiline("What does this project do? What problem does it solve?"),
        'status': ask("Current status (e.g., 'In development', 'Deployed', 'Planned')", "In development"),
        'tech_stack': ask_multiline("Tech stack (languages, frameworks, libraries)?"),
        'architecture': ask_multiline("Architecture overview (how is it structured)?"),
        'integrations': ask_multiline("External integrations (APIs, databases, services)? [Enter to skip]"),
        'environment': ask("Where does it run? (e.g., 'Ubuntu 22.04 server', 'Local dev only')", "Local development"),
        'gotchas': ask_multiline("Any important gotchas or quirks to remember? [Enter to skip]"),
    }

    return info

def onboard_project(project_path: Path, skip_existing: bool = False) -> bool:
    """Main onboarding function"""

    # Validate project path
    if not project_path.exists():
        print(f"❌ Error: Project path does not exist: {project_path}")
        return False

    if not project_path.is_dir():
        print(f"❌ Error: Path is not a directory: {project_path}")
        return False

    print(f"\n🚀 Onboarding project: {project_path}")
    print(f"   Skip existing files: {skip_existing}\n")

    # Check if already onboarded
    claude_dir = project_path / '.claude'
    if claude_dir.exists() and not skip_existing:
        response = ask(f".claude/ directory already exists. Overwrite? (y/n)", "n")
        if response.lower() != 'y':
            print("❌ Onboarding cancelled")
            return False

    # Collect project information
    project_info = collect_project_info(project_path)

    print("\n" + "="*70)
    print("CREATING PROJECT CONTEXT")
    print("="*70 + "\n")

    # Create structure
    create_directory_structure(project_path, skip_existing)

    # Create files
    create_claude_md(project_path, project_info, skip_existing)
    create_context_md(project_path, project_info, skip_existing)
    create_tech_stack_md(project_path, project_info, skip_existing)
    create_rules_md(project_path, project_info, skip_existing)
    create_next_steps_md(project_path, project_info, skip_existing)
    create_session_md(project_path, project_info, skip_existing)
    create_journal_readme(project_path, skip_existing)

    # Update .gitignore
    update_gitignore(project_path)

    print("\n" + "="*70)
    print("✅ PROJECT ONBOARDING COMPLETE!")
    print("="*70)
    print(f"\nNext steps:")
    print(f"1. Review and edit files in {claude_dir}")
    print(f"2. Start working: Claude Code will automatically load this context")
    print(f"3. Update journal as you work: {claude_dir / 'journal'}")
    print(f"4. Keep context fresh: update files as you learn\n")

    return True

def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Onboard a project into Elle\'s two-tier context system',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/project
  %(prog)s /path/to/project --skip-existing
  %(prog)s  # Interactive mode - will prompt for path
        """
    )
    parser.add_argument('project_path', nargs='?', help='Path to project directory')
    parser.add_argument('--skip-existing', action='store_true',
                        help='Skip files that already exist (don\'t overwrite)')

    args = parser.parse_args()

    # Get project path
    if args.project_path:
        project_path = Path(args.project_path).resolve()
    else:
        # Interactive mode
        path_str = ask("Enter project path")
        if not path_str:
            print("❌ No path provided")
            return 1
        project_path = Path(path_str).resolve()

    # Onboard
    success = onboard_project(project_path, args.skip_existing)
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())
