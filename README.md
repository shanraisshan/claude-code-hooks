# Claude Code Hooks
[![Hooks](https://img.shields.io/badge/supports%20all-26%20hooks-white?style=flat&labelColor=555)](https://github.com/shanraisshan/claude-code-hooks/blob/main/.claude/hooks/HOOKS-README.md#hook-events-overview---official-26-hooks) [![Version](https://img.shields.io/badge/updated%20with%20Claude%20Code-v2.1.87%20(Mar%2029%2C%202026%207:47%20PM%20PKT)-white?style=flat&labelColor=555)](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) [![Stars](https://img.shields.io/github/stars/shanraisshan/claude-code-hooks?style=flat&label=%E2%98%85&labelColor=555&color=white)](https://github.com/shanraisshan/claude-code-hooks)

<p align="center">
  <img src="!/claude-speaking.svg" alt="Claude Code mascot speaking" width="168" height="108">
</p>

<p align="center">
  <img src="!/repo-description.svg" alt="Mouse click on PreToolUse, Keyboard on PostToolUse, Human voice on other hooks" height="56">
</p>

# [Demo Video + Presentation](https://youtu.be/6_y3AtkgjqA)

<p>
  <a href="https://youtu.be/6_y3AtkgjqA"><img src="!/pill-youtube-red.svg" alt="YouTube" height="36"></a>&nbsp;
  <a href="presentation/index.html"><img src="!/pill-slides.svg" alt="Slides" height="36"></a>
</p>

[![thumbnail](!/thumbnail/thumbnail3.jpg)](https://youtu.be/6_y3AtkgjqA)

## Installation

<p>
  <a href="install/README-mac.md"><img src="!/pill-mac.svg" alt="Mac" height="36"></a>&nbsp;
  <a href="install/README-linux.md"><img src="!/pill-linux.svg" alt="Linux" height="36"></a>&nbsp;
  <a href="install/README-windows.md"><img src="!/pill-windows.svg" alt="Windows" height="36"></a>
</p>

![How to Use](!/how-to-use.svg)

**Step 1.** Start Claude Code:
```bash
claude
```

**Step 2.** Send a prompt (e.g., `Hi`) — you'll hear a sound on session start, tool use, agent response, and more.

## Common Errors

If you don't follow the prerequisites, you will see the following error on claude code start

```
SessionStart:startup hook error
```

## Changelog
new hook addition changelogs only

| Date | Hooks | Changes | Claude Code Version | Demo |
|------|:-----:|---------|:-------------------:|:----:|
| Mar 26, 2026 | 26 | Added `TaskCreated` | [v2.1.84](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2184) | [Demo 4](https://www.youtube.com/watch?v=O8PVI6JsfFc) |
| Mar 25, 2026 | 25 | Added `CwdChanged`, `FileChanged` | [v2.1.83](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2183) | |
| Mar 18, 2026 | 23 | Added `StopFailure` | [v2.1.78](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2178) | |
| Mar 14, 2026 | 22 | Added `PostCompact`, `Elicitation`, `ElicitationResult` | [v2.1.76](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2176) | |
| Mar 5, 2026 | 19 | Added `InstructionsLoaded` | [v2.1.69](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2169) | |
| Feb 21, 2026 | 18 | Added `WorktreeCreate` and `WorktreeRemove` | [v2.1.50](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2150) | |
| Feb 20, 2026 | 16 | Added `ConfigChange` | [v2.1.49](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2149) | |
| Feb 6, 2026 | 15 | Added `TeammateIdle` and `TaskCompleted` | [v2.1.33](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2133) | |
| — | 13 | Added `PostToolUseFailure` | — | [Demo 3](https://youtu.be/6_y3AtkgjqA) |
| Jan 17, 2026 | 12 | Added `Setup` | [v2.1.10](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2110) | |
| Jan 7, 2026 | 12 | Added subagent hooks: `PreToolUse`, `PostToolUse`, `Stop` | [v2.1.0](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#210) | |
| Nov 18, 2025 | 11 | Added `PermissionRequest` | [v2.0.45](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2045) | [Demo 2](https://youtu.be/JFPJtMNV8Qw) |
| Nov 17, 2025 | 10 | Added `SubagentStart` | [v2.0.43](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2043) | |
| Nov 10, 2025 | 9 | Added `Notification` | [v2.0.37](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2037) | [Demo 1](https://youtu.be/vgfdSUbz_b0) |
| Jul 28, 2025 | 8 | Added `SessionStart` | [v1.0.62](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1062) | |
| Jul 16, 2025 | 7 | Added `UserPromptSubmit` | [v1.0.54](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1054) | |
| Jul 10, 2025 | 6 | Added `PreCompact` | [v1.0.48](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1048) | |
| Jul 2, 2025 | 5 | Split `Stop` into `Stop` and `SubagentStop` | [v1.0.41](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1041) | |
| Jun 30, 2025 | 4 | Initial release: `PreToolUse`, `PostToolUse`, `Stop`, `SessionEnd` | [v1.0.38](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1038) | |

### [Not in Official Docs](.claude/hooks/HOOKS-README.md#not-in-official-docs)

## Links

<p>
  <a href="https://www.youtube.com/watch?v=vgfdSUbz_b0"><img src="!/pill-youtube.svg" alt="YouTube" height="36"></a>&nbsp;
  <a href="https://www.linkedin.com/posts/shanraisshan_claudecode-aicoding-voicehooks-activity-7393305703697805312-4gl0"><img src="!/pill-linkedin.svg" alt="LinkedIn" height="36"></a>&nbsp;
  <a href="https://www.reddit.com/r/ClaudeCode/comments/1otaf7f/i_just_made_claude_code_speak_using_hooks/"><img src="!/pill-reddit.svg" alt="Reddit" height="36"></a>&nbsp;
  <a href="https://x.com/shanraisshan/status/1987817251966513620"><img src="!/pill-x.svg" alt="X" height="36"></a>&nbsp;
  <a href="https://medium.com/@shanraisshan/claude-code-just-got-a-voice-%25EF%25B8%258F-51008157305b"><img src="!/pill-medium.svg" alt="Medium" height="36"></a>
</p>

## Other Repos

<a href="https://github.com/shanraisshan/codex-cli-hooks"><img src="!/codex-speaking.svg" alt="Codex CLI Hooks" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/codex-cli-hooks"><strong>codex-cli-hooks</strong></a> · <a href="https://github.com/shanraisshan/claude-code-best-practice"><img src="!/claude-jumping.svg" alt="Claude Code Best Practice" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/claude-code-best-practice"><strong>claude-code-best-practice</strong></a> · <a href="https://github.com/shanraisshan/codex-cli-best-practice"><img src="!/codex-jumping.svg" alt="Codex CLI Best Practice" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/codex-cli-best-practice"><strong>codex-cli-best-practice</strong></a>

## Developed by

[![Developed by Claude Code](!/developed-by-claude-code.svg)](https://docs.anthropic.com/en/docs/claude-code)

| Workflow | Description |
|---------|-------------|
| /workflows:workflow-changelog | Scan for new hooks and drift across all files |
| /workflows:workflow-add-hook <HookName>* | Add any recommended hook across all files in one command |

