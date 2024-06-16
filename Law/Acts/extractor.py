import os
from PyPDF2 import PdfReader


def getPdfNames():
    return os.listdir('./pdfs')

def readPdf(path):
    path = os.path.join('./pdfs',path)
    pdf_reader = PdfReader(path)

    bookText = []

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        bookText.append(text)
    
    return bookText


def getCopora():
    corpora = []

    paths = getPdfNames()
    
    for path in paths:
        corpora.append(readPdf(path))

    return corpora

if __name__ == "__main__":
    cor = getCopora()
    for i in cor:
        print(len(i))