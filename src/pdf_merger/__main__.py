#!/usr/bin/env python3
"""
Entry point for running the PDF Merger Tool as a module.
This allows the package to be executed with: python -m src.pdf_merger
"""

from .pdf_merger import main

if __name__ == "__main__":
    main() 