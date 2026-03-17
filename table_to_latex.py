"""
Convert table data to LaTeX format
"""

from typing import List, Dict, Optional


class TableToLatex:
    """Convert structured table data (headers, rows) to LaTeX code"""
    
    def __init__(self, headers: List[str], rows: List[List[str]]):
        """
        Initialize converter with table data
        
        Args:
            headers: List of column headers
            rows: List of rows, where each row is a list of cell values
        """
        self.headers = headers
        self.rows = rows
        self.num_cols = len(headers) if headers else (len(rows[0]) if rows else 0)
    
    @staticmethod
    def _escape_latex(text: str) -> str:
        """Escape special LaTeX characters"""
        if text is None:
            return ""
        
        text = str(text)
        
        # Escape special characters
        replacements = {
            '\\': r'\textbackslash{}',
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text
    
    def _calculate_column_widths(self) -> List[float]:
        """Calculate column widths"""
        max_textwidth = 0.90
        width_per_col = max_textwidth / self.num_cols if self.num_cols > 0 else 0.90
        
        # Slightly adjust to ensure rounding doesn't exceed max
        widths = [round(width_per_col, 2) for _ in range(self.num_cols)]
        
        # Adjust last column if necessary
        total = sum(widths)
        if total > max_textwidth:
            widths[-1] -= (total - max_textwidth)
            widths[-1] = round(widths[-1], 2)
        
        return widths
    
    def generate_latex(
        self,
        section_title: Optional[str] = None,
        caption: Optional[str] = None,
        label: Optional[str] = None
    ) -> str:
        """
        Generate LaTeX table code
        
        Args:
            section_title: Optional section title
            caption: Optional table caption
            label: Optional LaTeX label for references
            
        Returns:
            LaTeX code as string
        """
        if self.num_cols == 0:
            raise ValueError("Table has no columns")
        
        # Calculate column widths
        col_widths = self._calculate_column_widths()
        
        # Build column specification
        col_spec = "|" + "|".join(
            [f">{{\\RaggedRight}}p{{{width}\\textwidth}}" for width in col_widths]
        ) + "|"
        
        # Start building LaTeX
        latex = []
        latex.append("\\begin{table}[H]")
        
        if section_title:
            latex.append(f"\\section{{{section_title}}}")
        
        latex.append("\\centering")
        latex.append(f"\\begin{{tabular}}{{{col_spec}}}")
        latex.append("\\hline")
        
        # Add header row
        if self.headers:
            escaped_headers = [self._escape_latex(h) for h in self.headers]
            latex.append(" & ".join(escaped_headers) + " \\\\ \\hline")
        
        # Add data rows
        for row in self.rows:
            escaped_cells = [self._escape_latex(cell) for cell in row]
            latex.append(" & ".join(escaped_cells) + " \\\\ \\hline")
        
        latex.append("\\end{tabular}")
        
        if caption:
            latex.append(f"\\caption{{{caption}}}")
        
        if label:
            latex.append(f"\\label{{{label}}}")
        
        latex.append("\\end{table}")
        
        return "\n".join(latex)


def convert_to_latex(
    headers: List[str],
    rows: List[List[str]],
    section_title: Optional[str] = None,
    caption: Optional[str] = None,
    label: Optional[str] = None
) -> str:
    """
    Convenience function to convert table data to LaTeX
    
    Args:
        headers: List of column headers
        rows: List of rows, where each row is a list of cell values
        section_title: Optional section title
        caption: Optional table caption
        label: Optional LaTeX label
        
    Returns:
        LaTeX code as string
    """
    converter = TableToLatex(headers, rows)
    return converter.generate_latex(section_title, caption, label)
