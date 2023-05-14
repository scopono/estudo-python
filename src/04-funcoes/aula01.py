""" Aula 01 - Introdução às Funções"""

# Função → Bloco de código que realiza uma tarefa específica
# Dividir o problema em pequenas partes
# Evitar duplicação de código

# 1. Funções da Standard Library Functions - built-in functions (vieram com o python)
## ex.: print, len etc
### print('Olá', 123, True)
### nomes = ['João', 'Maria']
### tamanho_lista = len(nomes)
### print(nomes, tamanho_lista)

# 2. User Defined Functions - Definidas pelo desenvolvedor(a)
# Fazerem parte da solução do problema

# Declarar funções
## nome: saudacoes
## parametros: nenhum
## retorno: nenhum
def cumprimento():
    print('Olá')

cumprimento()

## nome: saudacoes
## parametros: nome
## retorno: nenhum

def saudacoes(nome):
    print(f'Olá {nome}')

### Chamada
### valores, variáveis, expressões que entram no parâmetro: **argumentos**

saudacoes('Joao') ### 'Joao' é um argumento passado para o parâmetro nome
nome = 'Carlos' ### parâmetro nome != variável nome
saudacoes (nome) ### Pode passar tanto literais quanto variáveis

## Declaração
## nome: calcular_media
## parâmetros: nota1, nota 2, nota 3
## retorno: nenhum

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    print(media)

## Chamada
calcular_media(10.0, 3.0, 6.0)
n1 = 10.0
n2 = 3.0
n3 = 8.0
### argumentos são variáveis
calcular_media(n1, n2, n3)

## Declaração
## nome: calcular_media
## parâmetros: nota1, nota 2, nota 3
## retorno: media

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

## Chamada
media = calcula_media(10.0, 8.4, 3.2)
print('valor da média', media)
### enviar no email
### salvar no banco de dados
### salvar no arquivo
