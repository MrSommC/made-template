#!/bin/bash

set -e

# Install required Python packages
pip install -r requirements.txt

# Run tests
echo "Running unit tests..."
python3 unit_tests.py


