""" Aula 02 - Instrução if"""

# Python
# if condicao:
#   instrucao
#   instrucao

# C, Java, C#, outras
# if() {
#   instrucao
#   instrucao
# }

codigo_cliente = 32 # F2 ou Botão Direito → Rename Symbol para alterar o nome da variável
valor_desconto = 23.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print('Desconto Especial!')
    print(codigo_cliente)  # Cada indentação é constituída por 4 espaços, definindo a estrutura do código
else:
    print('Sem desconto especial')

nome = 'Lo'

print(len(nome))

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido')

if not NOME_INVALIDO: 
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')

# nome tem que ter pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas
nome = 'Lo'
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18

if IDADE_INVALIDA:
    erros.append('Idade deve ser maior ou igual a 18')

if len(erros) != 0:
    print(erros)
else:
    print('Dados válidos')

# False: False, None, 0, 0.0, string vazia '', lista, tupla ou set vazios
# True: todo o resto
if erros:
    print(erros)
else:
    print('Dados válidos')

# else if → elif no Python

# Verifica se um número é positivo ou negativo ou zero
numero = 3
if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')

# Calcule a média e verifique se as duas notas são válidas antes do cálculo
n1 = 5.6
n2 = 10.0

# Código Errado
if n1 >= 0 and n1 <= 10:
    if n2 >=0 and n2 <= 10:
        pass
    else:
        print('Notas inválidas')
else:
    print('Notas inválidas')

# Código Certo (na estrutura relacional de C, por exemplo)

if (n1 >= 0 and n1 <= 10) and (n2 >=0 and n2 <= 10):
    pass
else:
    print('Notas inválidas')

# Código Certo (maneira que tem como fazer em Python)

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2)/2
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperacao')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')