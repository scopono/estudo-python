""" Exercício 01 - Maior/menor elemento"""

numeros = []
contador = 1

while contador <= 3:
    numero = float(input('Insira um número no campo a seguir: '))
    numeros.append(numero)
    contador += 1

menor = numeros[0]
maior = numeros[0]

for i in numeros:
    if i <= menor:
        menor = i
    if i >= maior:
        maior = i

if menor == maior:
    print('Todos os números da lista são iguais!')
else:
    print(f'O menor número é {menor}, enquanto o maior número é {maior}.')
