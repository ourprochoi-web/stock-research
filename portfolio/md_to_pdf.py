#!/usr/bin/env python3
"""Markdown → PDF 변환 스크립트 (xhtml2pdf, 한글 지원, 표/목차 포맷팅)"""

import markdown
import sys
import os
from xhtml2pdf import pisa

FONT_PATH = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"

CSS = """
@page {
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
    @frame footer {
        -pdf-frame-content: footerContent;
        bottom: 0mm;
        margin-left: 16mm;
        margin-right: 16mm;
        height: 10mm;
    }
}

@font-face {
    font-family: "KoreanFont";
    src: url("FONT_PATH_PLACEHOLDER");
}

body {
    font-family: "KoreanFont", Helvetica, sans-serif;
    font-size: 9pt;
    line-height: 1.6;
    color: #1a1a1a;
}

h1 {
    font-family: "KoreanFont", Helvetica, sans-serif;
    font-size: 18pt;
    color: #0d1b2a;
    border-bottom: 2px solid #1b4965;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 14px;
}

h2 {
    font-family: "KoreanFont", Helvetica, sans-serif;
    font-size: 14pt;
    color: #1b4965;
    border-bottom: 1px solid #bee9e8;
    padding-bottom: 4px;
    margin-top: 22px;
    margin-bottom: 10px;
}

h3 {
    font-family: "KoreanFont", Helvetica, sans-serif;
    font-size: 11pt;
    color: #274c77;
    margin-top: 16px;
    margin-bottom: 6px;
}

h4 {
    font-family: "KoreanFont", Helvetica, sans-serif;
    font-size: 10pt;
    color: #3d6098;
    margin-top: 12px;
    margin-bottom: 5px;
}

p {
    margin: 4px 0;
    font-size: 9pt;
}

strong {
    color: #0d1b2a;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 12px 0;
    font-size: 8pt;
    -pdf-keep-with-next: true;
}

th {
    background-color: #1b4965;
    color: white;
    padding: 5px 6px;
    text-align: left;
    font-size: 7.5pt;
    border: 1px solid #1b4965;
    font-family: "KoreanFont", Helvetica, sans-serif;
}

td {
    padding: 4px 6px;
    border: 1px solid #d0d7de;
    font-size: 7.5pt;
    font-family: "KoreanFont", Helvetica, sans-serif;
}

tr.even td {
    background-color: #f6f8fa;
}

blockquote {
    border-left: 3px solid #1b4965;
    margin: 10px 0;
    padding: 6px 12px;
    background-color: #f0f7fb;
    color: #333;
    font-size: 8.5pt;
}

code {
    font-family: Courier, monospace;
    font-size: 7.5pt;
    background-color: #f0f3f5;
    padding: 1px 3px;
}

pre {
    background-color: #f6f8fa;
    border: 1px solid #d0d7de;
    padding: 8px;
    font-size: 7pt;
    font-family: Courier, monospace;
}

hr {
    border: 0;
    border-top: 1px solid #d0d7de;
    margin: 16px 0;
}

a {
    color: #1b4965;
    text-decoration: none;
}

ul, ol {
    margin: 4px 0;
    padding-left: 20px;
}

li {
    margin: 2px 0;
    font-size: 8.5pt;
}

em {
    font-style: italic;
    color: #555;
}

.toc-section {
    margin-bottom: 20px;
}

.toc-section a {
    color: #1b4965;
    text-decoration: none;
}

.toc-section li {
    margin: 3px 0;
    font-size: 9pt;
}

.page-number {
    text-align: center;
    font-size: 7.5pt;
    color: #999;
}
""".replace("FONT_PATH_PLACEHOLDER", FONT_PATH)


def add_even_row_classes(html):
    """Add 'even' class to alternating table rows for zebra striping."""
    import re
    def process_table(match):
        table_html = match.group(0)
        rows = table_html.split("</tr>")
        result = []
        data_row_idx = 0
        for row in rows:
            if "<th" in row:
                result.append(row)
            elif "<td" in row:
                if data_row_idx % 2 == 1:
                    row = row.replace("<tr>", '<tr class="even">', 1)
                    row = row.replace("<tr >", '<tr class="even">', 1)
                data_row_idx += 1
                result.append(row)
            else:
                result.append(row)
        return "</tr>".join(result)

    return re.sub(r'<table.*?</table>', process_table, html, flags=re.DOTALL)


def convert_md_to_pdf(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    extensions = [
        "tables",
        "fenced_code",
        "toc",
        "sane_lists",
    ]
    extension_configs = {
        "toc": {"toc_depth": "2-3", "title": ""},
    }

    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)
    html_body = md.convert(md_text)

    # Zebra stripe tables
    html_body = add_even_row_classes(html_body)

    # Build TOC
    toc_html = ""
    if hasattr(md, "toc") and md.toc and len(md.toc) > 100:
        toc_html = f"""
        <div class="toc-section">
            <h2>목차 (Table of Contents)</h2>
            {md.toc}
        </div>
        <hr/>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8"/>
    <style>{CSS}</style>
</head>
<body>
{toc_html}
{html_body}

<div id="footerContent">
    <p class="page-number">
        <pdf:pagenumber/> / <pdf:pagecount/>
    </p>
</div>
</body>
</html>"""

    with open(pdf_path, "wb") as out_f:
        status = pisa.CreatePDF(full_html, dest=out_f, encoding="utf-8")

    if status.err:
        raise RuntimeError(f"xhtml2pdf errors: {status.err}")

    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"  >> {os.path.basename(pdf_path)} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    portfolio_dir = os.path.dirname(os.path.abspath(__file__))

    md_files = sorted(
        [f for f in os.listdir(portfolio_dir) if f.endswith(".md")],
    )

    if not md_files:
        print("No .md files found in portfolio/")
        sys.exit(1)

    print(f"변환 대상: {len(md_files)}개 파일\n")

    for md_file in md_files:
        md_path = os.path.join(portfolio_dir, md_file)
        pdf_path = os.path.join(portfolio_dir, md_file.replace(".md", ".pdf"))
        print(f"변환 중: {md_file} ...")
        try:
            convert_md_to_pdf(md_path, pdf_path)
        except Exception as e:
            print(f"  !! {md_file} 실패: {e}")

    print("\n완료!")
