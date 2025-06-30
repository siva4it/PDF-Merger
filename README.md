# PDF Merger Tool

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pdf-merger-tool.svg)](https://badge.fury.io/py/pdf-merger-tool)
[![GitHub release](https://img.shields.io/github/release/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/releases)

A professional, feature-rich Python tool for merging multiple PDF files into a single PDF with advanced features like custom output folders, duplicate detection, and comprehensive error handling.

## ✨ Features

- **Multiple PDF Support**: Merge any number of PDF files (minimum 2)
- **Smart Input Handling**: Add files one by one with validation
- **Duplicate Detection**: Automatically detects and prevents duplicate files
- **Page Count Reporting**: Shows total pages and file sizes
- **Custom Output Folders**: Specify any output directory with automatic creation
- **Permission Validation**: Checks write permissions before merging
- **Professional Error Handling**: Comprehensive error messages and recovery
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- PyPDF2 library

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/siva4it/PDF-Merger.git
   cd PDF-Merger
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool**
   ```bash
   python run_pdf_merger.py
   ```

## 📖 Usage

### Running from Command Line

**Method 1: Simple Launcher Script (Recommended)**
```cmd
python run_pdf_merger.py
```

**Method 2: Windows Batch File**
```cmd
run_pdf_merger.bat
```

**Method 3: As a Python Module (from project root)**
```cmd
python -m src.pdf_merger
```

**Method 4: Direct Import (from project root)**
```cmd
python -c "import sys; sys.path.insert(0, 'src'); from pdf_merger import main; main()"
```

### Interactive Usage

1. **Start the tool**
   ```bash
   python run_pdf_merger.py
   ```

2. **Add PDF files**
   - Enter the path to each PDF file
   - Press Enter without a filename when done
   - Minimum 2 files required

3. **Specify output settings**
   - Enter output folder path (optional, press Enter for current directory)
   - Provide output filename

4. **Review and confirm**
   - Check the summary of files to merge
   - Confirm the merge operation

### Example Workflow

```
==================================================
PDF Merger Tool
==================================================

Enter path to PDF file #1: document1.pdf
✓ Added: document1.pdf (15 pages, 2.45 MB)

Enter path to PDF file #2: document2.pdf
✓ Added: document2.pdf (12 pages, 1.78 MB)

Enter path to PDF file #3: [press Enter]

Files to merge: 2
  1. document1.pdf (15 pages)
  2. document2.pdf (12 pages)

Enter output folder path (press Enter for current directory): merged_pdfs
✓ Created output folder: 'merged_pdfs'

Enter the name for the merged PDF file: combined.pdf

Output will be saved to: 'merged_pdfs/combined.pdf'

Merging PDFs...
✓ Successfully merged 2 files into 'merged_pdfs/combined.pdf'
✓ Total pages: 27
✓ File size: 4.23 MB
```

## 🛠️ Development

### Project Structure
```
PDF-Merger/
├── run_pdf_merger.py          # Main launcher script
├── run_pdf_merger.bat         # Windows batch launcher
├── src/
│   └── pdf_merger/
│       ├── __init__.py
│       ├── __main__.py
│       └── pdf_merger.py
├── tests/
│   └── test_pdf_merger.py
├── examples/
│   └── demo_multiple_pdfs.py
├── docs/
│   ├── QUICK_START.md
│   └── GITHUB_SETUP.md
├── scripts/
│   └── run_pdf_merger.bat
├── setup.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Running Tests
```bash
python tests/test_pdf_merger.py
```

### Development Setup
```bash
# Clone and setup
git clone https://github.com/siva4it/PDF-Merger.git
cd PDF-Merger
pip install -r requirements.txt

# Run tests
python tests/test_pdf_merger.py

# Run the tool
python run_pdf_merger.py
```

## 📋 Requirements

- **Python**: 3.6 or higher
- **PyPDF2**: >=3.0.0
- **Operating System**: Windows, macOS, or Linux

## 🔧 Installation Options

### From Source
```bash
git clone https://github.com/siva4it/PDF-Merger.git
cd PDF-Merger
pip install -r requirements.txt
```

### From PyPI (Future)
```bash
pip install pdf-merger-tool
```

### Development Installation
```bash
git clone https://github.com/siva4it/PDF-Merger.git
cd PDF-Merger
pip install -e .
```

## 🎯 Key Features Explained

### Multiple File Support
- Add unlimited PDF files (minimum 2)
- Smart input validation
- Duplicate file detection
- File existence verification

### Custom Output Folders
- Specify any output directory
- Automatic folder creation
- Permission validation
- Full path confirmation

### Professional Error Handling
- Comprehensive error messages
- Graceful failure recovery
- File validation
- Permission checking

### Progress Reporting
- Real-time status updates
- File size and page count display
- Merge progress indication
- Success confirmation

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues and Support

- **Bug Reports**: [GitHub Issues](https://github.com/siva4it/PDF-Merger/issues)
- **Feature Requests**: [GitHub Issues](https://github.com/siva4it/PDF-Merger/issues)
- **Documentation**: [GitHub Wiki](https://github.com/siva4it/PDF-Merger/wiki)

## 📈 Roadmap

- [ ] GUI interface
- [ ] Batch processing
- [ ] PDF compression options
- [ ] Page range selection
- [ ] Password protection support
- [ ] Cloud storage integration

## 🙏 Acknowledgments

- Built with [PyPDF2](https://pypdf2.readthedocs.io/)
- Inspired by the need for a simple, powerful PDF merging solution
- Thanks to all contributors and users

---

**Made with ❤️ for the Python community**

[![GitHub stars](https://img.shields.io/github/stars/siva4it/PDF-Merger.svg?style=social&label=Star)](https://github.com/siva4it/PDF-Merger)
[![GitHub forks](https://img.shields.io/github/forks/siva4it/PDF-Merger.svg?style=social&label=Fork)](https://github.com/siva4it/PDF-Merger)
[![GitHub issues](https://img.shields.io/github/issues/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/issues) 