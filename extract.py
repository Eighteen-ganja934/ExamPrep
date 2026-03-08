import sys
import subprocess
try:
    import fitz # PyMuPDF
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf", "--quiet"])
    import fitz

import glob

pdfs = glob.glob(r"c:\Users\HP\.gemini\antigravity\playground\sonic-andromeda\*.pdf")
output = []
for pdf in pdfs:
    output.append(f"=== START PDF: {pdf} ===")
    doc = fitz.open(pdf)
    for i, page in enumerate(doc):
        output.append(f"--- Page {i+1} ---")
        output.append(page.get_text())
    output.append(f"=== END PDF: {pdf} ===\n")

with open(r"c:\Users\HP\.gemini\antigravity\playground\sonic-andromeda\pyqs_text.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("Extraction complete.")
