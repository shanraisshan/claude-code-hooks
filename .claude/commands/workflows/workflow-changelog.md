---
description: Track Claude Code changelog and find what needs updating in this repo
argument-hint: [number of versions to check, default 10]
---

# Workflow Changelog

You are a coordinator for the claude-code-hooks project. Your job is to launch two research agents in parallel, wait for their results, merge findings, and present a unified report.

**Versions to check:** `$ARGUMENTS` (default: 10 if empty or not a number)

This is a **read-then-report** workflow. Launch agents, merge results, and produce a report. Only take action if the user approves.

---

## Phase 0: Launch Both Agents in Parallel

**Immediately** spawn both agents using the Task tool **in the same message** (parallel launch):

### Agent 1: workflow-changelog-agent

Spawn using `subagent_type: "workflow-changelog-agent"`. Give it this prompt:

> Research the claude-code-hooks project for changelog drift. Check the last $ARGUMENTS versions (default: 10).
>
> Fetch these 3 external sources:
> 1. Hooks Reference: https://code.claude.com/docs/en/hooks
> 2. Hooks Guide: https://code.claude.com/docs/en/hooks-guide
> 3. Changelog: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
>
> Then read all local repository files (settings, hooks.py, config, README, HOOKS-README, install settings, presentation) and analyze differences. Return a structured findings report covering missing hooks, configuration drift, version mismatches, hook behavior changes, bug fixes, matcher accuracy, presentation staleness, agent frontmatter hooks, and schema hook discovery (hidden hooks in settings.json schema propertyNames enum not in docs).

### Agent 2: claude-code-guide

Spawn using `subagent_type: "claude-code-guide"`. Give it this prompt:

> Research the latest Claude Code hooks system. I need you to find:
> 1. The complete list of all currently supported hook events (e.g. PreToolUse, PostToolUse, Stop, etc.) with their descriptions
> 2. Any new hooks or hook changes introduced in recent Claude Code versions
> 3. New hook input fields, matcher values, or configuration options added recently
> 4. Any new hook types (command, prompt, agent) or new environment variables
> 5. Changes to agent/skill frontmatter hook support
> 6. Any bug fixes related to hooks
> 7. New features in Claude Code that relate to hooks (e.g. new tool names for matchers, new subagent types)
>
> Be thorough — search the web, fetch docs, and provide concrete version numbers and details for everything you find.

Both agents run independently and will return their findings.

---

## Phase 0.5: Read Verification Checklist

**While agents are running**, read `changelog/verification-checklist.md`. This file contains accumulated verification rules — each rule specifies what to check, at what depth, and against which source. Every rule MUST be executed during Phase 2. The checklist is the project's regression test suite for drift detection.

---

## Phase 1: Read Previous Changelog Entries

**Before merging findings**, read the file `changelog/changelog.md` to get the last 10 changelog entries. Each entry is separated by `---`. Parse the priority actions from those previous entries so you can compare them against the current findings. This lets you identify:
- **Recurring items** — issues that appeared before and are still unresolved
- **Newly resolved items** — issues from previous runs that are now fixed
- **New items** — issues that appear for the first time in this run

---

## Phase 2: Merge Findings & Generate Report

**Wait for both agents to complete.** Once you have:
- **workflow-changelog-agent findings** — detailed repo analysis with local file reads, external doc fetches, and drift detection
- **claude-code-guide findings** — independent research on latest Claude Code hooks, features, and changes

Cross-reference the two. The workflow-changelog-agent provides repo-specific drift analysis, while the claude-code-guide agent may surface things it missed (e.g. very recent changes, undocumented features, or context from web searches). Flag any contradictions between the two for the user to resolve.

**Execute the verification checklist:** For every rule in `changelog/verification-checklist.md`, perform the check at the specified depth using the agent findings as source data. Include a **Verification Log** section in the report showing each rule's result:

```
Verification Log:
Rule # | Category         | Depth         | Result | Notes
1      | Hook Options     | field-level   | PASS   | All fields match
2      | Matcher Values   | content-match | FAIL   | SubagentStart values differ
...
```

**Update the checklist if needed:** If a finding reveals a new type of drift that no existing checklist rule covers (or covers at insufficient depth), append a new rule to `changelog/verification-checklist.md`. The rule must include: category, what to check, depth level, what source to compare against, date added, and the origin (what error prompted this rule). Do NOT add rules for one-off issues that won't recur.

