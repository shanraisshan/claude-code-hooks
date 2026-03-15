#!/bin/bash
# Claude Code Hooks Lifecycle Demo - Start Script

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "Starting Claude Code Hooks Lifecycle Demo..."
echo ""

# Start the server in the background
python3 server.py &
SERVER_PID=$!

# Wait for server to start
sleep 1

# Check if server started successfully
if ! kill -0 $SERVER_PID 2>/dev/null; then
    echo "ERROR: Server failed to start."
    exit 1
fi

# Open browser (macOS)
if command -v open &>/dev/null; then
    open "http://localhost:3456"
elif command -v xdg-open &>/dev/null; then
    xdg-open "http://localhost:3456"
fi

echo ""
echo "Now open another terminal and run:"
echo "  cd $SCRIPT_DIR"
echo "  claude"
echo ""
echo "Press Ctrl+C to stop the server."

# Wait for server process, forward Ctrl+C
trap "kill $SERVER_PID 2>/dev/null; exit 0" INT TERM
wait $SERVER_PID
