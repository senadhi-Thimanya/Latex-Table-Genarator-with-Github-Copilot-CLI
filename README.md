# Excel to LaTeX Table Generator

A simple Python script that converts Excel tables to LaTeX format with professional styling, supporting bullet lists, merged cells, and customizable formatting.

## Features

- ✅ Converts Excel (.xlsx) files to LaTeX table code
- ✅ Automatically detects and formats bullet lists (using • or - characters)
- ✅ Handles merged cells
- ✅ Generates tables with `\RaggedRight` column formatting
- ✅ Supports custom section titles, captions, and labels
- ✅ Smart column width distribution
- ✅ Full borders with `\hline`
- ✅ No command-line arguments needed - just edit and run!

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

1. **Edit the configuration** at the top of `excel_to_latex.py`:

```python
# Edit these values in the script
INPUT_EXCEL_FILE = "input.xlsx"       # Your Excel file
SHEET_NAME = None                      # None = active sheet
OUTPUT_LATEX_FILE = "output.tex"       # Output file

SECTION_TITLE = "Research Objectives"
TABLE_CAPTION = "Your caption here"
TABLE_LABEL = "tab:research-objectives"
```

2. **Run the script**:

```bash
python excel_to_latex.py
```

That's it! The LaTeX code will be saved to `output.tex`.

## Excel Formatting Tips

### Creating Bullet Lists

In your Excel cell, use one of these formats:

```
• First item
• Second item
• Third item
```

Or:

```
- First item
- Second item
- Third item
```

The tool will automatically convert these to LaTeX `\begin{itemize}` lists.

### Merged Cells

Merged cells in Excel are automatically converted to appropriate LaTeX formatting.

## Output Format

The generated LaTeX follows this structure:

```latex
\begin{table}[H]
\section{Your Section Title}
\centering
\begin{tabular}{|>{\RaggedRight}p{width}|...|}
\hline
Cell 1 & Cell 2 \\ \hline
...
\end{tabular}
\caption{Your caption}
\label{your-label}
\end{table}
```

## Required LaTeX Packages

Add these to your LaTeX document preamble:

```latex
\usepackage{float}      % For [H] positioning
\usepackage{array}      % For advanced column formatting
\usepackage{ragged2e}   % For \RaggedRight
```

## Example Output

```latex
\begin{table}[H]
\section{Research Objectives}
\centering
\begin{tabular}{|>{\RaggedRight}p{0.15\textwidth}|>{\RaggedRight}p{0.65\textwidth}|>{\RaggedRight}p{0.10\textwidth}|}
\hline
Column 1 & Column 2 & Column 3 \\ \hline
...
\end{tabular}
\caption{Your caption}
\label{tab:research-objectives}
\end{table}
```
