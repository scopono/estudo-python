""" Exercício 02 - Média Split"""

while 1: 
    x = 0
    notas = input('Insira suas notas no formato "nota 1, nota 2, nota 3, ...": ')

    lista_de_notas = notas.split(sep=', ')
        
    print(lista_de_notas)

    soma = 0.0
    for nota in lista_de_notas:
        if 0 <= float(nota) <= 10:
            soma += float(nota)
        else:
            print('Você inseriu uma nota inválida')
            x = 1
    if x == 1:
        continue

    media = soma/len(lista_de_notas)
    print(media)

    if media > 6.0:
        print(f'Parabéns! Você foi aprovado com {media} na média.')
    elif 4.0 <= media <= 6.0:
        print(f'Você está de recuperação com média de {media}')
    else:
        print(f'Você foi reprovado com média de {media}')
    break
