def aumentar(preco, porcentagem):
    return preco + preco * (porcentagem/100)

def diminuir(preco, porcentagem):
    return preco - preco * (porcentagem/100)

def dobro(preco):
    return preco * 2

def metade(preco):
    return preco / 2

def moeda(preco):
    return f'R${preco:0.2f}'.replace('.',',')