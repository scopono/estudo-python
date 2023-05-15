""" Exercício 03 - Função de Soma com Tupla"""
breakpoint()
def somar(n1, n2, n3):
    return n1 + n2 + n3

valores = []
contador = 0
while contador <= 2:
    entrada_valor = float(input('Insira uma parcela para a soma: '))
    valores.append(entrada_valor)
    contador += 1

print('O valor da soma é :', somar(*valores))