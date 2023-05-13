"""Aula 01 - Tipos de Dados - Listas"""

# lista
# ordenadas (botou na posicao 1, fica na posicao 1)
# mutáveis (pode editar os elementos da lista)
# indexáveis (acessar via index, isto é, pegar um elemento de uma determinada posicao através de um índice)

# criação da lista
nomes = ['Maria', 'Pedro', 'João']
print(nomes, type(nomes))

# acessar elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'João Santos']
print(nomes)

# tamanho de uma lista
print(len(nomes))

# adicionar elementos na lista
nomes.append('Marta Gomes')
print(nomes)

# método insert
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana Lucia')
print(nomes)

# método extend
nomes2 = ['Kaio Silva', 'Carlos Gomes']
nomes.extend(nomes2)
print(nomes)

# remover elementos

#remove

nomes.remove('Maria da Silva')
print(nomes)

# del

del nomes[0]
print(nomes)

# remove da memória, inclusive a lista
# del nomes
# print(nomes)

# método clear
# limpa a lista
nomes.clear()
print(nomes)

# iteração em lista
for nome in nomes:
    print(nome)

print('-----')

for i in range(len(nomes)):
    print(nomes[i])