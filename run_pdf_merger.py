#!/usr/bin/env python3
"""
PDF Merger Tool Launcher
Simple launcher script that can be run from the project root directory.
"""

import sys
import os

# Add src directory to Python path
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.insert(0, src_path)

# Import and run the main function
from pdf_merger import main

if __name__ == "__main__":
    main() 