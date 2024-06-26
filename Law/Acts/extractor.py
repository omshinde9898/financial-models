import os
from langchain.document_loaders import PyPDFLoader


def getPdfNames():
    return os.listdir('./Acts/pdfs')

def readPdf(path):
    path = os.path.join('./Acts/pdfs',path)
    pdf_reader = PyPDFLoader(path)

    bookText = pdf_reader.load()
    
    return bookText


def getCopora():
    corpora = []

    paths = getPdfNames()
    
    for path in paths:
        corpora.extend(readPdf(path))

    return corpora

if __name__ == "__main__":
    cor = getCopora()
    for i in cor:
        print(len(i))