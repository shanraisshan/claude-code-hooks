# Workflow Changelog History

## Status Legend

| Status | Meaning |
|--------|---------|
| ✅ COMPLETE (reason) | Action was taken and resolved successfully |
| ❌ INVALID (reason) | Finding was incorrect, not applicable, or intentional |
| ✋ ON HOLD (reason) | Action deferred — waiting on external dependency or user decision |

---

## [2026-02-20 08:14 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Doc Fix | `agent_type` version attribution — README said v2.1.43, changelog disagrees | ✅ COMPLETE (marked as ~v2.1.43, unconfirmed) |
| 2 | MEDIUM | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's 6 | ✅ COMPLETE (added update note to HOOKS-README and README) |
| 3 | LOW | Hook Options Table | `notification_type`, `message`, `title` missing from Notification Options column | ✅ COMPLETE (added to HOOKS-README) |
| 4 | LOW | Hook Types/Env | Additional `CLAUDE_HOOK_*` env vars from blog sources | ❌ INVALID (false positive — not in official docs) |
| 5 | LOW | New Hook | `OpenInEditor` hook existence | ❌ INVALID (false positive — does not exist in official docs) |

---

## [2026-02-20 11:15 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Hook Options Table | UserPromptSubmit Options column missing `prompt` input field in HOOKS-README | ✅ COMPLETE (added `prompt` to Options column) |
| 2 | LOW | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's tested 6; needs re-testing | ✅ COMPLETE (reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153)) |

---

## [2026-02-20 11:57 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (already reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153); pending response) |

---

## [2026-02-21 06:41 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeCreate — new in v2.1.50 for agent worktree isolation VCS setup | ✅ COMPLETE (added — all 18 hooks consistent across files) |
| 2 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeRemove — new in v2.1.50 for agent worktree isolation VCS teardown | ✅ COMPLETE (added — all 18 hooks consistent across files) |
| 3 | LOW | Hook Options Table | Add `tool_response` to PostToolUse Options column in HOOKS-README | ✅ COMPLETE (added to HOOKS-README) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream bug reported at [#27153](https://github.com/anthropics/claude-code/issues/27153); pending their fix) |

---

## [2026-02-21 07:57 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Presentation | Add can-block/cannot-block badge to WorktreeCreate and WorktreeRemove slides — all other 16 hook slides had this badge | ✅ COMPLETE (added "Cannot Block" badge to both slides) |
| 2 | LOW | Documentation | README.md changelog table missing v2.1.47 `last_assistant_message` — no action needed, table is for new hook additions only | ❌ INVALID (not applicable — editorial choice) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream bug reported; pending their fix) |
| 4 | LOW | Presentation | Setup hook not shown in lifecycle diagram — fires separately via --init/--maintenance | ✅ COMPLETE (added Setup to lifecycle diagram with separate trigger section) |
| 5 | LOW | Workflow | Updated workflow-add-hook to require can-block badge on every new hook slide and update summary can-block list | ✅ COMPLETE (added explicit instructions to workflow) |

---

## [2026-02-21 08:13 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | Add `WorktreeCreate` and `WorktreeRemove` to "Not in Official Docs" table in HOOKS-README — they exist in changelog (v2.1.50) but are absent from official hooks reference | ✅ COMPLETE (added both rows to table) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |
| 3 | LOW | Workflow | Updated workflow-add-hook to include "Not in Official Docs" table step when adding changelog-only hooks | ✅ COMPLETE (added instruction to HOOKS-README section) |

---

## [2026-02-21 09:10 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |

---

## [2026-02-22 02:30 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | WorktreeCreate can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list | ✅ COMPLETE (changed to "Can Block" + added to summary list) |
| 2 | HIGH | Doc Fix | HOOKS-README "Not in Official Docs" table stale — WorktreeCreate and WorktreeRemove ARE now in official docs (17 hooks listed, not 15) | ✅ COMPLETE (removed stale rows, updated count to 17) |
| 3 | MEDIUM | New Input Field | WorktreeCreate missing `name` input field in HOOKS-README Options column | ✅ COMPLETE (added `name` to Options column) |
| 4 | MEDIUM | New Input Field | WorktreeRemove missing `worktree_path` input field in HOOKS-README Options column | ✅ COMPLETE (added `worktree_path` to Options column) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |

