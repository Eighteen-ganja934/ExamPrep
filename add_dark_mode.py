import re
import os

filepath = r"c:\Users\HP\.gemini\antigravity\playground\sonic-andromeda\dist\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    r'\bbg-white\b': 'bg-white dark:bg-gray-800 dark:border-gray-700',
    r'\btext-gray-800\b': 'text-gray-800 dark:text-gray-100',
    r'\btext-gray-700\b': 'text-gray-700 dark:text-gray-300',
    r'\btext-gray-600\b': 'text-gray-600 dark:text-gray-400',
    r'\bborder-gray-200\b': 'border-gray-200 dark:border-gray-700',
    r'\bbg-gray-50\b': 'bg-gray-50 dark:bg-gray-900',
    r'\bbg-gray-100\b': 'bg-gray-100 dark:bg-gray-800',
    r'\btext-gray-900\b': 'text-gray-900 dark:text-gray-200',
    r'\bbg-blue-50\b': 'bg-blue-50 dark:bg-blue-900/30',
    r'\bbg-pink-50\b': 'bg-pink-50 dark:bg-pink-900/30',
    r'\bbg-yellow-50\b': 'bg-yellow-50 dark:bg-yellow-900/30',
    r'\bbg-purple-50\b': 'bg-purple-50 dark:bg-purple-900/30',
    r'\bbg-purple-100\b': 'bg-purple-100 dark:bg-purple-900/50',
    r'\btext-blue-900\b': 'text-blue-900 dark:text-blue-300',
    r'\btext-pink-900\b': 'text-pink-900 dark:text-pink-300',
    r'\btext-yellow-900\b': 'text-yellow-900 dark:text-yellow-300',
    r'\btext-purple-900\b': 'text-purple-900 dark:text-purple-300',
    r'\bborder-blue-200\b': 'border-blue-200 dark:border-blue-800',
    r'\bborder-pink-200\b': 'border-pink-200 dark:border-pink-800',
    r'\bborder-yellow-200\b': 'border-yellow-200 dark:border-yellow-800',
    r'\bborder-purple-200\b': 'border-purple-200 dark:border-purple-800',
    r'\bborder-gray-400\b': 'border-gray-400 dark:border-gray-600',
    r'\bborder-black\b': 'border-black dark:border-gray-500',
}

for pattern, replacement in replacements.items():
    # Only replace if not already followed by dark variant
    # This is a simple approach, wait we don't have duplicated runs so it's fine once.
    html = re.sub(pattern, replacement, html)

# Make sure chart instances are assigned to window to be accessible by toggle script
html = html.replace("const ctx1 = document.getElementById('likelihoodChart').getContext('2d');\n        new Chart(ctx1, {", "const ctx1 = document.getElementById('likelihoodChart').getContext('2d');\n        window.likelihoodChartInstance = new Chart(ctx1, {")
html = html.replace("const ctx2 = document.getElementById('marksChart').getContext('2d');\n        new Chart(ctx2, {", "const ctx2 = document.getElementById('marksChart').getContext('2d');\n        window.marksChartInstance = new Chart(ctx2, {")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)

print("Applied dark mode classes")
