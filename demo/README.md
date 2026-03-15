# Hooks Lifecycle Demo

Interactive real-time visualization of all 22 Claude Code hooks. As you use Claude Code in the demo directory, hooks light up on a flowchart diagram with sound effects.

## Quick Start

```bash
# Terminal 1 — start the visualization server
cd demo
./start-demo.sh
```

This starts a local server at `http://localhost:3456` and opens it in your browser.

```bash
# Terminal 2 — run Claude Code inside the demo directory
cd demo
claude
```

As you interact with Claude, each hook fires and lights up on the diagram in real-time.

## How It Works

```
demo/
  hooks-lifecycle.html           # Flowchart visualization (polls server for state)
  server.py                      # HTTP server — serves HTML + state API (port 3456)
  start-demo.sh                  # Convenience script — starts server + opens browser
  .claude/
    settings.json                # Hook config — all 22 hooks wired to demo-hooks.py
    hooks/
      scripts/demo-hooks.py      # Hook handler — updates state file + plays sounds
      state/hook-state.json      # Shared state — tracks which hooks have fired
  .mcp.json                      # MCP server config (elicitation)
```

**Flow:** Claude Code fires a hook → `demo-hooks.py` updates `hook-state.json` + plays a sound → the browser polls `/api/state` → the matching hook lights up on the flowchart.

## Components

### Visualization (`hooks-lifecycle.html`)

- SVG flowchart showing the full hook lifecycle
- Hooks glow gold when they fire, with pulse animation
- Fire count badges track how many times each hook has been triggered
- Event log at the bottom shows hook activity in real-time
- Resizable split panel — prompt guide on the left, flowchart on the right

### Server (`server.py`)

- `GET /` — serves the visualization page
- `GET /api/state` — returns current hook state as JSON
- `POST /api/reset` — resets all hooks to inactive

```bash
# Run with custom port
python3 server.py --port 8080
```

### Hook Handler (`demo-hooks.py`)

Receives hook events from Claude Code via stdin, then:
1. Writes the event to `hook-state.json` (atomic file write)
2. Plays the corresponding sound from the parent project's sound files

### Prompts to Try

The left panel of the visualization includes guided prompts to trigger different hooks. Some examples:

- **Basic interaction** — triggers SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop
- **Permission flow** — ask Claude to write a file to trigger PermissionRequest
- **Subagent hooks** — ask Claude to use the Agent tool for SubagentStart/SubagentStop
- **Compaction** — long conversations trigger PreCompact/PostCompact
- **Elicitation** — MCP elicitation triggers Elicitation/ElicitationResult

## Prerequisites

- Python 3
- The parent project's sound files (`.claude/hooks/sounds/`) must exist
- macOS (uses `afplay` for sound playback)

## Reset

Click the **Reset** button in the visualization header, or:

```bash
curl -X POST http://localhost:3456/api/reset
```
