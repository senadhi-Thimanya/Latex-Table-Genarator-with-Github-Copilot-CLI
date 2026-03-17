# LaTeX Table Generator - User Guide

## Quick Start

Your web app is running at: **http://localhost:8000**

## Features Available

### 1. **Paste Data** (Recommended - Works Perfectly ✅)
- Enter your table data directly as text
- Supports multiple formats:
  - Pipe-separated: `Name | Age | City`
  - Tab-separated: `Name	Age	City`
  - Space-separated: `Name Age City`

### 2. **Upload Excel File** (Fully Working ✅)
- Upload `.xlsx` or `.xls` files
- Automatically extracts table structure
- Converts to LaTeX

### 3. **Upload Table Image** (Available with optional setup)
- Upload PNG/JPG images of tables
- **Free Option**: Use the linked online OCR tool (https://www.onlineocr.net/)
  - Extract text from your table image
  - Paste into "Paste Data" tab
- **Advanced**: Install EasyOCR for local processing (requires ~500MB download)
  - `pip install easyocr`
  - Image extraction will then work automatically

## How to Use

### Basic Workflow
1. Open http://localhost:8000
2. Choose input method:
   - **Tab 1: Paste Data** - For manual entry or OCR'd text
   - **Tab 2: Upload File** - For Excel files
   - **Tab 3: Upload Image** - For table screenshots (with fallback guidance)
3. Fill in optional fields:
   - Section Title: Your table title
   - Caption: Table description
   - Label: LaTeX label (for references)
4. Click "Generate LaTeX"
5. Copy the code or download as .tex file

### Example Paste Data
```
Name | Age | City | Job
Alice | 30 | NYC | Engineer
Bob | 25 | LA | Designer
Charlie | 35 | Chicago | Manager
```

## Image-Based Table Extraction

### Option A: Online OCR (Free, No Installation)
1. Go to https://www.onlineocr.net/
2. Upload your table image
3. Extract text
4. Paste into "Paste Data" tab
5. Generate LaTeX

### Option B: Local OCR (Requires Installation)
Install EasyOCR for automatic image processing:
```powershell
pip install easyocr
```
Then restart the server - image extraction will work automatically.

Note: First run downloads ~500MB of models (one-time).

## Output

The generator creates proper LaTeX table code:
- Automatically formatted with `\begin{tabular}`
- Included section title if provided
- Caption and label for document references
- Ready to paste into your LaTeX documents

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server won't start | Make sure port 8000 is free; run `Get-Process python \| Stop-Process -Force` |
| Image upload shows fallback message | Install EasyOCR (`pip install easyocr`) or use online OCR |
| LaTeX code looks wrong | Check your table format in Paste Data tab - use pipes \| to separate columns |
| Port 8000 already in use | Kill Python processes: `Get-Process python \| Stop-Process -Force` |

## Server Management

Start server:
```powershell
python app.py
```

Stop server:
- Press `Ctrl+C` in the terminal
- Or: `Get-Process python | Stop-Process -Force`

## File Locations

- Web UI: `templates/` folder
- Core logic: `app.py`, `table_to_latex.py`
- Image extraction: `vision_table_extractor.py`
- Excel handling: `excel_to_latex.py`
