""" Exercício 02 - Mês do Ano com Tupla"""
dados_numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

numero = input('Digite um número de 1 a 12 para o nome do mês: ')
if numero in dados_numeros:
    mes = int(numero) - 1
    print(meses[mes])
else:
    print('Valor inválido.')
