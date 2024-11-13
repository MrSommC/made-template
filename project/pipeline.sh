#!/bin/bash

# Ensure the script stops if any command fails
set -e

# Install required packages
pip install -r requirements.txt

# Run the main pipeline script
python3 pipeline.py
