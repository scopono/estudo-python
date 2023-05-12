""" Aula 03 - Exercício Identificação"""

identificacao = input('Coloque a sua identificação no campo a seguir: ')
checa_tamanho = len(identificacao) == 7
tem_quatro_zeros = '0000' in identificacao

if checa_tamanho and not tem_quatro_zeros:
    checa_inicio = identificacao[0] == 'B' and identificacao[1] == 'R'
    checa_fim = identificacao [6] == 'X'
    if checa_inicio and checa_fim:
        print(f'A identificação {identificacao} registrada é válida.')
    else: 
        print(f'A identificação {identificacao} registrada não é válida.')
else:
    print(f'A identificação {identificacao} registrada não é válida.')