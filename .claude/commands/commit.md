---
description: Commit changes with auto-generated message showing command context, timestamp, and change count
argument-hint: [command name that produced these changes, e.g. workflows:workflow-changelog]
---

# Commit

Create a git commit with an auto-generated message. The first line is a summary, followed by a numbered list of the actions/changes that were executed.

## Format

```
[/command-name][DD-Mon-YY HH:MM AM/PM] N changes

1. First change description
2. Second change description
...
```

**"N changes" refers to the number of actions/changes that were executed during the session** — NOT the number of git file changes. Look back through the conversation to find the actions that were taken (e.g., from a workflows:workflow-changelog report's action items, or from a workflows:workflow-add-hook workflow's steps).

## Steps

1. **Get the command name** from `$ARGUMENTS`. If empty, ask the user what command or task produced these changes.

2. **Get the current timestamp** by running:
   ```
   date "+%d-%b-%y %I:%M %p"
   ```

3. **Read `changelog/changelog.md`** to get the latest entry's priority actions table. Use the items in that table as the list of changes. If the command name is not `workflows:workflow-changelog`, fall back to reviewing the conversation to identify actions.

4. **Run `git status --short`** to see which files were changed.

5. **Show the user** the proposed commit message (title + numbered list) and the files to stage. Ask for confirmation before committing.

6. **Stage and commit — one commit per file**:
   - Create a **separate commit for each changed file** (per CLAUDE.md Git Commit Rules)
   - Each commit message uses the same title line but includes only the change descriptions relevant to that file
   - Stage one file at a time with `git add <file>`, then commit using a HEREDOC
   - Format for each per-file commit:
     ```
     [/command-name][DD-Mon-YY HH:MM AM/PM] N changes

     1. Change description relevant to this file
     2. Another change relevant to this file
     ```
   - If a single change touches multiple files, include that change description in each relevant file's commit

## Example

If `/commit workflows:workflow-changelog` is run after a session that changed 3 files with 4 total actions:

**Commit 1** (`git add README.md`):
```
[/workflows:workflow-changelog][20-Feb-26 08:14 PM] 4 changes

1. Updated version badge to v2.1.90
```

**Commit 2** (`git add .claude/hooks/scripts/hooks.py`):
```
[/workflows:workflow-changelog][20-Feb-26 08:14 PM] 4 changes

1. Added stop_hook_active to Stop & SubagentStop Options
2. Added source to ConfigChange & SessionStart Options
```

**Commit 3** (`git add changelog/changelog.md`):
```
[/workflows:workflow-changelog][20-Feb-26 08:14 PM] 4 changes

1. Appended v2.1.90 changelog entry
```

## Rules

1. **Always show the proposed commits** (per-file messages + file list) before committing — never auto-commit
2. **One commit per file** — never bundle multiple files into a single commit
3. **Never stage sensitive files** (.env, credentials, secrets)
4. **Use specific file paths** when staging — not `git add -A` or `git add .`
5. **Do not push** unless the user explicitly asks
6. **"N changes" in the title = total actions executed** across the entire session, not per-file
7. Keep each change description short (under 80 chars)
