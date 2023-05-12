""" Exercício 01 - Média de três notas"""

notas = []
soma = 0


i = 0
while i <= 2:
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    i += 1

for nota in notas:
    soma = soma + nota

media = soma/len(notas)
print(f'A sua média aritmética é {media}')

