""" Exercício 03 - Mês do Ano com Dicionário"""
dados_numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

meses = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}

numero = input('Digite um número de 1 a 12 para o nome do mês: ')

if numero in dados_numeros:
    print(meses[numero])
else:
    print('Valor inválido')
