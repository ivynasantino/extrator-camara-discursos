#!/usr/bin/python3

import re

def arquivoParaString(caminho):
    resultado = ""

    with open(caminho, 'r+') as arquivo:
        for linha in arquivo:
            resultado += linha

    return resultado

def escreveListaEmArquivo(lista, caminho):
    with open(caminho, "w+") as arquivo:
        for linha in lista:
            arquivo.write("|".join(linha) + "\n")
            

def partidoEstadoFala(linha):
    regexInfo = "([A-Z]*) - ([A-Z]{2}).*\)\s-\s(.*)"

    resultado = re.search(regexInfo, linha)

    if resultado:
        resultado = resultado.groups()

    return resultado


def falante(linha):
    regexFalante = "[AO]\sSRA?.\s(.*)"

    resultado = re.search(regexFalante, linha)

    if resultado:
        resultado = resultado.groups()[0].strip()
    elif linha == "(DO PODER EXECUTIVO)":
        resultado = "PODER EXECUTIVO"

    return resultado

def parteFala(linha):
    return not (
        linha.isupper() or
        linha.isdigit() or
        linha == "/" or
        linha.startswith("Sessão de:") or
        linha.startswith("Notas Taquigráficas"))



def parseSessao(sessao, presidente):
    resultado = []
    falanteAtual = ""

    for linha in sessao.split("\n"):
        if falante(linha):
            if falanteAtual:
                if falanteAtual == "PRESIDENTE":
                    falanteAtual = presidente.upper()

                infos = (falanteAtual.strip().replace(",", ""), partidoAtual.strip(), estadoAtual.strip(), fala.strip())
                fala = ""
                partidoAtual = "N/A"
                estadoAtual = "N/A"
                resultado.append(infos)

            falanteAtual = falante(linha)

        if falanteAtual:
            if partidoEstadoFala(linha):
                partidoAtual, estadoAtual, fala = partidoEstadoFala(linha)
            elif parteFala(linha):
                fala += " " + linha

    return resultado

DOC = "previdencia_07-08-17h"

def main():
    sessao = arquivoParaString("../data/extract-texts-pdf/"+DOC+".txt")
    parsed = parseSessao(sessao, "Rodrigo Maia")
    escreveListaEmArquivo(parsed, "../data/process-texts/"+DOC+"-PT.txt")


sessao = arquivoParaString("../data/extract-texts-pdf/"+DOC+".txt")

if __name__ == "__main__":
    main()

