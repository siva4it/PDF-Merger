# Contributing to PDF Merger Tool

Thank you for your interest in contributing to the PDF Merger Tool! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork the repository**
   ```bash
   git clone https://github.com/siva4it/PDF-Merger.git
   cd PDF-Merger
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the coding standards below
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**
   ```bash
   python tests/test_pdf_merger.py
   ```

5. **Submit a pull request**
   - Use the provided PR template
   - Describe your changes clearly
   - Reference any related issues

## 📋 Development Setup

### Prerequisites
- Python 3.6 or higher
- Git
- PyPDF2 library

### Installation
```bash
# Clone the repository
git clone https://github.com/siva4it/PDF-Merger.git
cd PDF-Merger

# Install dependencies
pip install -r requirements.txt

# Run tests
python tests/test_pdf_merger.py
```

## 🏗️ Project Structure

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
├── setup.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 📝 Coding Standards

### Python Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise

### Code Example
```python
def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into a single PDF.
    
    Args:
        pdf_files (list): List of PDF file paths to merge
        output_path (str): Path for the output merged PDF
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Implementation here
        return True
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        return False
```

### Error Handling
- Use try-except blocks for file operations
- Provide meaningful error messages
- Log errors appropriately
- Handle edge cases gracefully

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python tests/test_pdf_merger.py

# Run with pytest (if installed)
pytest tests/
```

### Writing Tests
- Test both success and failure cases
- Use descriptive test names
- Test edge cases and error conditions
- Keep tests independent and isolated

### Test Example
```python
def test_merge_pdfs_success():
    """Test successful PDF merging."""
    # Test implementation
    assert result is True

def test_merge_pdfs_invalid_file():
    """Test PDF merging with invalid file."""
    # Test implementation
    assert result is False
```

## 📚 Documentation

### Code Documentation
- Add docstrings to all functions
- Include type hints where appropriate
- Document complex algorithms
- Provide usage examples

### User Documentation
- Update README.md for new features
- Add examples to demo scripts
- Update quick start guide
- Maintain changelog

## 🔄 Pull Request Process

### Before Submitting
1. **Test your changes**
   - Run the test suite
   - Test on different Python versions
   - Verify functionality manually

2. **Check code quality**
   - Follow PEP 8 style
   - Remove any debug code
   - Ensure proper error handling

3. **Update documentation**
   - Update README if needed
   - Add docstrings to new functions
   - Update examples if applicable

### PR Guidelines
- Use descriptive titles
- Reference related issues
- Include test results
- Provide clear description of changes
- Add screenshots for UI changes

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Tests pass locally
- [ ] Manual testing completed
- [ ] No breaking changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No debug code left
```

## 🐛 Issue Reporting

### Bug Reports
When reporting bugs, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

### Feature Requests
For feature requests, please include:
- Use case description
- Expected functionality
- Potential implementation approach
- Priority level

## 🏷️ Version Control

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, etc.)
- Keep under 50 characters for the subject line
- Use present tense

### Branch Naming
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

## 🤝 Community Guidelines

### Be Respectful
- Be kind and respectful to all contributors
- Provide constructive feedback
- Help newcomers learn and contribute

### Communication
- Use clear, professional language
- Ask questions when unsure
- Share knowledge and best practices
- Be patient with responses

## 📞 Getting Help

### Questions and Support
- Check existing issues and discussions
- Search documentation first
- Ask questions in issues or discussions
- Provide context when asking for help

### Contact Information
- GitHub Issues: [Repository Issues](https://github.com/siva4it/PDF-Merger/issues)
- Discussions: [GitHub Discussions](https://github.com/siva4it/PDF-Merger/discussions)

## 🎉 Recognition

### Contributors
All contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

### Types of Contributions
We welcome all types of contributions:
- Code improvements
- Bug fixes
- Documentation updates
- Testing improvements
- Feature suggestions
- Community support

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the PDF Merger Tool! Your help makes this project better for everyone. 🌟 