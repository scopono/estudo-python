""" Exercício 02 - Função de Soma com Retorno"""

def somar(n1, n2, n3):
    resultado = n1 + n2 + n3
    return resultado

valor1 = float(input('Insira o primeiro número: '))
valor2 = float(input('Insira o segundo número: '))
valor3 = float(input('Insira o terceiro número: '))

soma = somar(valor1, valor2, valor3)
print(soma)