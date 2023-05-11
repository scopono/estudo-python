""" Aula 04 - while"""

# O while é um loop como um for que usamos quando não sabemos antecipadamente o número de elementos de uma lista ou não está em memória
# completamente.

# Por exemplo, um arquivo com 3000 linhas e se deseja encontrar uma palavra em um determinado local do arquivo. Ao invés de trazer o arquivo
# todo para a memória e percorrer essas 3000 linhas com o for, o while pode ser utilizado para ler linha por linha para, quando achar a 
# palavra, o arquivo poder ser fechado.

# Dessa forma, o while pode ser usado para leitura de arquivos, bancos de dados que usam cursores etc.

# while condicao:
#   instrucao
#   instrucao

contador = 0
while contador <= 10:
    print(contador)
    contador += 1

# linha = arquivo.readline()
# while linha:
#     instrucao linhalinha = arquivo.readline()

