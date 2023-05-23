""" Aula 02 - Atributos de classe e instância"""

# classe pessoa possui atributos de instancia (atributos associados a algum objeto criado):
## nome e email
# atributos de classe são atributos associados a classe e não a um objeto em específico.
## 'Humano"
class Pessoa:
    especie = 'Humano'
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')
pessoa3 = Pessoa('Pedro Santos', 'pedro@email.com')

# alterar um atributo de classe na instância (objeto) altera apenas para essa instância

pessoa1.especie = 'Alienigena'

# alterando um atributo de classe na classe altera todos os objetos

Pessoa.especie = 'Alienigenas do Passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)

print(Pessoa.especie)
