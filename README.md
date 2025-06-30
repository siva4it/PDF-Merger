# PDF Merger Tool

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0.0+-green.svg)](https://pypi.org/project/PyPDF2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/network)
[![GitHub issues](https://img.shields.io/github/issues/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/issues)

A professional, feature-rich Python tool for merging multiple PDF files into a single PDF with advanced error handling and user-friendly interface.

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
   python -m src.pdf_merger
   ```

## 📖 Usage

### Running from Command Line

**Method 1: As a Python Module (Recommended)**
```cmd
python -m src.pdf_merger
```

**Method 2: Using the Windows Batch File**
```cmd
scripts\run_pdf_merger.bat
```

**Method 3: Direct Import**
```cmd
python -c "import sys; sys.path.insert(0, 'src'); from pdf_merger import main; main()"
```

### Interactive Usage

1. **Start the tool**
   ```bash
   python -m src.pdf_merger
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

## 📁 Project Structure

```
PDF-Merger/
├── src/
│   └── pdf_merger/
│       ├── __init__.py         # Package metadata and main import
│       └── pdf_merger.py       # Main application logic
├── tests/
│   └── test_pdf_merger.py      # Test suite
├── examples/
│   └── demo_multiple_pdfs.py   # Example/demo script
├── scripts/
│   └── run_pdf_merger.bat      # Windows launcher
├── docs/
│   ├── README.md
│   ├── QUICK_START.md
│   └── GITHUB_SETUP.md
├── .github/
│   ├── workflows/
│   │   └── python-app.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── pull_request_template.md
├── requirements.txt
├── setup.py
├── pyproject.toml
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── .gitignore
└── README.md                   # Project overview and navigation
```

## 📖 Documentation

- **[📚 Full Documentation](docs/README.md)** - Complete user guide and API reference
- **[⚡ Quick Start Guide](docs/QUICK_START.md)** - Get up and running in minutes
- **[🔧 GitHub Setup](docs/GITHUB_SETUP.md)** - Repository setup instructions

## 🧪 Testing

```bash
# Run the test suite
python tests/test_pdf_merger.py

# Run examples
python examples/demo_multiple_pdfs.py
```

## 🛠️ Development

```bash
# Install in development mode
pip install -e .

# Run with module syntax
python -m src.pdf_merger

# Run tests
python -m pytest tests/
```

## 📦 Installation

### From Source
```bash
git clone https://github.com/siva4it/PDF-Merger.git
cd PDF-Merger
pip install -r requirements.txt
```

### Using pip (when published)
```bash
pip install pdf-merger-tool
pdf-merger
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Support

- **Bug Reports**: [Create an issue](https://github.com/siva4it/PDF-Merger/issues/new?template=bug_report.md)
- **Feature Requests**: [Suggest a feature](https://github.com/siva4it/PDF-Merger/issues/new?template=feature_request.md)
- **Documentation**: [View docs](docs/README.md)

## 📊 Project Status

- **Version**: 1.0.0
- **Status**: Production Ready
- **Python Support**: 3.6+
- **Platforms**: Windows, macOS, Linux

---

⭐ **Star this repository** if you find it helpful!

🔗 **Links**: [Documentation](docs/README.md) | [Issues](https://github.com/siva4it/PDF-Merger/issues) | [Releases](https://github.com/siva4it/PDF-Merger/releases) 