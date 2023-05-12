""" Aula 04 - Exercício Identificação"""

identificador = input('Coloque o seu identificador no campo a seguir: ')
dados_numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
erros = []

contador = 0
for i in range(len(identificador)): # Verifica se há uma sequência de quatro números
    if identificador[i] in dados_numeros:
        contador += 1
    else:
        if identificador[-1] in dados_numeros:
            contador = 0


tem_tamanho_ideal = len(identificador) == 7
tem_br = identificador[0] == 'B' and identificador[1] == 'R'
tem_x = identificador [-1] == 'X'
sequencia_errada = contador != 4 or '0000' in identificador

print(contador)
if tem_tamanho_ideal and tem_br and tem_x and not sequencia_errada:
    print(f'O identificador {identificador} registrado é válido.')
else:
    print(f'O identificador {identificador} registrado não é válido.')

if tem_br is False: 
    erros.append('O identificador não inicia com a sequência "BR"')

if tem_x is False:
    erros.append('O identificador não termina com a letra "X"')

if tem_tamanho_ideal is False:
    erros.append('O identificador não possui 7 caracteres')

if sequencia_errada: 
    erros.append('O identificador não apresenta números inteiros entre 0001 e 9999')

for erro in erros:
    print(erro)
    