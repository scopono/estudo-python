""" Aula 08 - Heranças entre Classes com super()"""

# Há as classes mães (superclasses), que sõa as classes principais, e as sub-classes, que irão herdar as informações.

class Pessoa: #SUPER CLASSE
    def __init__(self, nome, sobrenome, cpf):           #4
        print("ENTREI NA SUPER CLASSE")                 #5
        self.nome = nome                                #6
        self.sobrenome = sobrenome                      #7                      
        self.cpf = cpf                                  #8
    
    def obtem_nome_completo(self):                      #11
        return f'{self.nome} {self.sobrenome}'          #12
    
class Cliente(Pessoa): # SUB-CLASSE # O parâmetro faz herança dos atributos da classe Pessoa 
    # Herdados através do parâmetro:
    ## self.nome = nome
    ## self.sobrenome = sobrenome 
    ## self.cpf = cpf 
    pass       

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):                                   #2
        super().__init__(nome, sobrenome, cpf) # super() → Chama a super classe          #3
        self.salario = salario                                                           #9
    def calcula_pagamento(self):
        return self.salario - (10/100) * self.salario

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento() # especificidade
        return pagamento_salario + self.bonus

# cliente = Cliente("Paulo", "Mulotto", "123.123.123-12")                                  
funcionario = Funcionario("João", "Reis", "322.512.623-30", 3500)                            #1
programador = Programador("José", "Augusto", "123.123.123-33", 4000, 500)
print(funcionario.obtem_nome_completo())                                                     #10
print(funcionario.salario)                                                                   #13
print(funcionario.calcula_pagamento())
print(programador.calcula_pagamento())