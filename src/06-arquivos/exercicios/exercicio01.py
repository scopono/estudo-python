""" Exercício 01 - Arquivos com prontuário, nome e email"""

def carregar_dados_alunos(arquivo):
    lista_dict = []
    for linha in arquivo:
        dicionario = {}
        linha = linha.strip()
        dados = linha.split(sep=',')
        dicionario['prontuario'] = dados[0]
        dicionario['nome'] = dados[1]
        dicionario['email'] = dados[2]
        lista_dict.append(dicionario)
    tupla = tuple(lista_dict)
    return tupla

with open('src/06-arquivos/exercicios/dados_alunos.txt', 'r', encoding="utf-8") as alunos:
    dados_alunos = carregar_dados_alunos(alunos)
    print(dados_alunos, type(dados_alunos))
