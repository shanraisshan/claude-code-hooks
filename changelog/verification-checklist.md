# Verification Checklist

Rules accumulate over time. Each workflow-changelog run MUST execute ALL rules at the specified depth. When a new type of drift is caught that an existing rule should have caught (but didn't exist or was too shallow), append a new rule here.

## Depth Levels

| Depth | Meaning | Example |
|-------|---------|---------|
| `exists` | Check if a section/table/file exists | "Does HOOKS-README have a matcher table?" |
| `presence-check` | Check if a specific item is present or absent | "Is WorktreeCreate in the Not-in-Docs table?" |
| `content-match` | Compare actual values word-by-word against source | "Do SubagentStart matcher values match official docs?" |
| `field-level` | Verify every individual field is accounted for | "Does each hook's Options column list every input field from docs?" |
| `cross-file` | Same value must match across multiple files | "Does hook count match across settings x4, hooks.py, config, README, HOOKS-README, presentation?" |

---

## 1. HOOKS-README Documentation

Rules that verify HOOKS-README content against official docs.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 1A | Hook Options | For each hook, verify every input field listed in official docs appears in HOOKS-README Options column | field-level | hooks-reference page | 2026-02-20 | Notification fields (`notification_type`, `message`, `title`) were missing |
| 1B | Matcher Values | For each hook with a matcher, compare HOOKS-README per-hook matcher reference values against official docs values word-by-word | content-match | hooks-reference page | 2026-02-24 | SubagentStart said "Agent name string" instead of specific values (Bash, Explore, Plan, custom) |
| 1C | Not-in-Docs Table | For each hook listed in HOOKS-README "Not in Official Docs" table, verify it is actually absent from official docs; remove if now present | presence-check | hooks-reference page | 2026-02-22 | WorktreeCreate/WorktreeRemove were listed as "not in docs" but had been added |
| 1D | Command-Only Events | Verify HOOKS-README prompt/agent hook exclusion list includes ALL command-only events (not just a subset) | content-match | hooks-reference page | 2026-02-24 | List only mentioned TeammateIdle, omitted 8 other command-only events |
| 1E | Common Input Fields | Verify HOOKS-README common input fields section lists all fields from official docs (session_id, transcript_path, cwd, permission_mode, hook_event_name) | field-level | hooks-reference page | 2026-02-23 | Section was missing entirely |
| 1F | Environment Variables | Verify HOOKS-README env vars section lists all standard hook env vars from official docs | field-level | hooks-guide page | 2026-02-20 | Potential env var gaps flagged by external sources |
| 1G | Hook Type Classification Totals | Verify that (command-only event count) + (prompt/agent supported count) = total hook count. If they don't sum correctly, a hook is missing from one of the two lists | content-match | HOOKS-README hook types section | 2026-02-24 | Setup was omitted from both lists (9 command-only + 8 prompt/agent = 17, but total is 18) |
| 1H | Decision Control Table Completeness | For each hook that can-block per official docs, verify it has an entry in the HOOKS-README Decision Control Patterns table (lines 446+). Check both JSON-based decision hooks AND exit-code-only/stdout-based hooks | presence-check | hooks-reference page can-block list vs HOOKS-README Decision Control Patterns table | 2026-02-24 | WorktreeCreate was can-block in official docs and on presentation slide (fixed 2026-02-22) but was never added to the HOOKS-README Decision Control table — Rule 2A only checks presentation badges, not the HOOKS-README table |
| 1I | Hook Handler Types List | Verify HOOKS-README Hook Types section lists all handler types from official docs (command, http, prompt, agent). Check both the count in the intro text and the subsection headings. Handler types ≠ hook event classification (Rule 1G) | content-match | hooks-reference page | 2026-02-28 | HOOKS-README said "three hook handler types" but v2.1.63 added `http` as a fourth — no rule covered handler type completeness |

---

## 2. Presentation

Rules that verify presentation slides accuracy and completeness.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 2A | Can-Block Status | For each hook, verify can-block/cannot-block badge in presentation matches official docs can-block table | content-match | hooks-reference page | 2026-02-22 | WorktreeCreate had "Cannot Block" but should have been "Can Block" |
| 2B | Presentation Slides | Verify totalSlides variable matches actual slide count, and each hook has a dedicated slide | cross-file | presentation index.html | 2026-02-21 | Slide count consistency after adding new hooks |
| 2C | Can-Block Summary Slide | Verify the presentation summary slide listing of blocking hooks matches the set of individual hook slides that have "Can Block" badge | cross-file | presentation individual slides vs summary slide | 2026-02-24 | WorktreeCreate was wrong on individual slide AND missing from summary — two independent errors, Rule 2A only checks individual slides vs docs |
| 2D | Lifecycle Diagram Completeness | Verify all hooks appear somewhere in the presentation lifecycle diagram (sequential flow, async section, or separate trigger section). Count hooks in diagram must equal total hook count | presence-check | presentation lifecycle diagram vs hook list | 2026-02-24 | Setup was missing from lifecycle diagram (caught 2026-02-21) but no rule was added to prevent recurrence |
| 2E | Presentation vs HOOKS-README Matcher Values | For hooks that show matcher values on presentation slides, verify those values match what HOOKS-README per-hook matcher reference table says | cross-file | presentation slides vs HOOKS-README | 2026-02-24 | Rule 1B checks HOOKS-README vs official docs, but presentation could drift independently from HOOKS-README |
| 2F | Hook Number Sequence | Verify all `<span class="hook-number">N</span>` values in presentation are sequential 1 through total-hook-count with no duplicates and no gaps. Extract all hook-number spans and check the sequence | cross-file | presentation hook-number spans | 2026-03-27 | TaskCreated was added with duplicate hook-number 16 (same as TaskCompleted) because workflow-add-hook did not increment hook-numbers for subsequent slides — only data-slide numbers were shifted |

---

## 3. Cross-File Consistency

Rules that verify the same value matches across multiple repo files.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 3A | Version Badges | Compare version string across README badge, presentation title (line 543), presentation slide 2 (line 561), presentation slide 3 (line 599) | cross-file | changelog latest version | 2026-02-21 | Version staleness found in multiple locations on every run |
| 3B | Hook Count | Verify hook count is identical across: settings.json, settings-mac.json, settings-linux.json, settings-windows.json, hooks.py HOOK_SOUND_MAP, hooks-config.json, HOOKS-README heading, README badge, presentation (check ALL count locations: slide 2 "N Hooks Explained", slide 2 "supports N hooks (as of vX.X.XX)" use-case span, slide 3 TOC title, totalSlides variable) | cross-file | all listed files | 2026-02-21 | Count went from 16 to 18 but not all files were updated. The "supports N hooks" use-case span on slide 2 was missed during 2026-03-26 run |
| 3C | Hook Name Spelling | Verify all 18 hook names are spelled identically (exact PascalCase) across: settings.json hooks keys, settings-mac/linux/windows hooks keys, hooks.py HOOK_SOUND_MAP keys, hooks-config.json toggle names (disable[Name]Hook pattern), HOOKS-README table, presentation slide hook-name spans, presentation TOC items, lifecycle diagram | cross-file | all listed files | 2026-02-24 | Rule 3B only checks count — a misspelled hook would pass count check but break functionality |
| 3D | Agent Hook Consistency | Verify the 6 agent hooks are consistent across: AGENT_HOOK_SOUND_MAP in hooks.py (6 entries), agent sound folders (6 folders), HOOKS-README agent hooks section (6 listed), presentation agent slide (says "6 of N hooks") | cross-file | hooks.py, filesystem, HOOKS-README, presentation | 2026-02-24 | Agent hook count/names never had a cross-file consistency rule |

---

## 4. Settings & Config

Rules that verify settings files, config, and filesystem assets.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 4A | Sound Folder Existence | For each entry in HOOK_SOUND_MAP and AGENT_HOOK_SOUND_MAP, verify corresponding folder exists under .claude/hooks/sounds/ and contains at least one .mp3 and one .wav file | presence-check | hooks.py maps vs filesystem | 2026-02-24 | Sound folders could be missing after manual edits; workflow-add-hook creates them but no verification existed |
| 4B | Settings Hook Structure | For each hook across all 4 settings files, verify: timeout value (5000 for all except Setup which is 30000), async is true, `once` flag only on PreCompact/SessionStart/SessionEnd, statusMessage matches hook name | field-level | settings.json vs settings-mac/linux/windows | 2026-02-24 | Wrong timeout or missing once flag would cause behavioral bugs not caught by name/count checks |
| 4C | hooks-config.json Toggle Pattern | Verify each hook has exactly one toggle key in hooks-config.json following the pattern `disable[ExactHookName]Hook`, and no extra/orphaned toggles exist | presence-check | hooks-config.json vs hook name list | 2026-02-24 | A renamed or removed hook could leave orphaned toggle keys or miss new ones |
| 4D | README Changelog Table | Verify latest row in README.md changelog table has current hook count and latest version. Hook count across rows should be monotonically non-decreasing | content-match | README.md changelog table vs current state | 2026-02-24 | Changelog table could show stale count or version after updates to other files |
| 4E | Handler Option Completeness | For each handler-level option documented in official docs (type, command, timeout, async, statusMessage, shell, if, asyncRewake, once, matcher), verify HOOKS-README has a corresponding Hook Option subsection or table entry documenting the option's behavior | field-level | hooks-reference + hooks-guide pages vs HOOKS-README Hook Option subsections | 2026-03-28 | The `if` conditional field (v2.1.85) was in official hooks guide but not documented in HOOKS-README — no rule checked handler-level option completeness (Rule 1A only covers per-hook input fields, Rule 4B only checks settings file structure) |

---

## 5. Schema & Hidden Hooks

Rules that verify the settings.json schema against official docs and local repo.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 5A | Schema Hook Names | Locate the Claude Code settings.json JSON schema and extract the `propertyNames` enum from the `hooks` property. Compare the enum entries against: (a) official docs hook list, (b) local repo HOOK_SOUND_MAP keys. Flag hooks in schema but not in docs as "hidden/undocumented". Flag hooks in docs but not in schema as "schema outdated". Flag hooks in schema but not in local repo as "unsupported by project" | cross-file | settings.json schema vs hooks-reference page vs hooks.py HOOK_SOUND_MAP | 2026-03-04 | Elicitation and ElicitationResult were discovered in the schema enum during v2.1.64 InstructionsLoaded addition — no rule existed to detect hidden hooks in the schema |

---

## 6. Process

Meta-rules about the workflow verification process itself.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 6A | Source Credibility Guard | Only flag items as drift if confirmed by official sources (hooks-reference page, hooks-guide page, GitHub changelog). Third-party blog sources may be outdated or wrong — use them for leads only, verify against official docs before flagging | content-match | official docs only | 2026-02-24 | Past runs produced false positives: OpenInEditor hook (2026-02-20), CLAUDE_HOOK_* env vars (2026-02-20), Windows relative path (2026-02-24) — all sourced from blogs, not official docs |

---

## 7. Embedded Count References

Rules that catch stale numeric references embedded in prose text (not in structured headings/tables).

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 7A | HOOKS-README Prose Counts | Grep HOOKS-README for all patterns matching `\d+ hook`, `not all \d+`, `remaining \d+ hook`, `of \d+ hook` and verify each number matches the current total hook count (or the correct derived count, e.g. total - 6 for agent remaining count). These are embedded in prose text that structured count checks (Rule 3B) miss | content-match | current hook count vs all numeric references in HOOKS-README | 2026-04-02 | "Not all 26 hooks" (line 47) and "remaining 10 hooks" (line 186) survived 8+ hook additions because workflow-add-hook only updated structured locations (heading, numbered list) and no verification rule grepped for prose-embedded counts |
| 7B | Not-in-Docs Table Accuracy | For each hook listed in HOOKS-README "Not in Official Docs" table, verify: (a) it is actually absent from official docs (remove if now present), (b) the "(N hooks listed, X excluded)" note in the Setup row matches the actual official docs hook count | content-match | hooks-reference page vs HOOKS-README Not-in-Docs table | 2026-04-02 | PermissionDenied was added to official docs but remained in Not-in-Docs table for 1+ runs; Setup note said "25 hooks listed, Setup and PermissionDenied excluded" when official docs actually listed 26 hooks (only Setup excluded) |
