""" Exercício 04 - Participacao com adição de outras participações"""

from classes import participacao

participacao_projeto_aluno1 = participacao.Participacao(3213132, '07/04/2026', '24/11/2027', 'Batista Ferreira', 'Montagem de um mini carro')
participacao_projeto_aluno1.add_participacao('Vislab', 'Criação de ChatBot')

print(participacao_projeto_aluno1)