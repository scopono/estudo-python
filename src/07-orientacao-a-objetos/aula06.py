""" Aula 06 - equal e hash code"""

nome1 = 'João' #
nome2 = 'João'
print(nome1 == nome2) # Já possuem o __eq__ e o __hash__ implementados internamente, por isso dão true

class Pessoa:
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    def __eq__(self, value):
        if isinstance(value, self.__class__): 
            return self.cpf == value.cpf # and self.nome == value.nome # verifica se tem o mesmo cpf
        return False
    
    # Hash - gera um hash code para uma string ou numero usado nas coleções para facilitar acessos rápidos objetos em uma coleção e
    # indexar assim os objetos das coleções no hash map.
    def __hash__(self): 
        return hash(self.cpf)
    
    def __repr__(self): # set usa __repr__
        return f'Pessoa({self.cpf}, {self.nome})'


pessoa1 = Pessoa('João', '100100100-10') # set não vai imprimir quando tem eq e hash porque vai considerar que é igual
pessoa2 = Pessoa('João', '100100100-10') # vai achar que são pessoas diferentes sem os métodos eq e hash
pessoa3 = Pessoa('Maria', '100100100-11')

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)

print(pessoa1 == pessoa2) 

pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)

print(pessoas_lista.count(pessoa1))
