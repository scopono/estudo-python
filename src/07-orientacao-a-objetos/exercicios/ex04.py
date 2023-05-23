class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto_associado):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto_associado = projeto_associado
        self.participacoes = []

    def __str__(self):
        return f'Participacao[código = {self.codigo}, data de início = {self.data_inicio}, data de término = {self.data_fim}, aluno = {self.aluno}, projeto associado = {self.projeto_associado}, projetos anteriores = {self.participacoes}]'
    
    def add_participacao(self, *args):
        for participacao in args:
            self.participacoes.append(participacao)

participacao_projeto_aluno1 = Participacao(3213132, '07/04/2026', '24/11/2027', 'Batista Ferreira', 'Montagem de um mini carro')
participacao_projeto_aluno1.add_participacao('Vislab', 'Criação de ChatBot')

print(participacao_projeto_aluno1)

