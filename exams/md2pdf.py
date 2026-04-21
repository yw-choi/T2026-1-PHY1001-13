#!/usr/bin/env python3
"""Convert markdown exam files (with LaTeX math) to PDF via xelatex."""

import sys
import re
import os
import subprocess
import tempfile


PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Noto Sans CJK KR}
\setsansfont{Noto Sans CJK KR}
\usepackage{amsmath,amssymb,amsfonts}
\DeclareMathOperator{\Tr}{Tr}
\usepackage{geometry}
\geometry{margin=2cm}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{xcolor}
\definecolor{sogang}{HTML}{8B0029}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=sogang,urlcolor=sogang}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em}

\begin{document}
"""

POSTAMBLE = r"""
\end{document}
"""


def md_to_latex(md_text):
    lines = md_text.split("\n")
    tex_lines = []
    in_list = False
    in_table = False
    table_cols = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        # Horizontal rule -> \bigskip\hrule
        if re.match(r"^---+\s*$", line):
            if in_list:
                tex_lines.append(r"\end{itemize}")
                in_list = False
            tex_lines.append(r"\bigskip\hrule\bigskip")
            i += 1
            continue

        # Headers
        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            if in_list:
                tex_lines.append(r"\end{itemize}")
                in_list = False
            level = len(m.group(1))
            title = process_inline(m.group(2))
            if level == 1:
                tex_lines.append(r"{\centering\Large\bfseries\color{sogang} " + title + r" \par}")
                tex_lines.append(r"\bigskip")
            elif level == 2:
                tex_lines.append(r"\bigskip{\large\bfseries\color{sogang} " + title + r"}\par\medskip")
            elif level == 3:
                tex_lines.append(r"\medskip{\normalsize\bfseries\color{sogang} " + title + r"}\par\smallskip")
            i += 1
            continue

        # Display math block $$...$$
        if line.strip().startswith("$$"):
            if in_list:
                pass  # keep in list context
            # Collect until closing $$
            if line.strip() == "$$":
                # Multi-line display math
                math_lines = []
                i += 1
                while i < len(lines) and lines[i].strip() != "$$":
                    math_lines.append(lines[i])
                    i += 1
                tex_lines.append(r"\[")
                tex_lines.extend(math_lines)
                tex_lines.append(r"\]")
                i += 1
                continue
            else:
                # Single line $$...$$
                content = line.strip()
                if content.endswith("$$") and len(content) > 4:
                    inner = content[2:-2]
                    tex_lines.append(r"\[" + inner + r"\]")
                    i += 1
                    continue

        # Table detection
        if "|" in line and not line.strip().startswith(">"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if i + 1 < len(lines) and re.match(r"^\|?[\s\-:]+\|", lines[i + 1]):
                # Table header
                if in_list:
                    tex_lines.append(r"\end{itemize}")
                    in_list = False
                table_cols = len(cells)
                col_spec = "l" * table_cols
                tex_lines.append(r"\begin{longtable}{" + col_spec + "}")
                tex_lines.append(r"\toprule")
                tex_lines.append(" & ".join(process_inline(c) for c in cells) + r" \\")
                tex_lines.append(r"\midrule")
                in_table = True
                i += 2  # skip header and separator
                continue
            elif in_table:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                tex_lines.append(" & ".join(process_inline(c) for c in cells) + r" \\")
                i += 1
                continue

        if in_table and (not line.strip() or "|" not in line):
            tex_lines.append(r"\bottomrule")
            tex_lines.append(r"\end{longtable}")
            in_table = False

        # Blockquote
        if line.strip().startswith(">"):
            if in_list:
                tex_lines.append(r"\end{itemize}")
                in_list = False
            content = process_inline(line.strip().lstrip("> "))
            tex_lines.append(r"\begin{quote}\small\itshape " + content + r"\end{quote}")
            i += 1
            continue

        # Unordered list
        m = re.match(r"^(\s*)[-*]\s+(.*)", line)
        if m:
            if not in_list:
                tex_lines.append(r"\begin{itemize}[nosep]")
                in_list = True
            tex_lines.append(r"\item " + process_inline(m.group(2)))
            i += 1
            continue

        # Ordered list
        m = re.match(r"^(\s*)\d+\.\s+(.*)", line)
        if m:
            if not in_list:
                tex_lines.append(r"\begin{itemize}[nosep]")
                in_list = True
            tex_lines.append(r"\item " + process_inline(m.group(2)))
            i += 1
            continue

        # Empty line
        if not line.strip():
            if in_list:
                tex_lines.append(r"\end{itemize}")
                in_list = False
            tex_lines.append("")
            i += 1
            continue

        # Regular paragraph
        if in_list:
            tex_lines.append(r"\end{itemize}")
            in_list = False
        tex_lines.append(process_inline(line))
        i += 1

    if in_list:
        tex_lines.append(r"\end{itemize}")
    if in_table:
        tex_lines.append(r"\bottomrule")
        tex_lines.append(r"\end{longtable}")

    return "\n".join(tex_lines)


def process_inline(text):
    """Process inline markdown formatting, preserving LaTeX math."""
    # Protect math spans
    parts = []
    rest = text

    # Split by $...$ and $$...$$ keeping them intact
    # First handle $$...$$
    tokens = re.split(r"(\$\$.*?\$\$)", rest)
    result_tokens = []
    for tok in tokens:
        if tok.startswith("$$") and tok.endswith("$$"):
            result_tokens.append(tok.replace("$$", "$"))  # display->inline in text context
        else:
            # Split by $...$
            subtokens = re.split(r"(\$[^$]+?\$)", tok)
            for st in subtokens:
                if st.startswith("$") and st.endswith("$") and len(st) > 2:
                    result_tokens.append(st)  # keep math as is
                else:
                    result_tokens.append(format_text(st))

    return "".join(result_tokens)


def format_text(text):
    """Apply markdown formatting to non-math text."""
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"\\textit{\1}", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r"\\texttt{\1}", text)
    # Escape special LaTeX chars (but not already escaped ones, and not in math)
    # Be careful: & # % need escaping
    text = text.replace("&", r"\&")
    text = text.replace("#", r"\#")
    text = text.replace("%", r"\%")
    # Don't escape $ as it's used for math
    return text


def convert(md_path, pdf_path):
    with open(md_path, "r") as f:
        md_text = f.read()

    tex_body = md_to_latex(md_text)
    tex_full = PREAMBLE + tex_body + POSTAMBLE

    with tempfile.TemporaryDirectory() as tmpdir:
        tex_path = os.path.join(tmpdir, "exam.tex")
        with open(tex_path, "w") as f:
            f.write(tex_full)

        for run in range(2):
            result = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "exam.tex"],
                cwd=tmpdir,
                capture_output=True,
                text=True,
                timeout=60,
            )
            pass

        tmp_pdf = os.path.join(tmpdir, "exam.pdf")
        if os.path.exists(tmp_pdf):
            import shutil
            shutil.copy2(tmp_pdf, pdf_path)
            print(f"  OK: {pdf_path}")
            return True
        else:
            print(f"  ERROR: no PDF generated for {md_path}")
            return False


if __name__ == "__main__":
    for md_path in sys.argv[1:]:
        pdf_path = md_path.replace(".md", ".pdf")
        convert(md_path, pdf_path)
