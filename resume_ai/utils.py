import PyPDF2

def extract_text_from_pdf(file):
    reader=PyPDF2.PdfReader(file)
    text=""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

'''
👉 PyPDF2 is used to:
1.Read PDF files
2.Extract text from PDF
3.Work with PDF pages

👉 reader = PyPDF2.PdfReader(file)
1.Opens the PDF
2.Creates a reader object
3.Loads all pages

reader = open_pdf(file)
Now reader contains:
1.Total pages
2.Page content
3.PDF structure


👉 for page in reader.pages:
If the resume has:
3 pages
5 pages
10 pages
This loop goes through each page one by one.

👉 So flow is:
👉 PDF → Extract text → Send text to LLM → Analyze

'''