""" Exercício 03 - Linha para dict"""

def linha_para_dict(arquivo, chaves):
    dicionario = {}
    for linha in arquivo:
        linha = linha.strip()
        valores = linha.split(sep=',')
        for i in range(len(valores)):
            chave = chaves[i]
            dicionario[chave] = valores[i]
    return dicionario

lista_chaves = []

while True:
    chave_input = input('Adicione uma chave desejada para o valor no arquivo (digite -1 para encerrar o input): ')
    if chave_input == '-1':
        break
    lista_chaves.append(chave_input)
    

with open ("src/06-arquivos/exercicios/linha_pra_dict.txt", "r", encoding="utf-8") as dados:
    informacoes = linha_para_dict(dados, lista_chaves)
    print(informacoes, type(informacoes))