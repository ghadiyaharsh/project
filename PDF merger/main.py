
import PyPDF2   # Importing the PyPDF2 library to handle PDF files

pdfiles = [                                                          # List of PDF files to be merged
    "d:/pii/PYP-Project/project/PDF merger/pdf1.pdf",
    "d:/pii/PYP-Project/project/PDF merger/pdf2.pdf"
]

merger = PyPDF2.PdfMerger()         # Creating a PdfMerger object to handle the merging process



for pdf in pdfiles:                # Looping through each PDF file in the list
    with open(pdf, 'rb') as pdfFile:                                # Open the PDF file in binary read mode
        merger.append(pdfFile)                                      # Appending the PDF file to the merger object
merger.write('d:/pii/PYP-Project/project/PDF merger/merged.pdf')    # Writing the merged PDF to a new file
merger.close()

