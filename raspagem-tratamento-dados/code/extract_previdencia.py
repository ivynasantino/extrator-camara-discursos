#coding: utf-8
#!/usr/bin/python3

import PyPDF2
import sys
import re

doc_name = "Sessão da Câmara dos Deputados - [07-08-2019 17h08min]"
obj = open("../files/nova_previdencia/" + doc_name + ".pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(obj, strict=False)

num_of_pages = pdf_reader.getNumPages()
print('Número total de páginas do documento: %d' % num_of_pages)

file_name = "previdencia_07-08-17h.txt"
prev_file = open("../data/extract-texts-pdf/" + file_name, 'w')
for page in range(num_of_pages):
    print('Página: %d' % page)
    page_text = pdf_reader.getPage(page).extractText()
    prev_file.write(page_text)
    
prev_file.close()
obj.close()