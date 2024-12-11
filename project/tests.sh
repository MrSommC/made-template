#!/bin/bash

set -e

pip install -r project/requirements.txt

# Run tests
echo "Running all tests (unit and system-level)..."
python3 project/unit_tests.py