Also compare the current findings against the previous changelog entries (from Phase 1). For each priority action, mark it as:
- `NEW` — first time this issue appears
- `RECURRING` — appeared in a previous run and is still unresolved (include which run date it first appeared)
- `RESOLVED` — appeared in a previous run but is now fixed (include resolution date)

Produce a structured report with these sections:

1. **New Hooks to Add** — Missing hooks with version and `/workflows:workflow-add-hook` command
2. **Configuration Drift** — Inconsistencies across files with specific fixes
3. **Version & Count Mismatches** — Table showing current vs expected for each location
4. **Documentation Updates** — Outdated docs with changelog version references
5. **Bug Fixes & Workaround Status** — Known issues with fix status
6. **New Features to Consider** — Relevant new features from changelog
7. **Matcher & Schema Accuracy** — Per-hook verification status
8. **Hook Types & Environment Variables** — Documentation coverage status
9. **Removed/Deprecated Hooks** — Hooks in repo but not in docs
10. **Presentation Updates** — Staleness across all presentation elements
11. **Hook Options Table** — Per-hook Options column accuracy
12. **Agent Frontmatter Hooks** — 3-hook assumption verification
13. **Schema Hook Discovery** — Hidden/undocumented hooks found in the settings.json schema `propertyNames` enum but not in official docs or changelog (e.g. `Elicitation`, `ElicitationResult`), and hooks in docs but not in the schema. Present as a comparison table: Hook Name | In Schema | In Official Docs | In Local Repo. Flag hidden hooks prominently — these are early signals of upcoming features.
14. **claude-code-guide Agent Findings** — Unique insights from the agent that weren't captured by the workflow-changelog-agent. Only include findings that add new information. If there are contradictions between the two agents, flag them for the user to resolve. Do NOT list "confirmed agreements" — if both agents found the same thing, that's expected and not worth reporting.

End with a prioritized **Action Items** summary table. Each item must include a `Status` column showing `NEW`, `RECURRING (first seen: <date>)`, or `RESOLVED`:

```
Priority Actions:
#  | Type              | Action                                    | Status
1  | New Hook          | /workflows:workflow-add-hook <Name>                      | NEW
2  | New Input Field   | Document <field> added to <Hook> in v<X>  | NEW
3  | Hook Options Table| Update Options column for <Hook>          | RECURRING (first seen: 2026-02-20)
4  | Removed Hook      | Investigate <Name> removal                | NEW
5  | Config Drift      | Fix <description>                         | NEW
6  | Version Update    | Update badges to vX.X.X                   | NEW
7  | Can-Block Fix     | Fix can-block status for <Hook>           | NEW
8  | Matcher/Schema    | Update documentation for <Hook>           | NEW
9  | Hook Types/Env    | Document missing items                    | RECURRING (first seen: 2026-02-15)
10 | Presentation      | Update to <version>                       | NEW
11 | Agent Hook Docs   | Update frontmatter hook support           | NEW
12 | Schema Discovery  | Hidden hook <Name> found in schema enum   | NEW
13 | Bug Fix           | Remove <workaround>                       | RESOLVED
```

Also include a **Resolved Since Last Run** section listing any items from the previous run that are no longer issues.

---

## Phase 2.5: Append Summary to changelog/changelog.md

**This phase is MANDATORY — always execute it before presenting the report to the user.**

Read the existing `changelog/changelog.md` file, then **append** (do NOT overwrite) a new entry at the end. The entry format must be exactly:

```markdown
---

## [<YYYY-MM-DD HH:MM AM/PM PKT>] Claude Code v<VERSION>

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH/MED/LOW | <type> | <action description> | <status> |
| ... | ... | ... | ... | ... |
```

**Status format — MUST use one of these three formats:**
- `✅ COMPLETE (reason)` — action was taken and resolved successfully
- `❌ INVALID (reason)` — finding was incorrect, not applicable, or intentional
- `✋ ON HOLD (reason)` — action deferred, waiting on external dependency or user decision

The `(reason)` is mandatory and must briefly explain what was done or why. Examples:
- `✅ COMPLETE (added to HOOKS-README)`
- `❌ INVALID (false positive — not in official docs)`
- `✋ ON HOLD (upstream issue #27153 still open)`

