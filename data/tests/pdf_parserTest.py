import pytest
import pandas as pd
import sys
sys.path.insert(1, "./nlp/")
import pdf_parser
import PyPDF4

sample = 'tests/00-24' + '.pdf'
pdfFileObj = open(sample, 'rb')
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
if pdfReader.isEncrypted:
    pdfReader.decrypt('')
pageObj = pdfReader.getPage(2)
pageObj.mergePage(pdfReader.getPage(3))
names_ = ["FARR", "REARDON", "UNDERWOOD"]
positions_ = ['p', 'r', 'r']

def test_getNames():
    (pageObj, names, positions) = pdf_parser.getNames(pdfReader)
    assert names == names_
    assert positions == positions_


def test_readWords():
    __ = ""
    text = pdf_parser.readWords(pdfReader, pageObj, names_, positions_, 0, __)
    s = open('tests/sample.txt', 'r').read()
    assert text[0][0] == s

