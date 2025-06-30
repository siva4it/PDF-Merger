#!/usr/bin/env python3
"""
PDF Merger Script

This script takes multiple PDF file paths as input and merges them into a single PDF file.
It uses the PyPDF2 library and includes comprehensive error handling.
"""

import os
import sys
from pathlib import Path

try:
    from PyPDF2 import PdfMerger, PdfReader
except ImportError:
    print("Error: PyPDF2 library is not installed.")
    print("Please install it using: pip install PyPDF2")
    sys.exit(1)


def validate_pdf_file(file_path):
    """
    Validate that a file exists and is a valid PDF.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        bool: True if file is valid, False otherwise
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False
    
    if not file_path.lower().endswith('.pdf'):
        print(f"Error: File '{file_path}' is not a PDF file.")
        return False
    
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            if len(reader.pages) == 0:
                print(f"Error: File '{file_path}' appears to be empty or corrupted.")
                return False
        return True
    except Exception as e:
        print(f"Error reading PDF file '{file_path}': {str(e)}")
        return False


def validate_and_create_folder(folder_path):
    """
    Validate and create output folder if it doesn't exist.
    
    Args:
        folder_path (str): Path to the folder
        
    Returns:
        bool: True if folder is valid/created, False otherwise
    """
    if not folder_path.strip():
        return True  # Empty path means current directory
    
    try:
        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✓ Created output folder: '{folder_path}'")
        else:
            # Check if it's actually a directory
            if not os.path.isdir(folder_path):
                print(f"Error: '{folder_path}' exists but is not a directory.")
                return False
            print(f"✓ Using existing folder: '{folder_path}'")
        
        # Check write permissions
        test_file = os.path.join(folder_path, "test_write.tmp")
        try:
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
        except Exception as e:
            print(f"Error: No write permission in folder '{folder_path}': {str(e)}")
            return False
        
        return True
    except Exception as e:
        print(f"Error creating/validating folder '{folder_path}': {str(e)}")
        return False


def get_pdf_files():
    """
    Get multiple PDF file paths from user input with validation.
    
    Returns:
        list: List of valid PDF file paths
    """
    pdf_files = []
    used_files = set()
    
    print("Enter the paths to PDF files you want to merge.")
    print("Press Enter without a filename when you're done adding files.\n")
    
    while True:
        file_path = input(f"Enter path to PDF file #{len(pdf_files) + 1} (or press Enter to finish): ").strip()
        
        if not file_path:
            if len(pdf_files) < 2:
                print("Error: You need at least 2 PDF files to merge.")
                continue
            break
        
        # Check for duplicate files
        if file_path in used_files:
            print(f"Error: File '{file_path}' has already been added.")
            continue
        
        if validate_pdf_file(file_path):
            pdf_files.append(file_path)
            used_files.add(file_path)
            print(f"✓ Added: {file_path}")
        else:
            print("Please try again with a valid PDF file.")
    
    return pdf_files


def get_output_folder():
    """
    Get the output folder from user input with validation.
    
    Returns:
        str: Valid output folder path (empty string for current directory)
    """
    while True:
        folder_path = input("Enter output folder path (press Enter for current directory): ").strip()
        
        if validate_and_create_folder(folder_path):
            return folder_path
        else:
            print("Please try again with a valid folder path.")


def get_output_filename():
    """
    Get the output filename from user input with validation.
    
    Returns:
        str: Valid output filename
    """
    while True:
        output_name = input("Enter the name for the merged PDF file (e.g., merged.pdf): ").strip()
        
        if not output_name:
            print("Error: Output filename cannot be empty.")
            continue
        
        if not output_name.lower().endswith('.pdf'):
            output_name += '.pdf'
        
        return output_name


def get_full_output_path(output_folder, output_filename):
    """
    Combine output folder and filename to create full output path.
    
    Args:
        output_folder (str): Output folder path
        output_filename (str): Output filename
        
    Returns:
        str: Full output path
    """
    if output_folder:
        return os.path.join(output_folder, output_filename)
    else:
        return output_filename


def check_file_exists(full_path):
    """
    Check if output file already exists and ask for overwrite confirmation.
    
    Args:
        full_path (str): Full path to the output file
        
    Returns:
        bool: True if file doesn't exist or user wants to overwrite
    """
    if os.path.exists(full_path):
        overwrite = input(f"File '{full_path}' already exists. Overwrite? (y/n): ").strip().lower()
        return overwrite in ['y', 'yes']
    return True


def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into a single PDF.
    
    Args:
        pdf_files (list): List of PDF file paths to merge
        output_path (str): Path for the output merged PDF file
        
    Returns:
        bool: True if merge was successful, False otherwise
    """
    try:
        merger = PdfMerger()
        
        # Add each PDF file
        for i, pdf_path in enumerate(pdf_files, 1):
            print(f"Adding file #{i}: '{pdf_path}'...")
            merger.append(pdf_path)
        
        # Write the merged PDF to output file
        print(f"Creating merged PDF: '{output_path}'...")
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        
        merger.close()
        return True
        
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False


