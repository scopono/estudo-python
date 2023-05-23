import moeda

preco = float(input('Digite o preço: RS$'))
preco_dobro = moeda.dobro(preco)
preco_metade = moeda.metade(preco)

print(f'A metade de RS${preco} é RS${preco_metade}.')
print(f'o dobro de RS${preco} é RS${preco_dobro}.')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 10%, temos R$ {moeda.diminuir(preco, 10)}')
