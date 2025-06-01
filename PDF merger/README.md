🧾 PDF Merger Project

This project merges multiple PDF files into a single PDF using Python and the PyPDF2 library.

📂 Project Structure
PDF merger/
│
├── pdf1.pdf
├── pdf2.pdf
├── merged.pdf # Output file
└── merge_pdf.py # Python script to merge PDFs


📌 Features
- Merge multiple PDF files into one
- Easy-to-edit Python script
- Uses the PyPDF2 library

🚀 How It Works
1. A list of PDF file paths is defined.
2. The `PyPDF2.PdfMerger()` object is created.
3. Each file is opened and appended to the merger.
4. The merged output is saved as `merged.pdf`.

🛠️ Requirements
- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Install PyPDF2 using pip:

```bash
pip install PyPDF2
```

▶️ How to Run

Make sure the paths in the script are correct.

Place your input PDF files (pdf1.pdf, pdf2.pdf, ...) in the appropriate directory.

Run the script:
python merge_pdf.py
A new file named merged.pdf will be created.
