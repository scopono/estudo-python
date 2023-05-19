""" Exercício 3.5 - Linhas para dicts (teste)"""

def linha_para_dict(arquivo, chaves):
    lista_dict = []
    contador = 0
    acumulador = 0
    chaves_a_frente = 0
    for linha in arquivo:
        dicionario = {}
        linha = linha.strip()
        valores = linha.split(sep=',')
        for i in range(len(valores)):
            if contador >= 1:
                dicionario[chaves[i + chaves_a_frente]] = valores[i]
            else:
                dicionario[chaves[i]] = valores[i]
            acumulador += 1
        lista_dict.append(dicionario)
        contador += 1
        chaves_a_frente = acumulador
    return lista_dict

lista_chaves = []

while True:
    chave_input = input('Adicione uma chave desejada para o valor no arquivo (digite -1 para encerrar o input): ')
    if chave_input == '-1':
        break
    else:
        lista_chaves.append(chave_input)
    
with open ("src/06-arquivos/exercicios/linhas_pra_dicts(teste).txt", "r", encoding="utf-8") as dados:
    informacoes = linha_para_dict(dados, lista_chaves)
    print(informacoes, type(informacoes))