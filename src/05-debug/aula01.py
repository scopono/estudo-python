""" Aula 01 - Debug PDB"""

def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

def calcular_media(n1, n2, n3):
    soma = somar(n1, n2, n3)
    media = soma/3
    return media

# Para a execução do código, mostrando em qual instrução e linha o python está em tempo de execução e fornecendo um terminal (Pdb)
## help/help (comando) → lista de comandos que podem ser executados no debugger do python/definição do comando
## next → Pula para a próxima instrução que será executada pelo código
## *nome de variável* → Informa o valor de uma variável JÁ EXECUTADA
## exit → Sai do debugger
## step → Executa a linha atual e vai parar na primeira ocasião possível (caso seja a chamada de uma função ou função atual).
### Entra em uma função.
## where → Mostra a função e as chamadas atuais

breakpoint()
nota1 = 10.0
nota2 = 3.0
nota3 = 5.5

media = calcular_media(nota1, nota2, nota3)
print(media)