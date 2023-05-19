""" Aula 02 - Manipulando Arquivos (2)"""

# arq = open('src/06-arquivos/arquivo.txt', 'w', encoding='utf-8')

# string = 'Olá, tudo bem?'
# string = ['Olá', 'Caio', 'Tudo']

# arq.write('Ola tudo bem?\n') # Escreve uma string
# for nome in string:
#     arq.write(nome + '\n')
# arq.writelines(string) # Escreve uma lista de strings, isto é, um iterável de strings
# arq.write('Caio\nMarcos\nJoão')
# arq.close()

# forma correta de se trabalhar com arquivos
with open('src/06-arquivos/arquivo.txt', 'a') as arq: #somente no escopo do with que tem acesso ao arq, não precisando do arq.close() (context manager)
    arq.write('teste\n')
with open('src/06-arquivos/arquivo.txt', 'r') as arq:
    x = arq.readlines()
    print(type(x))

with open('src/06-arquivos/arquivo.txt', 'r') as arq:
    x = arq.read()
    print(type(x))

with open('src/06-arquivos/arquivo.txt', 'rb') as arq: ## rb - lê o conteúdo do arquivo em instância de bytes (tráfego de dados por redes)
    x = arq.read()
    print(type(x))

with open('src/06-arquivos/arquivo.txt', 'rb') as arq: 
    x = arq.read()
    print(type(x.decode())) ## decodifica o binário

with open('src/06-arquivos/arquivo.txt', 'r') as arq: 
# vai imprimir separado pois o print possui como padrão o \n, sendo possível usar a função strip() para retirar os caracteres especiais
    for i in arq:  
        print(i)

with open('src/06-arquivos/arquivo.txt', 'r') as arq: 
    print(next(arq))
    print(next(arq))

    