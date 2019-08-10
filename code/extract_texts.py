#coding: utf-8
import PyPDF2
import sys

doc_names = ["Sessão da Câmara dos Deputados - [10-07-2019 09h00min]", 
            "Sessão da Câmara dos Deputados - [10-07-2019 16h13min]",
            "Sessão da Câmara dos Deputados - [11-07-2019 09h00min]",
            "Sessão da Câmara dos Deputados - [11-07-2019 09h31min]",
            "Sessão da Câmara dos Deputados - [11-07-2019 22h16min]",
            "Sessão da Câmara dos Deputados - [12-07-2019 09h00min]",
            "Sessão da Câmara dos Deputados - [12-07-2019 09h31min]",
            "Sessão da Câmara dos Deputados - [12-07-2019 16h57min]"]

for doc_name in doc_names:
    obj = open("../files/nova_previdencia/" + doc_name + ".pdf", "rb")
    pdf_reader = PyPDF2.PdfFileReader(obj, strict=False)

    num_of_pages = pdf_reader.getNumPages()
    print('Número total de páginas do documento: %d' % num_of_pages)

    for page in range(num_of_pages):
        print('Página: %d' % page)
        page_text = pdf_reader.getPage(page).extractText()
        print(page_text)
        print()
    obj.close()
