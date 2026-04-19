#!/usr/bin/env python3
"""
Demo Hook Handler - plays sounds AND updates lifecycle visualization state.
Handles all 27 Claude Code hooks.
"""

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path


HOOK_SOUND_MAP = {
    "PreToolUse": "pretooluse",
    "PermissionRequest": "permissionrequest",
    "PostToolUse": "posttooluse",
    "PostToolUseFailure": "posttoolusefailure",
    "UserPromptSubmit": "userpromptsubmit",
    "Notification": "notification",
    "Stop": "stop",
    "SubagentStart": "subagentstart",
    "SubagentStop": "subagentstop",
    "PreCompact": "precompact",
    "PostCompact": "postcompact",
    "SessionStart": "sessionstart",
    "SessionEnd": "sessionend",
    "Setup": "setup",
    "TeammateIdle": "teammateidle",
    "TaskCreated": "taskcreated",
    "TaskCompleted": "taskcompleted",
    "ConfigChange": "configchange",
    "WorktreeCreate": "worktreecreate",
    "WorktreeRemove": "worktreeremove",
    "InstructionsLoaded": "instructionsloaded",
    "Elicitation": "elicitation",
    "ElicitationResult": "elicitationresult",
    "StopFailure": "stopfailure",
    "CwdChanged": "cwdchanged",
    "FileChanged": "filechanged",
    "PermissionDenied": "permissiondenied",
}

ALL_HOOKS = list(HOOK_SOUND_MAP.keys())


def get_sounds_base():
    """Resolve path to the PARENT project's sounds directory."""
    script_dir = Path(__file__).resolve().parent   # demo/.claude/hooks/scripts/
    hooks_dir = script_dir.parent                  # demo/.claude/hooks/
    claude_dir = hooks_dir.parent                  # demo/.claude/
    demo_dir = claude_dir.parent                   # demo/
    project_root = demo_dir.parent                 # project root
    sounds_base = project_root / ".claude" / "hooks" / "sounds"
    # Debug: uncomment to verify path resolution
    # print(f"[debug] sounds_base = {sounds_base}", file=sys.stderr)
    return sounds_base


def get_state_dir():
    """Resolve path to the state directory."""
    script_dir = Path(__file__).resolve().parent   # demo/.claude/hooks/scripts/
    state_dir = script_dir.parent / "state"        # demo/.claude/hooks/state/
    return state_dir


def create_initial_state():
    """Return a fresh state dict with all 27 hooks inactive."""
    hooks = {}
    for hook_name in ALL_HOOKS:
        hooks[hook_name] = {
            "active": False,
            "last_fired": None,
            "fire_count": 0,
        }
    return {
        "hooks": hooks,
        "last_updated": None,
    }


def play_sound(sound_folder_name):
    """Play the sound file for a given hook (macOS afplay)."""
    sounds_dir = get_sounds_base() / sound_folder_name
    for ext in [".wav", ".mp3"]:
        file_path = sounds_dir / f"{sound_folder_name}{ext}"
        if file_path.exists():
            subprocess.Popen(
                ["afplay", str(file_path)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            return True
    return False


def update_state(hook_name):
    """Update the state file to mark a hook as active (file-locked read-modify-write)."""
    import fcntl

    state_dir = get_state_dir()
    state_dir.mkdir(parents=True, exist_ok=True)
    state_file = state_dir / "hook-state.json"
    lock_file = state_dir / ".hook-state.lock"

    # Use a lock file to prevent race conditions between concurrent hook fires
    with open(lock_file, "w") as lf:
        fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
        try:
            # Read current state under lock
            try:
                with open(state_file, "r") as f:
                    state = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                state = create_initial_state()

            # Backfill any hooks added after the state file was created
            for h in ALL_HOOKS:
                if h not in state.get("hooks", {}):
                    state.setdefault("hooks", {})[h] = {
                        "active": False,
                        "last_fired": None,
                        "fire_count": 0,
                    }

            # Update the hook
            if hook_name in state["hooks"]:
                state["hooks"][hook_name]["active"] = True
                state["hooks"][hook_name]["last_fired"] = time.time()
                state["hooks"][hook_name]["fire_count"] = (
                    state["hooks"][hook_name].get("fire_count", 0) + 1
                )
            state["last_updated"] = time.time()

            # Write state under lock
            fd, temp_path = tempfile.mkstemp(dir=str(state_dir), suffix=".json")
            try:
                with os.fdopen(fd, "w") as f:
                    json.dump(state, f, indent=2)
                os.replace(temp_path, str(state_file))
            except Exception:
                try:
                    os.unlink(temp_path)
                except OSError:
                    pass
                raise
        finally:
            fcntl.flock(lf.fileno(), fcntl.LOCK_UN)


def main():
    try:
        stdin_content = sys.stdin.read().strip()
        if not stdin_content:
            sys.exit(0)

        input_data = json.loads(stdin_content)
        event_name = input_data.get("hook_event_name", "")

        if not event_name:
            sys.exit(0)

        # Debug: uncomment to trace hook events
        # print(f"[demo-hooks] event={event_name}", file=sys.stderr)

        # Update visualization state
        update_state(event_name)

        # Play sound
        sound_folder = HOOK_SOUND_MAP.get(event_name)
        if sound_folder:
            play_sound(sound_folder)

        # Output valid JSON so blocking hooks (WorktreeCreate, etc.) succeed
        print("{}")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
