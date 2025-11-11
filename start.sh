#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

if ! python -c "import textual" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

python3 src/tui.py

deactivate
