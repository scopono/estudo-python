""" Aula 01 - Manipulando Arquivos (1)"""

# open("caminho", "r")

## Mode
### r - Leitura
### a - Append/Incrementar
### w - Escrita
### x - Criar arquivos
### r+ - Leitura + Escrita

arquivo = open("src/06-arquivos/texto.txt", "r")

# Leitura
## print(arquivo.readable()) ## Indica um valor booleano para falar se o arquivo pode ser lido ou não.
## print(arquivo.read()) ## Retorna todo o conteúdo do arquivo
### PS: Se der arquivo.read() de novo, ele vai retornar uma string vazia, porque ele trabalha como um curso que vai do início até o final
### do arquivo. Dessa forma, quando chamamos a função read() novamente, não	há	mais conteúdo pois ele todo	já foi lido
### Entretanto, podemos fecharo  arquivo com arquivo.close() para poder ler ele novamente.
## print(arquivo.readline()) ## Lê apenas uma linha
## print(lista)
## print(lista[3]) 

# Escrita

arquivo = open("src/06-arquivos/texto.txt", "a") 
## Tomar cuidado ao usar o "write" pois ele limpa o arquivo que já existe e escreve algo no aruqivo existente
## arquivo.write("\nPascal") ## Irá escrever no arquivo, mas colado com outra linguagem de programação, podendo ser usado o \n para pular linha.
## arquivo.write("\nC++")
## arquivo.write("\nTerraform")

# Criação de arquivos
## arquivo = open("src/06-arquivos/texto2.txt", "x") ## Pode ser usado também o "w" para criar arquivos
# arquivo.close() ## Fecha o arquivo para que seja possível acessar e/ou alterar o arquivo com outros sistemas, como com o Windows Explorer.

## Remoção de arquivos

import os

if os.path.exists("src/06-arquivos/texto2.txt"):
    os.remove("src/06-arquivos/texto2.txt") ## remove arquivos
else:
    print("Arquivo não existe.")

os.rmdir("src/06-arquivos/nova_pasta") ## remove pastas vazias

arquivo.close()
