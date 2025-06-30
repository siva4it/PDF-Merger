# PDF Merger Tool

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0.0+-green.svg)](https://pypi.org/project/PyPDF2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/network)
[![GitHub issues](https://img.shields.io/github/issues/siva4it/PDF-Merger.svg)](https://github.com/siva4it/PDF-Merger/issues)

A professional, feature-rich Python tool for merging multiple PDF files into a single PDF with advanced error handling and user-friendly interface.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/siva4it/PDF-Merger.git
cd PDF-Merger

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m src.pdf_merger
```

**Windows users**: Double-click `scripts/run_pdf_merger.bat`

## ✨ Key Features

- **Multiple PDF Support**: Merge any number of PDF files (minimum 2)
- **Custom Output Folders**: Specify where to save merged PDFs
- **Automatic Folder Creation**: Creates output directories if needed
- **Smart Validation**: Comprehensive file and permission checking
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Professional UI**: Interactive prompts with clear feedback
- **Detailed Reporting**: File sizes, page counts, and merge statistics

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