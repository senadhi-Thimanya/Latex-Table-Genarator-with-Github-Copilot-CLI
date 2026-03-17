# Excel to LaTeX Table Generator

A user-friendly web application that converts tables from **multiple sources** to professional LaTeX code. Choose your input method:
- ✅ **Paste Data** - No setup needed (copy from Excel, Sheets, etc.)
- ✅ **Upload Excel File** - Direct .xlsx/.xls conversion
- ✅ **Upload Table Image** - Extract tables from screenshots

## Features

- ✅ **Multiple Input Methods** - Paste data, upload Excel, or extract from images
- ✅ **No Installation Required** (for Paste/Excel modes)
- ✅ **Automatic Table Detection** - Smart parsing of various table formats
- ✅ **Professional LaTeX Output** - `\begin{tabular}` with proper formatting
- ✅ **Customizable** - Add section titles, captions, and labels
- ✅ **Export Options** - Copy to clipboard or download as `.tex` file
- ✅ **Web UI** - Modern, responsive interface with drag-and-drop
- ✅ **No API Costs** - Everything runs locally on your machine

## Quick Start

### 1. Start the Server
```bash
python app.py
```

### 2. Open in Browser
Open: **http://localhost:8000**

### 3. Choose Your Input Method

#### Method A: Paste Table Data (Recommended - No Setup!)
```
Name | Age | City
John | 30  | NYC
Jane | 25  | LA
```
Copy from Excel, Google Sheets, or any table source and paste directly.

#### Method B: Upload Excel File
Select a `.xlsx` or `.xls` file and the tool extracts it automatically.

#### Method C: Upload Table Image
Upload a screenshot of a table. To enable automatic extraction:
```bash
pip install easyocr
```
(Optional - without this, use the linked free online OCR tool)

### 4. Customize (Optional)
- Add section title
- Add table caption
- Add LaTeX label

### 5. Export
- Copy code to clipboard
- Download as `.tex` file

## Installation

### Basic Setup (Paste Data & Excel - Works Immediately)
```bash
pip install -r requirements.txt
python app.py
```

### Add Image Extraction (Optional)
For automatic image-to-table conversion:
```bash
pip install easyocr
```
Then restart `python app.py`.

Note: First run downloads ~500MB of OCR models (one-time download).

## File Structure

```
.
├── app.py                    # Flask web server
├── table_to_latex.py         # LaTeX generation
├── excel_to_latex.py         # Excel to LaTeX converter
├── vision_table_extractor.py # Image extraction (optional)
├── templates/
│   └── index.html            # Web UI
├── requirements.txt          # Python dependencies
├── USER_GUIDE.md             # Detailed usage guide
└── README.md                 # This file
```

## Output Example

Input table:
```
Name | Age | City
Alice | 30 | NYC
Bob | 25 | LA
```

Generated LaTeX:
```latex
\begin{table}[H]
\centering
\begin{tabular}{|c|c|c|}
\hline
Name & Age & City \\ \hline
Alice & 30 & NYC \\ \hline
Bob & 25 & LA \\ \hline
\end{tabular}
\caption{Your caption}
\label{tab:your-label}
\end{table}
```

## Image Extraction Options

### Option 1: Online OCR (Free, No Installation)
1. Go to https://www.onlineocr.net/
2. Upload your table image
3. Copy extracted text
4. Paste into "Paste Data" tab
5. Generate LaTeX

### Option 2: Local OCR (Automatic)
```bash
pip install easyocr
python app.py
```
Then use "Upload Image" tab directly.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 8000 in use | Kill Python: `Get-Process python \| Stop-Process -Force` (Windows) |
| Image upload shows fallback | Install EasyOCR or use online OCR link provided |
| Table formatting wrong | Check paste format - use pipes `\|` or tabs to separate columns |
| Need help | See [USER_GUIDE.md](USER_GUIDE.md) for detailed instructions |

## Dependencies

- **Core**: Python 3.7+, Flask, Pillow, Openpyxl
- **Optional**: EasyOCR (for image extraction)

See `requirements.txt` for exact versions.

## Original CLI Script

The original `excel_to_latex.py` script still works for batch processing:

```bash
python excel_to_latex.py
```

Edit the configuration at the top of the file to set your input/output paths.

## Required LaTeX Packages

Include in your LaTeX document preamble:

```latex
\usepackage{float}      % For [H] positioning
\usepackage{array}      % For column formatting
\usepackage{ragged2e}   % For \RaggedRight
```

## FAQ

**Q: Do I need to install Tesseract?**
A: No. Image extraction now uses EasyOCR (easier to install) or free online tools.

**Q: Can I use this offline?**
A: Yes! Paste data and Excel methods work fully offline. Image extraction works offline after EasyOCR download.

**Q: Is my data sent anywhere?**
A: No. Everything runs locally on your machine. No cloud services used (except optional online OCR tool).

**Q: Can I batch process multiple tables?**
A: Yes - use the original CLI script: `python excel_to_latex.py`

## License

Open source - use freely in your projects.

