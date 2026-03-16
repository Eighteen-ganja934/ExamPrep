# ⚡ ExamPrep — Semester IV Study Portal

A premium, interactive study portal for GGSIPU B.Tech Semester IV mid-term preparation. Features data-driven analytics, pattern-based study guides, and past-paper analysis for multiple subjects.

---

## 🚀 Features

- **Multi-Subject Dashboard** — Homepage with subject cards linking to dedicated study tools for each paper.
- **Predictive Analytics** — Chart.js-powered visualizations showing topic frequency and mark weightage across past papers.
- **Pattern Master** — Accordion-based step-by-step solution guides for the most commonly repeated question types.
- **Exact PYQ Citations** — Every past question is quoted verbatim with precise citations (e.g., `[Q1(a), April 2024]`).
- **PDF Downloads** — Original mid-term question papers available for direct download.
- **Study Guide** — Official syllabus highlights and core concept tables for quick revision.
- **Predicted Mock Paper** — Synthesized mock exam based on historical trends.
- **Dark Academia Theme** — Sleek, responsive UI with glassmorphism cards and smooth animations.

---

## 📚 Subjects Covered

| Paper Code | Subject | Status |
|---|---|---|
| BS-202 | Probability, Statistics and Linear Programming | ✅ Available |
| EEC-206 | Network Analysis and Synthesis | ✅ Available |
| ECC-210 | Microprocessors and Microcontrollers | 🔜 Coming Soon |
| ECC-212 | Digital Communications | 🔜 Coming Soon |
| ECC-214 | Analog Electronics II | 🔜 Coming Soon |
| ECC-216 | Electromagnetic Field Theory | 🔜 Coming Soon |

---

## 🛠️ Project Structure

```
ExamPrep/
├── index.html              # Homepage — Subject Portal
├── bs-202.html             # PSLP Dashboard (Analytics, Patterns, Study Guide, Predicted Paper)
├── eec-206.html            # NAS Dashboard (Analytics, Patterns, Study Guide, Predicted Paper)
├── coming-soon.html        # Placeholder for unimplemented subjects
├── css/
│   └── home.css            # Global stylesheet (shared by homepage + coming-soon)
├── assets/
│   └── pdfs/
│       ├── PSLP/           # 4 original PSLP PYQ PDFs (May 2023 – March 2025)
│       └── NAS/            # 3 original NAS PYQ PDFs (May 2023 – March 2025)
└── README.md
```

---

## 💻 Technologies

- **HTML5 & CSS3** — Structure and styling with CSS custom properties.
- **Vanilla JavaScript** — Tab navigation, accordions, and interactivity.
- **Chart.js** — Bar and bubble charts for exam analytics.
- **Google Fonts** — Outfit (body) + DM Serif Display (headings).

---

## ⚙️ Usage

1. **Clone:**
   ```bash
   git clone https://github.com/realraunakgupta/ExamPrep.git
   ```
2. **Serve locally:**
   ```bash
   cd ExamPrep
   python -m http.server 8000
   ```
3. **Open:** Navigate to `http://localhost:8000` in your browser.

---

*Built for GGSIPU Semester IV Mid-Term Preparation.*
