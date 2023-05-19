""" Exercício 02 - Arquivos com código, título e responsável"""

def carregar_dados_projetos(arquivo):
    lista_dict = []
    for linha in arquivo:
        linha = linha.strip()
        dados = linha.split(sep=', ')
        lista_dict.append({'codigo': int(dados[0]),'titulo': dados[1], 'responsavel':dados[2]})
    tupla = tuple(lista_dict)
    return tupla

with open('src/06-arquivos/exercicios/dados_projeto.txt', 'r', encoding="utf-8") as projetos:
    dados_projetos = carregar_dados_projetos(projetos)
    print(dados_projetos, type(dados_projetos))