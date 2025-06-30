@echo off
echo Starting PDF Merger Tool...
echo.

REM Check if we're in the project root directory
if exist "run_pdf_merger.py" (
    python run_pdf_merger.py
) else if exist "src\pdf_merger\__init__.py" (
    REM We're in the project root, use the module approach
    python -m src.pdf_merger
) else (
    echo Error: Please run this script from the PDF-Merger project root directory.
    echo Current directory: %CD%
    echo.
    echo Please navigate to the PDF-Merger folder and try again.
)

echo.
echo Press any key to exit...
pause >nul 