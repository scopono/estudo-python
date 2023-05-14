""" Exercício 04 - Função de Soma com Args"""

def somar(*args):
    soma = 0
    for parcela in args:
        soma = soma + parcela
    return soma

resultado = somar(1.5, 2.5, 5.0, 11.0)
print(resultado)
