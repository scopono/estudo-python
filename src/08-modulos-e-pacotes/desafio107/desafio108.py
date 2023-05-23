import moeda

preco = float(input('Digite o preço: R$'))
preco_dobro = moeda.dobro(preco)
preco_metade = moeda.metade(preco)

print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(preco_metade)}.')
print(f'o dobro de {moeda.moeda(preco)} é {moeda.moeda(preco_dobro)}.')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}.')