# PDF Merger Tool

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0.0+-green.svg)](https://pypi.org/project/PyPDF2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/your-username/PDF-Merger.svg)](https://github.com/your-username/PDF-Merger/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/PDF-Merger.svg)](https://github.com/your-username/PDF-Merger/network)
[![GitHub issues](https://img.shields.io/github/issues/your-username/PDF-Merger.svg)](https://github.com/your-username/PDF-Merger/issues)

A simple and powerful Python script that merges multiple PDF files into a single PDF file using the PyPDF2 library.

## ✨ Features

- **Merge multiple PDF files** into one (minimum 2 files)
- **Custom output folder** support with automatic creation
- **Comprehensive error handling** and validation
- **File validation** (existence, PDF format, corruption check)
- **User-friendly interactive prompts** with clear feedback
- **File size and page count reporting** with detailed statistics
- **Overwrite protection** for existing files
- **Duplicate file detection** to prevent errors
- **Cross-platform support** (Windows, macOS, Linux)
- **Windows batch launcher** for easy execution

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/PDF-Merger.git
   cd PDF-Merger
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**
   ```bash
   python pdf_merger.py
   ```

### Alternative Installation Methods

**Using pip (if published to PyPI):**
```bash
pip install pdf-merger-tool
pdf-merger
```

**Windows users:**
- Double-click `run_pdf_merger.bat`

## 📖 Usage

The script will prompt you for:
1. Multiple PDF file paths (press Enter when done adding files)
2. Output folder path (optional - press Enter for current directory)
3. Name for the merged output file

### Example Usage

```
==================================================
PDF Merger Tool
==================================================
This tool merges multiple PDF files into a single PDF file.

Enter the paths to PDF files you want to merge.
Press Enter without a filename when you're done adding files.

Enter path to PDF file #1 (or press Enter to finish): document1.pdf
✓ Added: document1.pdf
Enter path to PDF file #2 (or press Enter to finish): document2.pdf
✓ Added: document2.pdf
Enter path to PDF file #3 (or press Enter to finish): document3.pdf
✓ Added: document3.pdf
Enter path to PDF file #4 (or press Enter to finish): 

Files to merge: 3
  1. document1.pdf
  2. document2.pdf
  3. document3.pdf

------------------------------
Output Settings
------------------------------
Enter output folder path (press Enter for current directory): merged_pdfs
✓ Created output folder: 'merged_pdfs'
Enter the name for the merged PDF file (e.g., merged.pdf): combined.pdf

Output will be saved to: 'merged_pdfs/combined.pdf'

==================================================
Merging PDFs...
==================================================
Adding file #1: 'document1.pdf'...
Adding file #2: 'document2.pdf'...
Adding file #3: 'document3.pdf'...
Creating merged PDF: 'merged_pdfs/combined.pdf'...

==================================================
SUCCESS!
==================================================
The PDFs have been successfully merged into: 'merged_pdfs/combined.pdf'

Summary:
  Number of files merged: 3
  Total pages: 45
  Output location: 'merged_pdfs/combined.pdf'

File sizes:
  File #1: 2.45 MB
  File #2: 1.78 MB
  File #3: 3.12 MB
  Merged PDF: 7.35 MB
  Total input size: 7.35 MB
```

## 📂 Output Folder Features

### **Custom Output Location**
- Specify any folder path for the merged PDF
- Press Enter to use the current directory
- Supports relative and absolute paths

### **Automatic Folder Creation**
- Creates output folders if they don't exist
- Validates folder permissions before merging
- Provides feedback on folder creation/usage

### **Smart Path Handling**
- Combines folder path and filename automatically
- Handles path separators for different operating systems
- Validates write permissions in the target folder

## 🛡️ Error Handling

The script handles various error scenarios:

- **Missing files**: Checks if input files exist
- **Invalid PDFs**: Validates that files are actual PDFs and not corrupted
- **Duplicate files**: Prevents adding the same file multiple times
- **Minimum files**: Ensures at least 2 PDF files are provided
- **Overwrite protection**: Asks for confirmation before overwriting existing files
- **Library errors**: Handles PyPDF2 import and usage errors
- **Folder permissions**: Validates write access to output folders
- **Invalid folders**: Checks if specified paths are valid directories

## 📋 Requirements

- Python 3.6+
- PyPDF2 library

## 📁 Project Structure

```
PDF-Merger/
├── pdf_merger.py              # Main script
├── requirements.txt           # Dependencies
├── setup.py                  # Package setup
├── pyproject.toml            # Modern Python packaging
├── run_pdf_merger.bat        # Windows launcher
├── test_pdf_merger.py        # Test script
├── demo_multiple_pdfs.py     # Demo script
├── README.md                 # This file
├── QUICK_START.md            # Quick start guide
├── CONTRIBUTING.md           # Contributing guidelines
├── LICENSE                   # MIT License
├── CHANGELOG.md              # Version history
├── .gitignore                # Git ignore rules
└── .github/                  # GitHub templates and workflows
    ├── workflows/
    │   └── python-app.yml    # CI/CD pipeline
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md     # Bug report template
    │   └── feature_request.md # Feature request template
    └── pull_request_template.md # PR template
```

## 🧪 Testing

Run the test script to verify everything works:

```bash
python test_pdf_merger.py
```

## 📝 Notes

- The script automatically adds `.pdf` extension if not provided
- File paths can be relative or absolute
- The merged PDF maintains the original page order (files are merged in the order they were added)
- Large PDF files may take some time to process
- You can merge any number of PDF files (minimum 2)
- The script shows detailed information including total pages and file sizes
- Output folders are created automatically if they don't exist
- Write permissions are validated before starting the merge process

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Reporting Issues

If you encounter any issues, please:

1. Check the [existing issues](https://github.com/your-username/PDF-Merger/issues)
2. Create a new issue with a clear description
3. Include your operating system and Python version
4. Provide steps to reproduce the problem

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyPDF2](https://pypi.org/project/PyPDF2/) - The PDF manipulation library
- All contributors who help improve this tool

## 📊 Project Status

- **Version**: 1.0.0
- **Status**: Production Ready
- **Python Support**: 3.6+
- **Platforms**: Windows, macOS, Linux

---

⭐ If you find this project helpful, please give it a star on GitHub! 