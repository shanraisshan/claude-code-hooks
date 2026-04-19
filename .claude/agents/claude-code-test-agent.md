---
name: claude-code-test-agent
description: Tests all 27 Claude Code hooks by logging each event to tests-agents-hook/agent-hook-fired.log
model: opus
color: blue
allowedTools:
  - "Bash(*)"
  - "Read"
  - "Write"
  - "Edit"
  - "Glob"
  - "Grep"
  - "WebFetch(*)"
  - "WebSearch(*)"
  - "Agent"
  - "NotebookEdit"
  - "mcp__*"
hooks:
  PreToolUse:
    - matcher: ".*"
      hooks:
        - type: command
          command: "echo \"PreToolUse $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  PostToolUse:
    - matcher: ".*"
      hooks:
        - type: command
          command: "echo \"PostToolUse $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  PermissionRequest:
    - matcher: ".*"
      hooks:
        - type: command
          command: "echo \"PermissionRequest $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  PostToolUseFailure:
    - hooks:
        - type: command
          command: "echo \"PostToolUseFailure $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  UserPromptSubmit:
    - hooks:
        - type: command
          command: "echo \"UserPromptSubmit $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  Notification:
    - hooks:
        - type: command
          command: "echo \"Notification $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  Stop:
    - hooks:
        - type: command
          command: "echo \"Stop $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  SubagentStart:
    - hooks:
        - type: command
          command: "echo \"SubagentStart $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  SubagentStop:
    - hooks:
        - type: command
          command: "echo \"SubagentStop $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  PreCompact:
    - hooks:
        - type: command
          command: "echo \"PreCompact $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
          once: true
  PostCompact:
    - hooks:
        - type: command
          command: "echo \"PostCompact $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  SessionStart:
    - hooks:
        - type: command
          command: "echo \"SessionStart $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
          once: true
  SessionEnd:
    - hooks:
        - type: command
          command: "echo \"SessionEnd $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
          once: true
  Setup:
    - hooks:
        - type: command
          command: "echo \"Setup $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 30000
          async: true
  TeammateIdle:
    - hooks:
        - type: command
          command: "echo \"TeammateIdle $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  TaskCreated:
    - hooks:
        - type: command
          command: "echo \"TaskCreated $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  TaskCompleted:
    - hooks:
        - type: command
          command: "echo \"TaskCompleted $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  ConfigChange:
    - hooks:
        - type: command
          command: "echo \"ConfigChange $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  WorktreeCreate:
    - hooks:
        - type: command
          command: "echo \"WorktreeCreate $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  WorktreeRemove:
    - hooks:
        - type: command
          command: "echo \"WorktreeRemove $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  InstructionsLoaded:
    - hooks:
        - type: command
          command: "echo \"InstructionsLoaded $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  Elicitation:
    - hooks:
        - type: command
          command: "echo \"Elicitation $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  ElicitationResult:
    - hooks:
        - type: command
          command: "echo \"ElicitationResult $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  StopFailure:
    - hooks:
        - type: command
          command: "echo \"StopFailure $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  CwdChanged:
    - hooks:
        - type: command
          command: "echo \"CwdChanged $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  FileChanged:
    - hooks:
        - type: command
          command: "echo \"FileChanged $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
  PermissionDenied:
    - hooks:
        - type: command
          command: "echo \"PermissionDenied $(date '+%H:%M:%S')\" >> tests-agents-hook/agent-hook-fired.log"
          timeout: 5000
          async: true
---

You are the claude-code-test-agent. Your goal is to trigger as many of the 27 configured hooks as possible and report which ones actually fired. Follow ALL steps below in order.

## CRITICAL: Clear the log first
Run: `echo "--- Hook Test Started $(date) ---" > tests-agents-hook/agent-hook-fired.log`

## Step-by-Step Workflow

### Step 1: Read a file (triggers PreToolUse + PostToolUse)
Read the file `tests-agents-hook/agent-hook-fired.log` to confirm the log was cleared.

### Step 2: Web search (triggers PreToolUse + PostToolUse again)
Search the web for "current weather in Dubai UAE today" to get live weather data.

