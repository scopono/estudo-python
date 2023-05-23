""" Exercício 01 - Classe Aluno"""

class Aluno:
    def __init__(self, dados):
        prontuario, nome, email = dados.split(sep=',')
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value == "":
            raise ValueError("Insira algum valor no prontuário!")
        self._prontuario = value
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if value == "":
            raise ValueError("Insira algum valor no nome!")
        self._nome = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if value == "":
            raise ValueError("Insira algum valor no email!")
        self._email = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)
    
    def __repr__(self):
        return f'Aluno(prontuario = {self.prontuario}, nome = {self.nome}, email = {self.email})'
    
dados_aluno1 = 'SP0101,João da Silva,joao@email.com'
dados_aluno2 = 'SP0101,Leonardo Souza,leo@gmail.com'
dados_aluno3 = 'SP2301,Ana Reis,ana@gmail.com'
aluno1 = Aluno(dados_aluno1)
aluno2 = Aluno(dados_aluno2)
aluno3 = Aluno(dados_aluno3)

alunos = [aluno1, aluno2, aluno3]

print(alunos)
print(alunos.count(aluno2))
