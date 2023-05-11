""" Aula 03 - Loop for"""

# 1. Iteração em coleção de elementos
# 2. Repetir instrução

linguagens = ['C', 'Python', 'Java']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for valor in colecao: 
#   instrucao
#   instrucao
#   instrucao

## Comportamenteo do operador in é diferente com base no contexto

for linguagem in linguagens:
    print(linguagem.upper())

nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3)/3
print(media)

notas = [10.0, 5.5, 8.3, 2.5]

soma = 0.0
for nota in notas:
    soma = soma + nota

media = soma/len(notas)
print(media)

# range:
## start → contagem inicial, que é 0 por padrão
## stop → contagem final
## step → de quanto em quanto conta, que por padrão é +1
valores = range(10)
valores = range(0, 10, 2)
valores = range(10, 0, -2)

for valor in valores:
    print(valor)


## Pode ser utilizado para imprimir arrays
for i in range(len(linguagens)):
    print(linguagens[i])
