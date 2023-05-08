""" Aula 04 - Variáveis, Constantes e Literais """

# Varia'vel é um container para guardar um dado ou ser um ponteiro para outro valor
# Diferente de C, há inferência de tipo, ou seja, o Python consegue analisar um valor e classificá-lo como inteiro, real etc.

numero = 10
print(numero)
print(type(numero))

# alteração do valor de variavel
numero = 20
print(numero)

# múltiplas atribuições, mas que acaba não sendo uma boa prática
nome, idade, endereco = 'Maria', 20, 'Rua das...'
print(nome, idade, endereco)

nome = 'Maria'
idade = 20
endereco = 'Rua das...'
print(nome, idade, endereco)

# atribuição de mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

# Status agora: nome1 = 'João'; nome2 = 'João'; nome3 = 'João';
nome2 = 'Pedro'
print(nome1, nome2, nome3)
# Status agora: nome1 = 'João'; nome2 = 'Pedro' (foi reatribuído); nome3 = 'João';

# snake_case
id_funcionario = 209
# camelCase
salarioAtual = 5000.50
print(id_funcionario, salarioAtual)

# Constantes
# Upper case - snake_case

PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais → Representações de valores fixos em um programação, como literais de inteiro (20, -1, -1666, etc), literais de reais
# (-2.5, 3/1.3 etc)
idade = 27
print(idade)
print(27)  # 27 = Literal de inteiro

# Numéricos
print(10, type(10))
print(-10, type(-10))
print(10.5, type(10.5))

# String
print('Maria', type('Maria'))
print("Maria", type("Maria"))
# PS: Aspas duplas e aspas simples são duas maneiras iguais de representar uma string, mas é bom se manter em apenas uma delas, ou seja,
# não ficar alternando durante o código, e alternar quando ser necessário utilizar aspas simples ou aspas duplas em uma string, como em
# "John's house" e em 'O filme estava "excelente"'.

# Docstring possuem a convenção de serem escrita em aspas duplas.

# Booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções

# Lista (list)
numeros = [1, 3, 5]
print(numeros, type(numeros))  # Mutável

# Tupla (tuple)
emails = ('joao@email.com', 'maria@email.com')  # Imutável
print(emails, type(emails))

# Conjunto (set)
# Não permite itens duplicados e não garante uma ordem
nomes = {'maria', 'joão', 'pedro', 'maria'}
print(nomes, type(nomes))
# Dicionário (dictionary)
aluno = {
    'prontuario': 123456,
    'nome': 'Maria da Silva',  # Também usa chaves, mas separa elementos em pares
    'idade': 34
}
print(aluno, type(aluno))
