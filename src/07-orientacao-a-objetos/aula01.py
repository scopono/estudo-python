""" Aula 01 - Introdução a Orientação a Objetos"""

# A orientação a objetos é um paradigma de programação, isto é, uma forma de programar para resolver algum problema
# Dessa forma, objetos são utilizados em tempo de execução para resolver problemas e trocarem mensagens entre si

# Calcular a área e o perímetro de um retângulo
## area = base * altura
## perímetro = 2 * (base + altura)
## É necessário uma estrutura para armazenar os valores necessários para os cálculos, como:

retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}

retangulo2 = {
    'base': 6.0,
    'altura': 3.0
}


## Solução com funções:
## Os dados do problema estão separados das funções que manipulam esses dados (dados estruturados em um local enquanto a lógica
## que manipulam esses dados para fazer os cálculos estão em outros) (programcação procedural e funcional)
def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print(calcular_area(retangulo1))
print(calcular_area(retangulo1))
print(calcular_perimetro(retangulo1))
print(calcular_perimetro(retangulo1))

## Solução com orientação a objetos:

### Classe representa um conceito
### Classe repreesnta um retângulo
### *Classe concilia a estrutura de dados e os métodos que manipulam os dados*
### Classe possui atributos: base e altura (variáveis na classe que cada objeto vai ter)
### Classe possui métodos
class Retangulo:
    def __init__(self, base, altura): #### Construtor (Não pode ser outro nome) ### Parâmetro self → Representa o objeto que está sendo chamado
        self.base = base #### Atributo base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

### Instanciando objetos do tipo retangulo
### Chamando o método construtor da classe para criar objetos em memória
retangulo1 = Retangulo(10.0, 5.0) #### self → objeto retangulo1 (self é um parâmetro escolhido por convenção)
retangulo2 = Retangulo(6.0, 3.0) #### Acrescentando atributos para o objeto chamado

print(type(retangulo1), retangulo1)
print(type(retangulo2), retangulo2)

print(
retangulo1.base,
retangulo1.altura,
retangulo1.calcular_area(),
retangulo1.calcular_perimetro()
)

print(
retangulo2.base,
retangulo2.altura,
retangulo2.calcular_area(),
retangulo2.calcular_perimetro()
)



