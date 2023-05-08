""" Aula 05 - Tipos de Dados """

# Numéricos
# int, float

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# Dado de tipo String
nome = 'João'
sobrenome = 'dos Santos'
nome_completo = nome + ' ' + sobrenome  # Concatenação de Strings
print(nome_completo)

produto = 'Pepsi'

# O cliente nome_completo comprou o produto
# f → Interpolação de variáveis
print(f'O cliente {nome} {sobrenome} comproiu o produto')

# Strings funcionam como listas de caracteres
nome = 'Renato'
print(nome[0], nome[-1])

# Métodos da String → Trabalham como as funções, só que acabam sendo sub-rotinas atreladas a objetos de um certo tipo, que no caso é o objeto
# string.

print(nome.lower())
print(nome.upper())

# Separator → É definido como ' ' por padronizado e define a distância de impressão de cada variável, podendo ser ajustado através de:
# sep '*caracteres que irão separar*'
print(1, 3, 7, 10, 'dsadsa', sep='XXXX')

# Tipo de dado Boolean

resultado = 10 < 3
print(resultado, type(resultado))

# Listas
frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
# print(frutas[3]) #IndexError

frutas[0] = 'banana grandona'
frutas.append('abacaxi')  # .append → Acrescenta um elemento na lista
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

# Tupla
codigos = ('SP01', 'SP02', 'SP03')
print(codigos[0])

# codigos [0] = 'SP05' # TypeError
# codigos.append (erro)
# Não pode usar os dois comandos acima pois tentam modificar a trupla, que é imutável.

print(len(codigos))

# Conjuntos
# Arranjo aleatório e sem elemento repetido
resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(23)
print(resultado_sorteio)

# Dicionários
funcionario = {
    'codigo': 123,
    'nome': 'Maria da Silva',
    'salario': 7000.00

}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())

funcionario['salario'] = 9000.00
print(funcionario)
