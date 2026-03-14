# Claude Code Voice Hooks

Voice notification system for all 19 Claude Code hooks. Plays sound effects when hook events fire.

## Project Structure

```
.claude/
  settings.json              # Active hook config (schema-validated by Claude Code)
  hooks/
    scripts/hooks.py         # Main hook handler — HOOK_SOUND_MAP + AGENT_HOOK_SOUND_MAP
    config/hooks-config.json # Per-hook disable toggles (disableXxxHook pattern)
    sounds/<hookname>/       # Sound files — each hook needs .mp3 + .wav
    HOOKS-README.md          # Full hook documentation (22 hooks)
  agents/
    workflows/workflow-changelog-agent.md  # Research agent for drift detection
    claude-code-test-agent.md              # Tests all 22 hooks
  commands/workflows/
    workflow-changelog.md    # Coordinator: launches agents, merges findings, reports drift
    workflow-add-hook.md     # Adds a new hook across all 11 files
install/
  settings-mac.json          # python3 + ${CLAUDE_PROJECT_DIR}
  settings-linux.json        # python3 + ${CLAUDE_PROJECT_DIR}
  settings-windows.json      # python + relative path
presentation/index.html      # 29-slide presentation (totalSlides = 29)
changelog/
  changelog.md               # Accumulated workflow-changelog run history
  verification-checklist.md  # 82+ regression rules across 6 categories
```

## Critical: Hook Count Consistency

The hook count (currently **22**) MUST match across ALL of these locations:
- `.claude/settings.json` hook entries
- `install/settings-mac.json`, `settings-linux.json`, `settings-windows.json`
- `hooks.py` HOOK_SOUND_MAP keys + docstring count
- `hooks-config.json` toggle count
- `HOOKS-README.md` heading + numbered list
- `README.md` badge + changelog table
- `presentation/index.html` (slides 2, 3, TOC, totalSlides)
- `claude-code-test-agent.md` frontmatter + body

When adding a hook, use `/workflows:workflow-add-hook` — it updates all 11 files.

## Agent Hooks

Only **6 of 22** hooks fire in agent sessions: PreToolUse, PostToolUse, PermissionRequest, PostToolUseFailure, Stop, SubagentStop. These are mapped in `AGENT_HOOK_SOUND_MAP` in hooks.py.

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

Persistent memory file: `~/.claude/projects/-Users-shayanraees-Documents-Github-claude-code-voice-hooks/memory/MEMORY.md`

## Schema Note

`.claude/settings.json` is validated against Claude Code's bundled JSON schema. The schema's `propertyNames` enum may contain hidden/undocumented hooks not yet in the changelog. The workflow-changelog agent checks for these. As of v2.1.76, Elicitation, ElicitationResult, and PostCompact are officially documented and need to be added to the repo (pending `/workflows:workflow-add-hook`).