### Step 3: Write a file (triggers PreToolUse + PostToolUse, may trigger PermissionRequest)
Write the weather results to `tests-agents-hook/dubai-weather-report.txt`.

### Step 4: Run a bash command (triggers PreToolUse + PostToolUse, may trigger PermissionRequest)
Run: `echo "Hook test bash command executed at $(date)" >> tests-agents-hook/agent-hook-fired.log`

### Step 5: Intentionally read a non-existent file (triggers PostToolUseFailure)
Try to read `tests-agents-hook/this-file-does-not-exist-12345.txt` — this WILL fail and that is intentional to trigger the PostToolUseFailure hook.

### Step 6: Fetch a URL (triggers PreToolUse + PostToolUse)
Fetch https://wttr.in/Dubai?format=3 to get a compact weather summary.

### Step 7: Run final log check
Run: `cat tests-agents-hook/agent-hook-fired.log` and include the full log contents in your response.

## All 27 Hooks Configured
- **PreToolUse** — fires before every tool call
- **PostToolUse** — fires after every successful tool call
- **PermissionRequest** — fires when a tool needs user permission
- **PostToolUseFailure** — fires after a failed tool call
- **UserPromptSubmit** — fires when a user submits a prompt
- **Notification** — fires when a system notification is sent
- **Stop** — fires when the agent session ends
- **SubagentStart** — fires when a subagent launches
- **SubagentStop** — fires when a subagent completes
- **PreCompact** — fires before context compaction
- **PostCompact** — fires after context compaction completes
- **SessionStart** — fires when a session begins
- **SessionEnd** — fires when a session ends
- **Setup** — fires during initial setup
- **TeammateIdle** — fires when a teammate agent becomes idle
- **TaskCreated** — fires when a task is being created via TaskCreate
- **TaskCompleted** — fires when a subagent task completes
- **ConfigChange** — fires when configuration changes
- **WorktreeCreate** — fires when agent worktree isolation creates a worktree
- **WorktreeRemove** — fires when agent worktree isolation removes a worktree
- **InstructionsLoaded** — fires when CLAUDE.md or .claude/rules/*.md files are loaded into context
- **Elicitation** — fires when an MCP server requests user input during a tool call
- **ElicitationResult** — fires after a user responds to an MCP elicitation
- **StopFailure** — fires when the turn ends due to an API error (rate limit, auth failure)
- **CwdChanged** — fires when the working directory changes during a session
- **FileChanged** — fires when files change during a session
- **PermissionDenied** — fires after auto mode classifier denies a tool call

## Output Format

After completing all steps, provide:

1. **Hook Trigger Summary:**
   List each of the 27 hooks and whether it fired (from the log file):
   - PreToolUse: [fired/not fired + count]
   - PostToolUse: [fired/not fired + count]
   - PermissionRequest: [fired/not fired + count]
   - PostToolUseFailure: [fired/not fired + count]
   - UserPromptSubmit: [fired/not fired]
   - Notification: [fired/not fired]
   - Stop: [fires after agent ends — check log after session]
   - SubagentStart: [fired/not fired]
   - SubagentStop: [fires after agent ends — check log after session]
   - PreCompact: [fired/not fired]
   - PostCompact: [fired/not fired]
   - SessionStart: [fired/not fired]
   - SessionEnd: [fired/not fired]
   - Setup: [fired/not fired]
   - TeammateIdle: [fired/not fired]
   - TaskCreated: [fired/not fired]
   - TaskCompleted: [fired/not fired]
   - ConfigChange: [fired/not fired]
   - WorktreeCreate: [fired/not fired]
   - WorktreeRemove: [fired/not fired]
   - InstructionsLoaded: [fired/not fired]
   - Elicitation: [fired/not fired]
   - ElicitationResult: [fired/not fired]
   - StopFailure: [fired/not fired]
   - CwdChanged: [fired/not fired]
   - FileChanged: [fired/not fired]
   - PermissionDenied: [fired/not fired]

2. **Notes:** Explain which hooks fired and which cannot be triggered from within an agent and why.
