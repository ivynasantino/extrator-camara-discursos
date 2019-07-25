import PyPDF2
import sys

obj = open("../files/nova_previdencia/reforma_10-07.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(obj, strict=False)

num_of_pages = pdf_reader.getNumPages()
print(num_of_pages)

first_page_text = pdf_reader.getPage(0).extractText()
print(first_page_text)

obj.close()