def calculate_total_pages(pdf_files):
    """
    Calculate the total number of pages across all PDF files.
    
    Args:
        pdf_files (list): List of PDF file paths
        
    Returns:
        int: Total number of pages
    """
    total_pages = 0
    for pdf_path in pdf_files:
        try:
            with open(pdf_path, 'rb') as file:
                reader = PdfReader(file)
                total_pages += len(reader.pages)
        except:
            pass
    return total_pages


def main():
    """
    Main function to run the PDF merger script.
    """
    print("=" * 50)
    print("PDF Merger Tool")
    print("=" * 50)
    print("This tool merges multiple PDF files into a single PDF file.\n")
    
    # Get PDF file paths
    pdf_files = get_pdf_files()
    
    print(f"\nFiles to merge: {len(pdf_files)}")
    for i, file_path in enumerate(pdf_files, 1):
        print(f"  {i}. {file_path}")
    
    # Get output folder
    print("\n" + "-" * 30)
    print("Output Settings")
    print("-" * 30)
    output_folder = get_output_folder()
    
    # Get output filename
    output_filename = get_output_filename()
    
    # Create full output path
    full_output_path = get_full_output_path(output_folder, output_filename)
    
    # Check if file exists and ask for overwrite
    if not check_file_exists(full_output_path):
        print("Operation cancelled.")
        sys.exit(0)
    
    print(f"\nOutput will be saved to: '{full_output_path}'")
    
    print("\n" + "=" * 50)
    print("Merging PDFs...")
    print("=" * 50)
    
    # Perform the merge
    if merge_pdfs(pdf_files, full_output_path):
        print("\n" + "=" * 50)
        print("SUCCESS!")
        print("=" * 50)
        print(f"The PDFs have been successfully merged into: '{full_output_path}'")
        
        # Show file information
        try:
            total_size = 0
            total_pages = calculate_total_pages(pdf_files)
            
            print(f"\nSummary:")
            print(f"  Number of files merged: {len(pdf_files)}")
            print(f"  Total pages: {total_pages}")
            print(f"  Output location: '{full_output_path}'")
            
            print(f"\nFile sizes:")
            for i, pdf_path in enumerate(pdf_files, 1):
                size = os.path.getsize(pdf_path) / (1024 * 1024)  # MB
                total_size += size
                print(f"  File #{i}: {size:.2f} MB")
            
            output_size = os.path.getsize(full_output_path) / (1024 * 1024)  # MB
            print(f"  Merged PDF: {output_size:.2f} MB")
            print(f"  Total input size: {total_size:.2f} MB")
            
        except:
            pass
    else:
        print("\n" + "=" * 50)
        print("FAILED!")
        print("=" * 50)
        print("The PDF merge operation failed. Please check the error messages above.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1) 