import base64
import os

pdf_files = {
    "may_2023.pdf": "PSLP_Mid_Term_May_2023.pdf",
    "nov_2023.pdf": "PSLP_Mid_Term_November_2023.pdf",
    "april_2024.pdf": "PSLP_Mid_Term_April_2024.pdf",
    "march_2025.pdf": "PSLP_Mid_Term_March_2025.pdf"
}

index_path = r"c:\Users\HP\.gemini\antigravity\playground\sonic-andromeda\dist\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html_content = f.read()

for short_name, filename in pdf_files.items():
    filepath = os.path.join(r"c:\Users\HP\.gemini\antigravity\playground\sonic-andromeda\dist", filename)
    with open(filepath, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")
        data_uri = f"data:application/pdf;base64,{encoded_string}"
        
        # Replace the href in the HTML
        old_href = f'href="{short_name}"'
        new_href = f'href="{data_uri}" download="{filename}"'
        html_content = html_content.replace(old_href, new_href)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML updated with base64 embedded PDFs.")
