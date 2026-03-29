# Claude Code Hooks

Sound notification system for all 26 Claude Code hooks. Plays sound effects when hook events fire.

## Project Structure

```
.claude/
  settings.json
  hooks/
    scripts/hooks.py
    config/hooks-config.json
    sounds/<hookname>/
    HOOKS-README.md
  agents/
    workflows/workflow-changelog-agent.md
    claude-code-test-agent.md
  commands/workflows/
    workflow-changelog.md
    workflow-add-hook.md
install/
  settings-mac.json
  settings-linux.json
  settings-windows.json
presentation/index.html
changelog/
  changelog.md
  verification-checklist.md
```

## Critical: Hook Count Consistency

The hook count (currently **26**) MUST match across ALL of these locations:
- `.claude/settings.json` hook entries
- `install/settings-mac.json`, `settings-linux.json`, `settings-windows.json`
- `hooks.py` HOOK_SOUND_MAP keys + docstring count
- `hooks-config.json` toggle count
- `HOOKS-README.md` heading + numbered list
- `README.md` badge + changelog table
- `presentation/index.html` (slides 2, 3, TOC, totalSlides)
- `claude-code-test-agent.md` frontmatter + body
- `demo/.claude/settings.json` hook entries
- `demo/.claude/hooks/scripts/demo-hooks.py` HOOK_SOUND_MAP + docstring
- `demo/hooks-lifecycle.html` flowchart SVG + prompt cards + branding count

When adding a hook, use `/workflows:workflow-add-hook` — it updates all 14 files.

## Agent Hooks

Only **6 of 26** hooks fire in agent sessions: PreToolUse, PostToolUse, PermissionRequest, PostToolUseFailure, Stop, SubagentStop. These are mapped in `AGENT_HOOK_SOUND_MAP` in hooks.py.

## Workflows

- `/workflows:workflow-changelog [N]` — Check last N versions for drift. Launches 2 agents in parallel, runs verification checklist, appends to changelog.md
- `/workflows:workflow-add-hook <HookName>` — Add a new hook across all files (sounds, config, settings, scripts, docs, presentation)
- `/commit` — Auto-generate commit message with timestamp and change count

## Conventions

- Hook names are **PascalCase** everywhere (e.g. `PreToolUse`, `InstructionsLoaded`)
- Sound folder names are **lowercase** (e.g. `pretooluse`, `instructionsloaded`)
- Settings files: timeout 5000 for all hooks except Setup (30000)
- `once: true` only on: PreCompact, SessionStart, SessionEnd
- `async: true` on all hooks
- Changelog entries use PKT timezone: `TZ=Asia/Karachi date`
- Version badge format: `v2.X.X | Mon DD, YYYY HH:MM AM/PM PKT`

## Memory

Persistent memory file: `~/.claude/projects/-Users-shayanraees-Documents-Github-claude-code-hooks/memory/MEMORY.md`

## Schema Note

`.claude/settings.json` is validated against Claude Code's bundled JSON schema. The schema's `propertyNames` enum may contain hidden/undocumented hooks not yet in the changelog. The workflow-changelog agent checks for these. As of v2.1.87, the schema has 26 hooks (all implemented in repo).
