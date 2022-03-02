import pandas as pd
import PyPDF4

sample = 'transcripts/2000/00-24.pdf'
pdfFileObj = open(sample, 'rb')
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

if pdfReader.isEncrypted:
    pdfReader.decrypt('')

# get page 0
pageObj = pdfReader.getPage(1)
for i in range(2, pdfReader.getNumPages()):

    # get each additional page
    pageObj2 = pdfReader.getPage(i)
    pageObj.mergePage(pageObj2)

# get entire page as one big string
page1 = pageObj.extractText()
# print(page1)

# split into lines and trim of first characters
pageLines = page1.split('\n')
pageLines2 = [line[3:] for line in pageLines]
print(' '.join(pageLines2))