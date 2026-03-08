# ExamPrep: PSLP Predictive Analysis

An interactive, responsive, and fully self-contained web infographic for Probability, Statistics, and Linear Programming (PSLP) exam preparation. 

Built to help students analyze historical question trends and access authentic past papers effortlessly, this project encapsulates exam data into a highly visual dashboard with embedded analytics.

---

## 🚀 Features

- **Predictive Analytics Tracking**: Highlights the historical recurrence likelihood of major topics (Bayes' Theorem, Standard Distributions, PMF/PDFs) based on multi-year data.
- **Embedded PYQ Repository**: Includes the original mid-term question papers (2023–2025) embedded natively as Base64 Data URIs, completely nullifying the risk of 404 broken links or CDN caching issues. 
- **Strategic Visualization**: Utilizes `Chart.js` for dynamic bar charts (topic likelihood) and doughnut charts (mark distributions). 
- **Algorithmic Solutions**: Features dedicated study cards providing structured, step-by-step generic solutions to consistently recurring numerical problems. 
- **Predicted Mock Paper**: Synthesized from the distribution weights of past exams, presenting a realistic mock paper for self-assessment.
- **Sleek Interface & Dark Mode**: fully responsive utility-first design built on Tailwind CSS, featuring a beautiful toggleable dark mode interface optimized for both desktop and mobile studying.

---

## 🛠️ Project Structure

The project is thoughtfully organized into development logic and production-ready output, guaranteeing easy access or modification of source data.

```text
ExamPrep/
├── index.html                  # The final standalone web application (Includes Base64 embedded PDFs)
├── README.md                   # Project documentation
├── scripts/                    # Python utility scripts utilized during development
│   ├── add_dark_mode.py        # Automated injection of Tailwind Dark Mode UI classes 
│   ├── embed_pdfs.py           # Core logic for converting binary PDFs to Base64 HTTP-embeddable links
│   └── extract.py              # OCR text extraction algorithms utilized for initial analysis
└── src/                        # Source materials and assets
    ├── pyqs_text.txt           # Extracted textual analysis of past papers
    └── pdfs/                   # Unmodified, original PDF scans of past term exams
```

---

## 💻 Technologies Used

- **HTML5 & Vanilla JS / CSS**: Core structural and functional backbone.
- **Tailwind CSS (via CDN)**: Rapid, standardized UI development.
- **Chart.js**: Open-source HTML5-canvas-based data visualization library.
- **Python 3**: Automation pipelines parsing the syllabus logic and embedding the binary PDFs into raw HTML strings.

---

## ⚙️ Installation & Usage

Because the website utilizes Base64 to embed PDFs directly into the HTML tree, no complex backend or package manager is required. 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ExamPrep.git
   ```
2. **Launch the platform:**
   Simply double-click `index.html` to open it locally in any modern browser (Chrome, Firefox, Edge, Safari). Alternatively, run a static server (e.g., `python -m http.server`) for a networked experience.
3. **Download PYQs:**
   Navigate to the "PYQs" section and tap the respective year button. The PDF will instantly construct and download via the local browser engine.

---

## 🔮 Limitations & Future Improvements

- **Scalability**: While Base64 embedding guarantees 100% uptime for files, it significantly inflates the file size of `index.html` (currently spanning multiple megabytes). Moving to a hosted S3-bucket configuration may be optimal if the database expands significantly. 
- **Dynamic Data Models**: The charts currently implement hardcoded datasets. A future iteration could decouple this logic into an external `.json` configuration file fetched upon app initialization.
- **Extended Storage**: Only Units I and II are fully mapped. Integrating insights from Units III and IV would complete the curriculum coverage.

---
*Developed synthetically for educational insight. Best of luck on the mid-terms!*
