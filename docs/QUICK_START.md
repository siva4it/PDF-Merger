# Quick Start Guide - PDF Merger Tool

Get up and running with the PDF Merger Tool in minutes!

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/siva4it/PDF-Merger.git
cd PDF-Merger
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Tool
```bash
python run_pdf_merger.py
```

## 📖 Basic Usage

### Running the Tool

**Method 1: Simple Launcher (Recommended)**
```cmd
python run_pdf_merger.py
```

**Method 2: Windows Batch File**
```cmd
run_pdf_merger.bat
```

**Method 3: As a Module (from project root)**
```cmd
python -m src.pdf_merger
```

### Step-by-Step Process

1. **Start the tool**
   ```bash
   python run_pdf_merger.py
   ```

2. **Add PDF files**
   - Enter the path to each PDF file
   - Press Enter without a filename when done
   - Minimum 2 files required

3. **Specify output settings**
   - Enter output folder path (optional)
   - Provide output filename

4. **Review and confirm**
   - Check the summary
   - Confirm the merge operation

## 🎯 Example Session

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

## 🛠️ Testing

Run the test suite to verify everything is working:
```bash
python tests/test_pdf_merger.py
```

## 🆘 Troubleshooting

### Common Issues

**"No module named 'src'"**
- Make sure you're in the project root directory
- Use `python run_pdf_merger.py` instead

**"PyPDF2 not found"**
- Install dependencies: `pip install -r requirements.txt`

**"Permission denied"**
- Check that you have write permissions in the output directory
- Try a different output location

### Getting Help

- Check the [main README](../README.md) for detailed documentation
- Report issues on [GitHub](https://github.com/siva4it/PDF-Merger/issues)
- Review the [contributing guidelines](../CONTRIBUTING.md)

## 🎉 Next Steps

- Try merging different types of PDF files
- Experiment with custom output folders
- Check out the [examples](../examples/) directory
- Contribute to the project!

---

**Happy PDF merging! 📄✨** 