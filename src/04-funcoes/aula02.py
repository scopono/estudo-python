""" Aula 02 - Argumentos: positional, keyword, default value"""

# Declara uma função que soma dois números
def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo/divisor

# argumentos posicionais
print(somar(10.0, 3.5)) ## n1 = 10.0, n2 = 3.5
print(somar(2.0, 6.5)) ## n1 = 2.0, n2 = 6.5
print(dividir(10.0, 2.0))

# unpack list e tuplas (numero da lista tem que ser igual ao numero de parametros)
# pode também fazer com set, mas não há ordem garantida, então não é recomendado.
numeros = [10.0, 5.5]
print('somar numeros de uma lista', somar(numeros[0], numeros[1]))
print('somar numeros de uma lista', somar(*numeros)) ## Um asterisco indica ao python fazer o unpack de uma lista ou tuplas

# unpack dict
# keys são os parâmetros e os valores são os argumentos
numeros = {
    "n1": 10.2,
    "n2": 5.3

}

print('somar numeros de um dict', somar(**numeros)) ## Dois astericos indica ao python fazer o unpack de um dicionário


# argumentos nomeados (keyword)
print(somar(n1=3.0, n2=6.2)) ## n1 = 3.0, n2 = 6.2
print(somar(n2=5.0, n1=7.8)) ## n1 = 7.8, n2 = 5.0
print(dividir(divisor=3.0, dividendo=10.0))

# Default value
# nome: saudacoes
# parametros: nome (obrigatorio), saudacao (opcional)
# retorno: string

def saudacoes(nome, saudacao='Oi'): ## 'Oi' é o valor padrão caso não seja passado nenhum parâmetro para saudacao
    return f'{saudacao}, {nome}'

print(saudacoes('João', 'Olá'))
print(saudacoes('Maria', 'Bom dia'))
print(saudacoes('Pedro'))

print(saudacoes(saudacao='Oi Oi', nome='Marcio'))
print(saudacoes(nome='Karina'))
