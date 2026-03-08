# PSLP Exam Prep Infographic

A responsive, interactive single-page infographic showcasing a predictive analysis for the Probability, Statistics, and Linear Programming (PSLP) mid-term examination.

## Features

- **Predictive Analytics:** Visualizes historical topic likelihoods using Chart.js based on previous year question papers.
- **Syllabus Overview:** Clean, readable breakdown of Units I and II.
- **Embedded PYQs:** Direct download links for actual past mid-term papers, embedded directly as Base64 data URIs so they never 404.
- **Top Topics Solutions:** Step-by-step algorithms for solving the most common types of questions (Bayes' Theorem, Normal Distribution, PDFs).
- **Mock Exam Paper:** A fully predicted, realistically weighted mock mid-term paper derived from historical patterns.
- **Dark Mode:** Built-in dark mode toggle for comfortable late-night studying, implemented using Tailwind CSS dark classes.

## Technologies Used

- **HTML5 & Vanilla CSS/JS:** Core structure and logic.
- **Tailwind CSS (via CDN):** Rapid, utility-first styling ensuring a beautiful, modern, and responsive interface.
- **Chart.js:** Data visualization for trend likelihoods and mark distributions.

## How to Run Locally

You don't need any complex build steps or dependencies to run this locally!

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ExamPrep.git
   ```
2. Open the `dist/index.html` file directly in any modern web browser.
   - Alternatively, you can use a local development server like Live Server (VS Code extension) or Python's HTTP server:
     ```bash
     cd ExamPrep/dist
     python -m http.server 8000
     ```
     Then navigate to `http://localhost:8000` in your browser.

## Deployment Notes

This project is configured to run flawlessly on simple static hosting platforms like Surge or GitHub Pages. 
Because the PDF past papers are directly encoded into the HTML body as Data URIs, there are no external assets to lose track of or fail loading. The entire experience is bundled into one robust `index.html` file.

## Disclaimer

This is a synthesized predictive analysis intended for study preparation. It does not guarantee the appearance of specific questions on the actual examination. Good luck!
