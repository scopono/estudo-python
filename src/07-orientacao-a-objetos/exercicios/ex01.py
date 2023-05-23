""" Exercício 01 - Classe Aluno"""

from classes import aluno

dados_aluno1 = 'SP0101,João da Silva,joao@email.com'
dados_aluno2 = 'SP0101,Leonardo Souza,leo@gmail.com'
dados_aluno3 = 'SP2301,Ana Reis,ana@gmail.com'
aluno1 = aluno.Aluno(dados_aluno1)
aluno2 = aluno.Aluno(dados_aluno2)
aluno3 = aluno.Aluno(dados_aluno3)

alunos = [aluno1, aluno2, aluno3]

print(alunos)
print(alunos.count(aluno2))