**Rules for appending:**
- Always append — never overwrite or replace previous entries
- The date and time is when the command is executed in Pakistan Standard Time (PKT, UTC+5); get it by running `TZ=Asia/Karachi date "+%Y-%m-%d %I:%M %p PKT"`. The version comes from agent findings
- If `changelog/changelog.md` doesn't exist or is empty, create it with the Status Legend table (see top of file) then the first entry
- Each entry is separated by `---`
- **Only include items with HIGH, MEDIUM, or LOW priority** — omit NONE priority items (things that need no action)

---

## Phase 2.6: Update Version Across README and Presentation

**This phase is MANDATORY — always execute it immediately after Phase 2.5, before presenting the report.**

This is a standard maintenance step, NOT an issue to report. When the latest Claude Code version differs from the repo's version, update it automatically in all locations:

1. **README.md badge (line 2):** Update version number and PKT timestamp. Run `TZ=Asia/Karachi date "+%b %d, %Y %-I:%M %p PKT"` to get the time, URL-encode it (spaces → `%20`, commas → `%2C`), and replace both the version and date portions in the badge.

2. **Presentation version references:** Update all three locations in `presentation/index.html`:
   - Title slide (search for version pattern near line 543)
   - Slide 2 introduction (search for version pattern near line 561)
   - Slide 3 TOC (search for version pattern near line 599)

   Also update the date on the title slide and slide 3 if present.

**Do NOT log version updates as action items in the changelog or report.** Version syncing is a routine part of every run, not a finding. Only log it if the update fails or requires manual intervention.

---

## Phase 2.7: Update CLAUDE.md If Needed

**This phase is MANDATORY — always execute it after Phase 2.6.**

Read `CLAUDE.md` at the project root and check if any of the following need updating based on the current run's findings:
- Hook count (e.g. "currently **19**" → new count)
- Agent hook count or list
- `once: true` hook list
- Slide count / `totalSlides`
- New conventions or structural changes discovered
- Any other facts in CLAUDE.md that are now stale

If updates are needed, edit CLAUDE.md. If everything is current, skip silently.

---

## Phase 3: Offer to Take Action

After presenting the report (and confirming both changelog/changelog.md and the README badge were updated), ask the user:

1. **Execute all actions** — Handle everything (new hooks via `/workflows:workflow-add-hook`, fixes, updates)
2. **Execute specific actions** — User picks which numbers to execute
3. **Just save the report** — No changes

When executing:
- **New hooks**: Use `/workflows:workflow-add-hook <HookName>` (one at a time, in order)
- **New input fields**: Update README.md changelog table, HOOKS-README.md Options column + description, and presentation slides
- **Hook options changes**: Edit HOOKS-README.md Options column; if `once`/`timeout` changed, also update all 4 settings files
- **Removed hooks**: Confirm with user before removing
- **Agent hook docs**: Update HOOKS-README.md and presentation (this project supports 6 agent hooks, not all 16)
- After all actions, re-run verification to confirm consistency

---

## Critical Rules

1. **Launch BOTH agents in parallel** in a single message — never sequentially
2. **Wait for both agents** before generating the report
3. **Never guess** versions or dates — use data from the agents
4. **New input fields are HIGH PRIORITY** — they require README, HOOKS-README, and presentation updates. Never dismiss them as "informational"
5. **For new hooks, ALWAYS use `/workflows:workflow-add-hook`** — never manually add hooks
6. **Cross-reference counts** — the same hook count must appear in: settings (x4), hooks.py, hooks-config.json, HOOKS-README.md, README.md badge, and presentation. Also grep HOOKS-README for ALL prose-embedded count references (`\d+ hook`, `not all \d+`, `remaining \d+ hook`) — these get missed by structured checks.
7. **Don't auto-execute** — always present the report first
8. **Agent hooks** — this project supports 6 agent hooks (PreToolUse, PostToolUse, PermissionRequest, PostToolUseFailure, Stop, SubagentStop). Not all 16 hooks fire in agent sessions.
9. **ALWAYS append to changelog/changelog.md** — Phase 2.5 is mandatory. Never skip it. Never overwrite previous entries.
10. **Compare with previous runs** — read the last 10 entries from changelog/changelog.md and mark each action item as NEW, RECURRING, or RESOLVED.
11. **ALWAYS execute the verification checklist** — read `changelog/verification-checklist.md` and execute every rule. Include a Verification Log in the report. Append new rules when a new type of drift is discovered that no existing rule covers.
12. **Checklist rules are append-only** — never remove or weaken existing rules. Only add new rules or upgrade depth levels.
