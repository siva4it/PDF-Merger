# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub repository setup files
- Contributing guidelines
- MIT License
- Setup.py and pyproject.toml for packaging
- Comprehensive .gitignore file

## [1.0.0] - 2024-12-19

### Added
- **Multiple PDF Support**: Merge any number of PDF files (minimum 2)
- **Custom Output Folder**: Specify where to save merged PDFs
- **Automatic Folder Creation**: Creates output folders if they don't exist
- **Smart Input Handling**: Add files incrementally with validation
- **Duplicate File Detection**: Prevents adding the same file multiple times
- **Page Count Reporting**: Shows total pages across all files
- **Detailed Statistics**: File sizes, page counts, and merge information
- **Permission Validation**: Checks write access before merging
- **Comprehensive Error Handling**: Handles various error scenarios gracefully
- **User-Friendly Interface**: Interactive prompts with clear feedback
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Windows Batch Launcher**: Easy-to-use batch file for Windows users
- **Test Script**: Validates installation and functionality
- **Demo Script**: Shows features and usage examples

### Features
- **File Validation**: Checks file existence, PDF format, and corruption
- **Overwrite Protection**: Asks for confirmation before overwriting files
- **Progress Feedback**: Shows which files are being processed
- **Summary Report**: Displays comprehensive merge results
- **Flexible Path Handling**: Supports relative and absolute paths
- **Robust Error Recovery**: Graceful handling of various error conditions

### Technical Details
- Built with Python 3.6+ compatibility
- Uses PyPDF2 library for PDF manipulation
- Follows PEP 8 coding standards
- Comprehensive documentation and examples
- Modular code structure with clear separation of concerns

## [0.1.0] - Initial Development

### Added
- Basic PDF merging functionality
- Support for merging two PDF files
- Simple command-line interface
- Basic error handling 