---

## [2026-02-23 01:08 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | HOOKS-README heading says "Official 18 Hooks" but only 17 are in official docs (Setup is unofficial) — heading wording misleading | ❌ INVALID (intentional wording) |
| 2 | MEDIUM | Matcher/Schema | HOOKS-README missing per-hook matcher values for SessionEnd, Notification, SubagentStart, SubagentStop, PreCompact, ConfigChange | ✅ COMPLETE (added Per-Hook Matcher Reference table) |
| 3 | LOW | Version Mismatch | TeammateIdle/TaskCompleted version — README says v2.1.33, CHANGELOG.md fetch suggests v2.1.45; needs verification | ✅ COMPLETE (v2.1.33 confirmed correct) |
| 4 | LOW | Documentation | Common input fields (session_id, transcript_path, cwd, permission_mode, hook_event_name) not in dedicated HOOKS-README section | ✅ COMPLETE (added Common Input Fields section) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 10:02 AM PKT] Claude Code v2.1.51

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | ~~MEDIUM~~ | ~~Documentation~~ | ~~HOOKS-README heading says "Official 18 Hooks" but only 17 are in official docs (Setup is unofficial) — heading wording misleading~~ | ❌ INVALID (intentional wording) |
| 2 | MEDIUM | Matcher/Schema | HOOKS-README missing per-hook matcher values for SessionEnd, Notification, SubagentStart, SubagentStop, PreCompact, ConfigChange | ✅ COMPLETE (added to HOOKS-README) |
| 3 | MEDIUM | Hook Types/Env | HOOKS-README prompt/agent hook exclusion list only mentions TeammateIdle — should list all 9 command-only events | ✅ COMPLETE (updated exclusion list) |
| 4 | ~~MEDIUM~~ | ~~Config Drift~~ | ~~Windows settings use relative path — windows hooks won't work regardless~~ | ❌ INVALID (intentional platform difference) |
| 5 | LOW | Version Mismatch | TeammateIdle/TaskCompleted version — README says v2.1.33, CHANGELOG.md fetch suggests v2.1.45; needs verification | ✅ COMPLETE (researched and fixed) |
| 6 | LOW | Documentation | Common input fields (session_id, transcript_path, cwd, permission_mode, hook_event_name) not in dedicated HOOKS-README section | ✅ COMPLETE (added section) |
| 7 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 02:18 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Matcher/Schema | Specify SubagentStart/SubagentStop matcher values (Bash, Explore, Plan, custom) in HOOKS-README — currently says "Agent name string" | ✅ COMPLETE (updated to specific values) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 03:37 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Matcher/Schema | Add WorktreeCreate to HOOKS-README Decision Control Patterns table (stdout path + non-zero exit fails creation) | ✅ COMPLETE (added row to Decision Control Patterns table in HOOKS-README) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 04:38 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-25 10:10 AM PKT] Claude Code v2.1.55

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-26 10:21 AM PKT] Claude Code v2.1.59

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-27 10:08 AM PKT] Claude Code v2.1.62

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Hook Type Classification | Add Setup to command-only event list in HOOKS-README line 326 (Rule 1G: 9 + 8 = 17 ≠ 18) | ✅ COMPLETE (added Setup to command-only list — now 10 + 8 = 18) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-28 11:39 AM PKT] Claude Code v2.1.63

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | PostToolUse can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list (Rules 2A + 2C) | ✅ COMPLETE (changed badge to "Can Block" + added PostToolUse to summary list) |
| 2 | LOW | Documentation | HTTP hook type (`type: "http"`) added in v2.1.63 — not documented in HOOKS-README Hook Types section | ✅ COMPLETE (added `type: "http"` section to HOOKS-README, updated count to "four hook handler types") |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-05 05:48 AM PKT] Claude Code v2.1.69

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | PostToolUseFailure can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list and HOOKS-README Decision Control table (Rules 2A + 2C + 1H) | ✅ COMPLETE (changed badge to "Can Block" + added to summary list + added to Decision Control table) |
| 2 | MEDIUM | New Input Field | `agent_id`/`agent_type` now available on ALL hook events (not just SubagentStart/SubagentStop) — document in HOOKS-README Common Input Fields section | ✅ COMPLETE (added to Common Input Fields table as conditional fields) |
| 3 | MEDIUM | Schema Discovery | Elicitation and ElicitationResult hidden hooks found in v2.1.69 schema enum — document in Not-in-Official-Docs table | ✋ ON HOLD (recurring since 2026-03-04 v2.1.64; waiting for official documentation before adding) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |
| 5 | LOW | Version Fix | InstructionsLoaded hook version corrected from v2.1.64 to v2.1.69 in HOOKS-README and README changelog table | ✅ COMPLETE (updated to v2.1.69) |

