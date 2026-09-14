#!/bin/bash
set -e

PROJECT_DIR="/Users/ashutoshrao/Desktop/Road Traffic AI Project"
cd "$PROJECT_DIR"

export DYLD_LIBRARY_PATH="/opt/homebrew/opt/expat/lib:${DYLD_LIBRARY_PATH}"
export OPENCV_FFMPEG_CAPTURE_OPTIONS="rtsp_transport;tcp"

echo ""
echo "  ┌────────────────────────────────────────────────────┐"
echo "  │  🛡️  SENTINEL — Gujarat Police Innovation 2026    │"
echo "  │  Integrated Video Management & Analytics Platform  │"
echo "  └────────────────────────────────────────────────────┘"
echo ""

if [ ! -d ".venv" ]; then
    echo "⚙️  Creating virtual environment..."
    python3 -m venv .venv
fi

echo "🚀 Starting SENTINEL Command Centre..."
echo "👉 Open your browser at http://localhost:8000"
echo ""

.venv/bin/python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
