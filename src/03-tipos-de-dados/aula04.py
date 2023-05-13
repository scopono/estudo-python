""" Aula 04 - Tipos de Dados - Dicionário"""

# dicionário
# coleção de key-value, isto é, valores indexáveis pela chave.
# key é única (sem chaves duplicadas)
# mutável

# criar um dicionário
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
print(carro, type(carro))

# acessar valores por chaves
print(carro["marca"])
print(carro.get("marca"))

# pegar todas as chaves, valores e pares
print(carro.keys())
print(carro.values())
print(carro.items())

#verifica se a chave existe
print("marca" in carro)
print("cor" in carro)

# adicionar chave/valor de forma dinâmica
carro["cor"] = 'Azul'
print("cor" in carro)
print(carro, type(carro))

# retirar elementos
marca = carro.pop("marca") ## .pop retorna o valor que estava dentro da key antes de retirá-la
print(marca)
print(carro)

# loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys(): ## É possível tirar o .keys() que ele já irá pegar as chaves
    print(key)

## Os pares key/value são processsados como tuplas, então as variáveis key, valor estão fazendo a função de unpack
for key, valor in carro.items():
    print(key, valor)

## lista de dicionários

aluno1 = {
    'nome': 'João',
    'email': 'joao@email.com',
    'notas': [8.0, 5.2, 2.0]

}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@email.com',
    'notas': [3.0, 2.3, 10.0]

}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'], aluno['notas'])
    for nota in aluno['notas']:
        print(nota)

# for aluno in alunos:
#     for key, value in aluno.items():
#         print(key, value)
