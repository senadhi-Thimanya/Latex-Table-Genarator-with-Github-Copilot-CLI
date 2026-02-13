# Excel to LaTeX Table Generator

A Python CLI tool that converts Excel tables to LaTeX format with professional styling, supporting bullet lists, merged cells, and customizable formatting.

## Features

- ✅ Converts Excel (.xlsx) files to LaTeX table code
- ✅ Automatically detects and formats bullet lists (using • or - characters)
- ✅ Handles merged cells
- ✅ Generates tables with `\RaggedRight` column formatting
- ✅ Supports custom section titles, captions, and labels
- ✅ Smart column width distribution
- ✅ Full borders with `\hline`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python excel_to_latex.py input.xlsx
```

This outputs the LaTeX code to stdout.

### Save to File

```bash
python excel_to_latex.py input.xlsx -o output.tex
```

### With Metadata

```bash
python excel_to_latex.py input.xlsx \
  --section "Research Objectives" \
  --caption "Research objectives, explanations, and corresponding learning outcomes" \
  --label "tab:research-objectives" \
  -o output.tex
```

### Specify Sheet

```bash
python excel_to_latex.py input.xlsx -s "Sheet2"
```

## Command Line Options

| Option | Description |
|--------|-------------|
| `input_file` | Input Excel file (.xlsx) [required] |
| `-o, --output` | Output LaTeX file (default: stdout) |
| `-s, --sheet` | Sheet name (default: active sheet) |
| `--section` | Section title for the table |
| `-c, --caption` | Table caption |
| `-l, --label` | Table label (e.g., tab:mytable) |

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

## Example

See `example.xlsx` for a sample Excel file and `example_output.tex` for the generated LaTeX.

## License

MIT
