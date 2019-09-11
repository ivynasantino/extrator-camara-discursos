#coding: utf-8
#!/usr/bin/python3

__author__ = "Ivyna Santino"
__maintainer__ = "Ivyna Santino"
__email__ = "ivyna.alves@ccc.ufcg.edu.br"
__version__ = "1.0.0"

def leitura_arquivo(caminho):
	obj = open(caminho, 'rb')
	pdf_reader = PyPDF2.PdfFileReader(obj, strict=False)
	return pdf_reader

def escreve_arquivo(caminho, texto_pdf):
	obj = open(caminho, 'w')
	obj.write(texto_pdf)

def dados_pdf(obj_pdf, nome_arquivo):
	numero_paginas = pdf_reader.getNumPages()
	print('Dados do documento')
	print('====================')
	print('%s tem %d páginas' % (nome_arquivo))
	print()
	return(numero_paginas)

def extrai_texto_pdf(obj_pdf, numero_paginas):
	print('Inicia extração dos textos')
	print('==========================')
	print()
	for pagina in range(numero_paginas):
		pagina_texto = obj_pdf.getPage(pagina).extractText()
		print('O texto da página %d foi extraído' % (pagina))
	return pagina_texto

def main():
	pasta = ""
	nome_arquivo = ""
	caminho = pasta + nome_arquivo

	obj_pdf = leitura_arquivo(caminho)
	dados_documento = dados_pdf(obj_pdf, nome_arquivo)

	texto_pdf = extrai_texto_pdf(obj_pdf, dados_documento)

	pasta_final = ""
	caminho_final = pasta_final + nome_arquivo
	arquivo_final = escreve_arquivo(, texto_pdf)

	arquivo_final.close()
	obj_pdf.close()
