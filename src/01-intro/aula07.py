""" Aula 07 - Entrada e Saída de Dados (Input and Output)"""

# saída padrão - sys stdout (standard output do sistema)
print('hello world', 'Maria')

# Elementos da função print

## values: object → Parâmetro que exibe dados de qualquer tipo

## sep → Interpreta como separador, sendo definido como ' ' por padrão.

## end →　É o último caractere de cada print dado, sendo definido como '\n' por padrão, ou seja, pula linha.

print('hello world', 'Maria', True, sep='&', end='??????\n')
print('hello world', 'Maria', True, sep='&', end='??????\n')

# Jogar valores imprimidos em um arquivo ao invés no standard output system
## Abre o arquivo de texto e cria um se não existir um antes e tiver o parâmetro 'w' de write
arquivo = open('nomes.txt', 'w', encoding='utf-8') 
## Imprime o texto para dentro do arquivo
print(
    'joao@email.com',
    'maria@email.com',
    'pedro@email.com',
    file=arquivo,
    sep=';'
) 

# Entrada/input
# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# ## idade = int(idade)
# print(type(nome), type(idade))

# if idade >= 18:
#     print(f'{nome}, você é maior de idade')
# else:
#     print(f'{nome}, você é menor de idade')

# file
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
## Quebra a string através de um separador, que irá procurar o caractere indicado nele e assim fazer uma lista
notas = conteudo.split(sep=';')
notas = [float(nota) for nota in notas]
print(notas)

media = (notas[0] + notas[1] + notas[2])/ len(notas)
print(media)
