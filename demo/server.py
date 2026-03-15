#!/usr/bin/env python3
"""
HTTP server for the Claude Code Hooks Lifecycle Demo.
Serves the visualization page and hook state API.

Usage: python3 server.py [--port PORT]
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys
import argparse
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, ".claude", "hooks", "state", "hook-state.json")
HTML_FILE = os.path.join(BASE_DIR, "hooks-lifecycle.html")

ALL_HOOKS = [
    "SessionStart",
    "UserPromptSubmit",
    "PreToolUse",
    "PermissionRequest",
    "PostToolUse",
    "PostToolUseFailure",
    "Notification",
    "Stop",
    "SubagentStart",
    "SubagentStop",
    "PreCompact",
    "PostCompact",
    "SessionEnd",
    "Setup",
    "TeammateIdle",
    "TaskCompleted",
    "ConfigChange",
    "WorktreeCreate",
    "WorktreeRemove",
    "InstructionsLoaded",
    "Elicitation",
    "ElicitationResult",
]


def create_initial_state():
    """Return a fresh state dict with all 22 hooks inactive."""
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


def read_state():
    """Read the current hook state from disk."""
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return create_initial_state()


def write_state(state):
    """Write state to disk (atomic)."""
    import tempfile

    state_dir = os.path.dirname(STATE_FILE)
    os.makedirs(state_dir, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(dir=state_dir, suffix=".json")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(state, f, indent=2)
        os.replace(temp_path, STATE_FILE)
    except Exception:
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise


def reset_state():
    """Reset all hooks to inactive."""
    state = create_initial_state()
    write_state(state)
    return state


class DemoHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the lifecycle demo."""

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.serve_html()
        elif self.path == "/api/state":
            self.serve_state()
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == "/api/reset":
            self.handle_reset()
        else:
            self.send_error(404, "Not Found")

    def serve_html(self):
        """Serve the hooks-lifecycle.html file."""
        try:
            with open(HTML_FILE, "r", encoding="utf-8") as f:
                content = f.read()
            body = content.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self.send_error(
                404,
                "hooks-lifecycle.html not found. "
                "Make sure it exists in the demo/ directory.",
            )

    def serve_state(self):
        """Serve the current hook state as JSON."""
        state = read_state()
        body = json.dumps(state).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-cache, no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def handle_reset(self):
        """Reset all hooks to inactive."""
        reset_state()
        body = json.dumps({"status": "ok"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        """Suppress per-request logging to keep output clean."""
        pass


def main():
    parser = argparse.ArgumentParser(description="Claude Code Hooks Lifecycle Demo Server")
    parser.add_argument("--port", type=int, default=3456, help="Port to listen on (default: 3456)")
    args = parser.parse_args()

    port = args.port

    # Ensure state directory and initial state file exist
    state_dir = os.path.dirname(STATE_FILE)
    os.makedirs(state_dir, exist_ok=True)
    if not os.path.exists(STATE_FILE):
        write_state(create_initial_state())

    server = HTTPServer(("", port), DemoHandler)
    server.socket.setsockopt(__import__('socket').SOL_SOCKET, __import__('socket').SO_REUSEADDR, 1)

    print("==================================")
    print("  Claude Code Hooks Lifecycle Demo")
    print("==================================")
    print(f"  Server: http://localhost:{port}")
    print("")
    print("  Instructions:")
    print(f"  1. Open http://localhost:{port} in your browser")
    print("  2. Open another terminal")
    print("  3. cd to the demo/ directory")
    print("  4. Run: claude")
    print("  5. Watch hooks light up!")
    print("")
    print("  Press Ctrl+C to stop the server.")
    print("==================================")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()
        sys.exit(0)


if __name__ == "__main__":
    main()
