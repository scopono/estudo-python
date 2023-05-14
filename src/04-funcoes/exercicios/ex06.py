"""Exercício 06 - Aquário"""

def volume(aquario):
    return (aquario['comprimento'] * aquario['altura'] * aquario['largura'])/1000

def potencia(aquario):
    return aquario['volume'] * 0.05 * (aquario['temp_desejada'] - aquario['temp_ambiente'])

def filtragem(aquario):
    return 2.5 * aquario['volume']

aquario = {
    'comprimento': 0,
    'altura': 0,
    'largura': 0,
    'temp_desejada': 0,
    'temp_ambiente': 0,
    'volume': 0,
    'potencia_termostato': 0,
    'filtragem_hora': 0
}

aquario['comprimento'] = float(input('Insira o comprimento do aquário: '))
aquario['altura'] = float(input('Insira a altura do aquário: '))
aquario['largura'] = float(input('Insira a largura do aquário: '))
aquario['temp_desejada'] = float(input('Insira a temperatura desejada para o aquário: '))
aquario['temp_ambiente'] = float(input('Insira a temperatura ambiente para o aquário: '))
                                 
aquario['volume'] = volume(aquario)
aquario['potencia_termostato'] = potencia(aquario)
aquario['filtragem_hora'] = filtragem(aquario)

for chave, valor in aquario.items():
    print(chave, valor)
