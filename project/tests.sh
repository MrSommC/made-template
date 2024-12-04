#!/bin/bash

set -e

pip install -r requirements.txt

# Run tests
echo "Running all tests (unit and system-level)..."
python3 unit_tests.py
