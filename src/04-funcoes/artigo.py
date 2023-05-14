""" Artigo Args e Kwargs"""

# Args
# Passa diversos argumentos para um mesmo parâmetro, sendo necessário um asterisco do lado do parâmetro
## Args é um nome que apenas é uma convenção de se dar a esse tipo de parâmetro, podendo ser *some_list, *xyz ou *anos
## Basicamente, cria uma lista com os argumentos

def titulos_copa(pais, *args):
    print('País: ', pais)
    for title in args:
        print('Ano: ', title)

titulos_copa('Brasil', '1958', '1962', '1970', '1994', '2002')
titulos_copa('Espanha', '2010')

# Kwargs
## Passa diversos parâmetros e argumentos opcionais para diferentes propósitos
## Basicamente, cria um dicionário opcional com os parâmetros em formato de keyword.

def calcular_preco(valor, **kwargs):
    porcentagem_imposto = kwargs.get('porcentagem_imposto')
    desconto = kwargs.get('desconto')

    if porcentagem_imposto:
        valor += valor * (porcentagem_imposto/100)
    if desconto:
        valor -= desconto
    
    return valor

preco_final = calcular_preco(100.0)
print(preco_final)

preco_final = calcular_preco(100.0, desconto=25.0)
print(preco_final)

preco_final = calcular_preco(100.0, porcentagem_imposto=10.0)
print(preco_final)

preco_final = calcular_preco(100.0, desconto=30.0, porcentagem_imposto=29.0)
print(preco_final)