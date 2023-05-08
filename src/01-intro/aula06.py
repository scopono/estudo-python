""" Aula 06 - Conversão de Tipos """

# Conversão de tipo implícita e explícita 
# string em um float, boolean em formato de string para transformar em boolean, 
# multiplicar variavel real com variavel inteiro que vai retornar outro tipo etc

# Conversão implícita
leitura = 5.53
peso = 3
total = leitura * peso ## conversão implícita do peso para float

# Conversão explícita (type casting)

## soma = 13.4 + '3.5' ## Funcionaria no PHP e JS, mas o Python é uma linguagem fortemente tipada, então é necessário ser claro com os tipos.
soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = int('27')
print(idade, type(idade))

nome = 'Maria'
altura = 1.70

## mensagem = nome + ' tem a altura de ' + altura ## Vai dar um erro de TypeError, pois não é possível concatenar um flaot com uma string.
mensagem = nome + ' tem a altura de ' + str(altura) ## Maneira através da concatenação
mensagem = f'{nome} tem a altura de {altura}' ## Maneira através da interpolação de variáveis

print(mensagem)