---

## [2026-03-06 08:20 AM PKT] Claude Code v2.1.70

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Input Field | Add 6 InstructionsLoaded fields (`file_path`, `memory_type`, `load_reason`, `globs`, `trigger_file_path`, `parent_file_path`) to HOOKS-README Options column | ✅ COMPLETE (added to Options column) |
| 2 | HIGH | New Input Field | Add `tool_use_id` to PreToolUse, PostToolUse, PostToolUseFailure Options columns in HOOKS-README | ✅ COMPLETE (added to Options columns) |
| 3 | MEDIUM | Decision Control | Update TeammateIdle/TaskCompleted in Decision Control table — v2.1.70 adds JSON `continue:false` support | ✅ COMPLETE (updated Decision Control table) |
| 4 | MEDIUM | Not-in-Docs Table | Remove InstructionsLoaded from Not-in-Docs table (now in official docs); update Setup note from "17 hooks" to "18 hooks" | ✅ COMPLETE (removed InstructionsLoaded row, updated Setup note) |
| 5 | LOW | Config Drift | Fix HOOKS-README line 387 cross-reference from "official 18 hooks" to "official 19 hooks" | ✅ COMPLETE (updated anchor link) |
| 6 | LOW | Presentation | Fix InstructionsLoaded slide version from "v2.1.64" to "v2.1.69" | ✅ COMPLETE (updated presentation slide) |
| 7 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 8 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-07 06:27 AM PKT] Claude Code v2.1.71

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Environment Variables | Add `${CLAUDE_SKILL_DIR}` to HOOKS-README env vars table (v2.1.69, skill-specific) | ✅ COMPLETE (added to env vars table) |
| 2 | LOW | Orphan Cleanup | Remove empty `.claude/hooks/sounds/elicitation/` orphan directory (no sound files, not in any map) | ✅ COMPLETE (removed empty directory) |
| 3 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-10 02:52 PM PKT] Claude Code v2.1.72

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-11 11:59 PM PKT] Claude Code v2.1.73

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Documentation | Fix HOOKS-README HTTP hook "Not supported" list — only mentions SessionStart/Setup, should reference all 11 command-only events | ✅ COMPLETE (updated to list all 11 command-only events) |
| 2 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-12 12:22 PM PKT] Claude Code v2.1.74

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | New Env Var | Add `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` to HOOKS-README env vars table — SessionEnd hooks now respect configured timeout (v2.1.74 fix) | ✅ COMPLETE (added to HOOKS-README env vars table) |
| 2 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-14 12:56 AM PKT] Claude Code v2.1.75

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-14 08:59 AM PKT] Claude Code v2.1.76

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook PostCompact` — new in v2.1.76, fires after context compaction | ✅ COMPLETE (added to all files except settings.json — blocked by v2.1.75 schema; will add after Claude Code update) |
| 2 | HIGH | New Hook | `/workflows:workflow-add-hook Elicitation` — new in v2.1.76, MCP server user input request | ✅ COMPLETE (added to all 11 files) |
| 3 | HIGH | New Hook | `/workflows:workflow-add-hook ElicitationResult` — new in v2.1.76, user response to MCP elicitation | ✅ COMPLETE (added to all 11 files) |
| 4 | MEDIUM | Doc Fix | Update HOOKS-README "Not in Docs" Setup note: "18 hooks listed" → "21 hooks listed" | ✅ COMPLETE (updated to 21) |
| 5 | MEDIUM | Decision Control | Add Elicitation/ElicitationResult to HOOKS-README Decision Control table (both can block) | ✅ COMPLETE (added both rows) |
| 6 | LOW | Config Drift | Fix Setup sound file naming: `Setup.mp3` → `setup.mp3` for Linux case-sensitivity | ✅ COMPLETE (renamed to lowercase) |
| 7 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-17 12:44 PM PKT] Claude Code v2.1.77

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Matcher/Schema | Update PreToolUse matcher example in HOOKS-README line 426: add `Agent`, `WebFetch`, `WebSearch` tool names | ✅ COMPLETE (added 3 tool names to matcher example) |
| 2 | LOW | Config Drift | Fix HOOKS-README line 394 stale anchor `#hook-events-overview---official-19-hooks` → `#hook-events-overview---official-22-hooks` | ✅ COMPLETE (fixed internal anchor) |
| 3 | LOW | Schema Discovery | Document `asyncRewake` schema option in HOOKS-README (exists since v2.1.72, undocumented in official docs) | ✅ COMPLETE (added Hook Option subsection) |
| 4 | LOW | Presentation | Fix slide counter initial text "1 / 26" → "1 / 29" in presentation/index.html line 2376 | ✅ COMPLETE (updated to 1 / 29) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-18 06:39 PM PKT] Claude Code v2.1.78

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook StopFailure` — new in v2.1.78, fires when turn ends due to API error (rate limit, auth failure) | ✅ COMPLETE (added to all files — 23 hooks consistent across repo) |
| 2 | LOW | Environment Variables | Add `CLAUDE_PLUGIN_DATA` to HOOKS-README env vars table (plugin persistent data directory, from official hooks reference) | ✅ COMPLETE (added to HOOKS-README env vars table) |
| 3 | LOW | Schema Discovery | Elicitation/ElicitationResult previously hidden hooks — now in official docs and repo | ✅ COMPLETE (resolved — both hooks added in v2.1.76 run, now fully documented) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-19 12:19 PM PKT] Claude Code v2.1.79

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Input Field | Add `error`, `error_details`, `last_assistant_message` to StopFailure Options column in HOOKS-README | ✅ COMPLETE (added 3 input fields to Options column) |
| 2 | HIGH | Matcher/Schema | Add InstructionsLoaded matcher (`load_reason`: session_start, nested_traversal, path_glob_match, include, compact) to Per-Hook Matcher Reference table | ✅ COMPLETE (added to matcher table) |
| 3 | HIGH | Matcher/Schema | Add StopFailure matcher (`error`: rate_limit, authentication_failed, billing_error, invalid_request, server_error, max_output_tokens, unknown) to Per-Hook Matcher Reference table | ✅ COMPLETE (added to matcher table) |
| 4 | MEDIUM | Config Drift | Fix HOOKS-README line 412 stale anchor `#hook-events-overview---official-22-hooks` → `#hook-events-overview---official-23-hooks` | ✅ COMPLETE (fixed internal anchor) |
| 5 | MEDIUM | Not-in-Docs | Remove StopFailure from "Not in Official Docs" table; update Setup note | ❌ INVALID (user confirmed StopFailure is not in official docs — keep in table) |
| 6 | LOW | Hook Options Table | Fix ElicitationResult Options: remove `action`/`content` (output fields), add `user_response`, `message` (input fields) | ✅ COMPLETE (fixed input/output field confusion) |
| 7 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-20 07:22 AM PKT] Claude Code v2.1.80

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Matcher/Schema | Add `resume` to SessionEnd matcher values in HOOKS-README line 452 and presentation slide 17 | ✅ COMPLETE (added `resume` to both HOOKS-README and presentation) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-23 09:44 PM PKT] Claude Code v2.1.81

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Not-in-Docs Table | Remove StopFailure from Not-in-Docs table; update Setup note from "21 hooks listed" to "22 hooks listed, Setup excluded" | ✋ ON HOLD (user decision: keep StopFailure in Not-in-Docs table like Setup) |
| 2 | LOW | Hook Options Table | Remove `mode` from ElicitationResult Options column — not in official docs for this hook (only for Elicitation) | ✅ COMPLETE (removed `mode` from ElicitationResult Options) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-25 09:43 PM PKT] Claude Code v2.1.83

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook CwdChanged` — v2.1.83, fires when working directory changes (reactive env management) | ✅ COMPLETE (added to all files — 25 hooks consistent across repo) |
| 2 | HIGH | New Hook | `/workflows:workflow-add-hook FileChanged` — v2.1.83, fires when files change | ✅ COMPLETE (added to all files — 25 hooks consistent across repo) |
| 3 | MEDIUM | Not-in-Docs Table | Update StopFailure entry — now confirmed in official docs by both agents; update Setup note "21 hooks" → "22 hooks listed, Setup excluded" | ✅ COMPLETE (removed StopFailure row, updated Setup note to "22 hooks listed, Setup excluded") |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-26 08:39 PM PKT] Claude Code v2.1.84

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook TaskCreated` — v2.1.84, fires when task created via TaskCreate tool | ✅ COMPLETE (added to all 14 files — 26 hooks consistent across repo) |
| 2 | HIGH | Not-in-Docs Table | Remove CwdChanged and FileChanged rows from HOOKS-README Not-in-Docs table — both now in official docs | ✅ COMPLETE (removed both rows from Not-in-Docs table) |
| 3 | HIGH | Not-in-Docs Table | Update Setup note from "(22 hooks listed, Setup excluded)" to "(25 hooks listed, Setup excluded)" | ✅ COMPLETE (updated to 25 hooks listed) |
| 4 | MEDIUM | Hook Options | Add `old_cwd`, `new_cwd` to CwdChanged Options column in HOOKS-README | ✅ COMPLETE (added to Options column) |
| 5 | MEDIUM | Env Var Docs | Fix `$CLAUDE_ENV_FILE` from "SessionStart only" to "SessionStart, CwdChanged, FileChanged" | ✅ COMPLETE (updated availability scope) |
| 6 | MEDIUM | Matcher Table | Add CwdChanged (no matcher) and FileChanged (filename basename) to Per-Hook Matcher Reference table | ✅ COMPLETE (added both entries to matcher table) |
| 7 | MEDIUM | Config Drift | Fix HOOKS-README stale anchor `#official-23-hooks` → `#official-26-hooks` | ✅ COMPLETE (updated anchor to match new heading) |
| 8 | MEDIUM | Can-Block Status | Investigate PostToolUseFailure — both agents report official docs say Cannot Block, but repo has Can Block since v2.1.69 | ✋ ON HOLD (needs investigation — keeping current Can Block status until confirmed) |
| 9 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-27 01:21 PM PKT] Claude Code v2.1.85

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Presentation | Fix hook numbering bug — TaskCreated has duplicate number 16 (same as TaskCompleted); all 9 subsequent hooks (ConfigChange through FileChanged) are off by one (17→18 through 25→26) | ✅ COMPLETE (fixed 10 hook-number spans: TaskCreated→17, ConfigChange→18, WorktreeCreate→19, WorktreeRemove→20, InstructionsLoaded→21, Elicitation→22, ElicitationResult→23, StopFailure→24, CwdChanged→25, FileChanged→26) |
| 2 | MEDIUM | New Hook Option | Document new `if` conditional field for hooks — permission rule syntax (e.g., `Bash(git *)`) reduces unnecessary hook process spawning (v2.1.85) | ✋ ON HOLD (not yet in official docs pages — only in GitHub changelog; will document when docs update) |
| 3 | MEDIUM | Hook Enhancement | Document PreToolUse `updatedInput` for AskUserQuestion — enables headless integrations to auto-respond to user questions (v2.1.85) | ✋ ON HOLD (not yet in official docs pages — only in GitHub changelog; will document when docs update) |
| 4 | MEDIUM | Can-Block Status | PostToolUseFailure — official docs say Cannot Block (output is only `additionalContext`), but repo had Can Block since v2.1.69 in presentation badge, summary list, and HOOKS-README Decision Control table | ✅ COMPLETE (changed presentation badge to "Cannot Block", removed from summary can-block list, removed from HOOKS-README Decision Control blocking group) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-28 06:07 PM PKT] Claude Code v2.1.86

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook Option | Document `if` conditional field in HOOKS-README — now confirmed in official hooks guide (permission rule syntax, v2.1.85). Previously ON HOLD awaiting docs | ✅ COMPLETE (added Hook Option: `if` subsection to HOOKS-README with syntax, supported hooks, and examples) |
| 2 | LOW | Matcher/Schema | Add `AskUserQuestion`, `ExitPlanMode` to PreToolUse matcher example in HOOKS-README line 448 (official docs list these as matchable tool names) | ✅ COMPLETE (added both tool names to PreToolUse matcher example) |
| 3 | LOW | Hook Enhancement | Document PreToolUse `updatedInput` for AskUserQuestion — headless integration feature (v2.1.85) | ✅ COMPLETE (added subsection to HOOKS-README with example JSON and use cases) |
| 4 | LOW | Schema Discovery | Monitor `CronCreate` hook — mentioned in v2.1.85 changelog but NOT in schema or official docs | ❌ INVALID (not in schema propertyNames enum, not in official docs — likely internal/non-hook feature per Rule 6A) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-29 07:43 PM PKT] Claude Code v2.1.87

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Hook Options Table | Update WorktreeCreate Options: `name` → `worktree_path`, `worktree_name`, `base_branch`; WorktreeRemove: add `worktree_name` — per official docs | ✅ COMPLETE (updated HOOKS-README Options column for both hooks) |
| 2 | MEDIUM | Hook Options Table | Update FileChanged Options: `event` → `change_type` per official docs | ✅ COMPLETE (updated HOOKS-README Options column) |
| 3 | MEDIUM | Hook Options Table | Update Elicitation Options: remove stale fields, add `tool_name`, `form_fields`; ElicitationResult: remove stale fields, add `tool_name`, `form_fields` — per official docs | ✅ COMPLETE (updated HOOKS-README Options column for both hooks) |
| 4 | MEDIUM | Hook Options Table | Update PreCompact/PostCompact: `trigger` → `compact_trigger`, remove undocumented `custom_instructions`/`compact_summary` — per official docs | ✅ COMPLETE (updated HOOKS-README Options column and matcher table) |
| 5 | MEDIUM | Can-Block Status | PostToolUse can-block — official docs confirm "No" (exit code 2 = feedback only, tool already ran). Updated presentation badge and summary list, removed from HOOKS-README Decision Control blocking group | ✅ COMPLETE (changed presentation badge to Cannot Block, removed from summary can-block list, updated Decision Control table) |
| 6 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-31 07:03 PM PKT] Claude Code v2.1.88

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook PermissionDenied` — v2.1.88, fires after auto mode classifier denials; return `{retry: true}` to retry | ✅ COMPLETE (added to all 14 files — 27 hooks consistent across repo) |
| 2 | HIGH | Not-in-Docs Table | Add PermissionDenied to HOOKS-README Not-in-Docs table; update Setup note to include PermissionDenied exclusion | ✅ COMPLETE (added row + updated Setup note to "25 hooks listed, Setup and PermissionDenied excluded") |
| 3 | MEDIUM | Hook Options Table | Investigate CwdChanged field name: `old_cwd` vs `previous_cwd` — WebFetch extraction suggested `previous_cwd` but page was truncated | ❌ INVALID (false positive — official docs confirm `old_cwd` and `new_cwd`, HOOKS-README is correct) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-04-01 10:58 AM PKT] Claude Code v2.1.89

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Config Drift | Fix HOOKS-README line 178: "not all 26" → "not all 27" (stale after PermissionDenied addition) | ✅ COMPLETE (updated to "not all 27") |
| 2 | LOW | New Feature | Document PreToolUse "defer" permission decision (v2.1.89, headless resume) in HOOKS-README Decision Control table | ✋ ON HOLD (not yet in official docs pages — only in GitHub changelog; will document when docs update) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-04-02 09:24 PM PKT] Claude Code v2.1.90

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Not-in-Docs Table | Remove PermissionDenied from HOOKS-README Not-in-Docs table — now confirmed in official hooks reference and guide; update Setup note from "(25 hooks listed, Setup and PermissionDenied excluded)" to "(26 hooks listed, Setup excluded)" | ✅ COMPLETE (removed PermissionDenied row, updated Setup note) |
| 2 | HIGH | Hook Options Table | Add `tool_name`, `tool_input`, `tool_use_id`, `reason` to PermissionDenied Options column in HOOKS-README (confirmed by schema and official docs) | ✅ COMPLETE (added 4 input fields to Options column) |
| 3 | HIGH | Matcher/Schema | Fix PermissionDenied matcher in HOOKS-README Per-Hook Matcher Reference — line 503 says "No matcher support" but official docs confirm tool_name matcher (same as PreToolUse/PostToolUse/PostToolUseFailure/PermissionRequest) | ✅ COMPLETE (updated to tool_name matcher with example) |
| 4 | MEDIUM | New Feature | Document PreToolUse "defer" permission decision in HOOKS-README Decision Control table — now confirmed in official hooks guide and reference (v2.1.89, headless resume) | ✅ COMPLETE (added `defer` to PreToolUse permissionDecision values + added PermissionDenied retry row) |
| 5 | MEDIUM | Can-Block Status | PermissionDenied can-block — official docs say "Cannot block but can signal retry" but presentation has "Can Block" badge and summary list includes it | ✅ COMPLETE (changed presentation badge to "Cannot Block", removed from summary can-block list) |
| 6 | LOW | Config Drift | Fix HOOKS-README line 47 stale count: "Not all 26 hooks are supported" → "Not all 27 hooks are supported" | ✅ COMPLETE (updated to "Not all 27") |
| 7 | LOW | Config Drift | Fix HOOKS-README line 186 stale count: "remaining 10 hooks" → "remaining 21 hooks" (27 - 6 = 21) | ✅ COMPLETE (updated to "remaining 21") |
| 8 | MEDIUM | Workflow Fix | Root cause: workflow-add-hook only updates structured locations (heading, numbered list) but never sweeps for prose-embedded count references. Added Step 6 "Stale Count Sweep" to workflow-add-hook and Rule 7A/7B to verification checklist | ✅ COMPLETE (updated workflow-add-hook.md, workflow-changelog.md, and verification-checklist.md) |
| 9 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-04-03 10:57 PM PKT] Claude Code v2.1.91

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-04-04 11:19 AM PKT] Claude Code v2.1.92

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Presentation | Fix PermissionDenied slide 31 stale text: remove "Not yet in official hooks reference — changelog and schema only" (now in official docs since v2.1.90 run confirmed) | ✅ COMPLETE (removed stale text from slide 31 line 2354) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-04-14 11:38 PM PKT] Claude Code v2.1.107

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | PreCompact: change presentation badge from "Cannot Block" to "Can Block" (v2.1.105 changed can-block status) | ✅ COMPLETE (changed badge class and text on slide 15) |
| 2 | HIGH | Can-Block Fix | Add PreCompact to presentation summary "Hooks That Can Block" list (lines 2589-2601) | ✅ COMPLETE (added PreCompact to summary list) |
| 3 | HIGH | Decision Control | Add PreCompact to HOOKS-README Decision Control table — exit code 2 or `{"decision":"block"}` blocks compaction | ✅ COMPLETE (added row to Decision Control table) |
| 4 | MEDIUM | Hook Options Table | Stop: add `stop_reason` input field to Options column (per official docs) | ✅ COMPLETE (added to Options column) |
| 5 | MEDIUM | Hook Options Table | StopFailure: update `error`/`error_details` → `error_type`/`error_message` (per official docs) | ✅ COMPLETE (renamed fields in Options column) |
| 6 | MEDIUM | Hook Options Table | ConfigChange: update `source` → `config_source` (per official docs) | ✅ COMPLETE (renamed in Options column + matcher table) |
| 7 | MEDIUM | Hook Options Table | Elicitation: update `mcp_server_name` → `server_name`, `form_fields` → `elicitation_schema` (per official docs) | ✅ COMPLETE (renamed in Options column + matcher table) |
| 8 | MEDIUM | Hook Options Table | ElicitationResult: update `mcp_server_name` → `server_name`, remove `form_fields` (per official docs) | ✅ COMPLETE (renamed + removed in Options column + matcher table) |
| 9 | MEDIUM | Hook Options Table | WorktreeCreate: remove `worktree_name`/`base_branch`, add `isolation_reason` (per official docs) | ✅ COMPLETE (replaced fields in Options column) |
| 10 | MEDIUM | Hook Options Table | WorktreeRemove: remove `worktree_name`, add `removal_reason` (per official docs) | ✅ COMPLETE (replaced field in Options column) |
| 11 | MEDIUM | Hook Options Table | FileChanged: update `change_type` → `changed_reason` (per official docs) | ✅ COMPLETE (renamed in Options column) |
| 12 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |
