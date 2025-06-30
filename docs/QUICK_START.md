# Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies
```bash
pip install PyPDF2
```

### 2. Run the Script
Choose one of these methods:

**Method A: Command Line**
```bash
python pdf_merger.py
```

**Method B: Windows Batch File (Double-click)**
- Double-click `run_pdf_merger.bat`

**Method C: Test First**
```bash
python test_pdf_merger.py
```

### 3. Follow the Prompts
The script will ask you for:
- Multiple PDF file paths (press Enter when done adding files)
- Output folder path (optional - press Enter for current directory)
- Output filename

**Example:**
```
Enter path to PDF file #1: document1.pdf
Enter path to PDF file #2: document2.pdf
Enter path to PDF file #3: document3.pdf
Enter path to PDF file #4: [press Enter to finish]

Enter output folder path (press Enter for current directory): merged_pdfs
Enter the name for the merged PDF file: combined.pdf
```

## 📁 File Structure
```
PDF-Merger/
├── pdf_merger.py          # Main script
├── requirements.txt       # Dependencies
├── run_pdf_merger.bat    # Windows launcher
├── test_pdf_merger.py    # Test script
├── README.md             # Full documentation
└── QUICK_START.md        # This file
```

## ✨ New Features
- **Multiple PDFs**: Merge any number of PDF files (minimum 2)
- **Smart Input**: Add files one by one, press Enter when done
- **Duplicate Detection**: Prevents adding the same file twice
- **Page Count**: Shows total pages across all files
- **Detailed Summary**: File sizes, page counts, and merge statistics
- **Custom Output Folder**: Specify where to save the merged PDF
- **Auto Folder Creation**: Creates output folders automatically
- **Permission Validation**: Checks write access before merging

## 📂 Output Folder Options
- **Current Directory**: Press Enter to save in the same folder as the script
- **Custom Folder**: Enter any folder path (relative or absolute)
- **Auto Creation**: Folders are created automatically if they don't exist
- **Permission Check**: Write access is validated before starting

## ✅ Ready to Use!
Your PDF merger is now ready to run. Just execute one of the commands above and follow the prompts! 