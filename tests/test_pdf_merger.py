#!/usr/bin/env python3
"""
Test script for PDF Merger functionality
This script tests the import and basic functionality without requiring actual PDF files.
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported."""
    try:
        from PyPDF2 import PdfMerger, PdfReader
        print("✓ PyPDF2 imports successful")
        return True
    except ImportError as e:
        print(f"✗ PyPDF2 import failed: {e}")
        return False

def test_script_import():
    """Test that the main script can be imported."""
    try:
        # Add src directory to path to import the package
        src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src')
        sys.path.insert(0, src_path)
        from pdf_merger import main
        print("✓ PDF merger script imports successful")
        return True
    except ImportError as e:
        print(f"✗ PDF merger script import failed: {e}")
        return False

def test_pdf_merger_creation():
    """Test that PdfMerger can be created."""
    try:
        from PyPDF2 import PdfMerger
        merger = PdfMerger()
        merger.close()
        print("✓ PdfMerger creation successful")
        return True
    except Exception as e:
        print(f"✗ PdfMerger creation failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing PDF Merger Setup...")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_script_import,
        test_pdf_merger_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! The PDF merger is ready to use.")
        print("\nTo run the PDF merger:")
        print("  python -m src.pdf_merger")
        print("\nAlternative methods:")
        print("  scripts\\run_pdf_merger.bat  (Windows)")
        print("  python -c \"import sys; sys.path.insert(0, 'src'); from pdf_merger import main; main()\"")
    else:
        print("✗ Some tests failed. Please check the error messages above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 