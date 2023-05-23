""" Aula 05 - Métodos especiais """

# __stf__(self)
## representação do objeto como string para humanos
# __repr__ (self)
## representação do objeto como string para recriar ese objeto
## logging, debug
## representação canônica do objeto

class Retangulo:
    def __init__(self, base, altura): 
        self.base = base 
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f'Retangulo[base={self.base}, altura={self.altura}]'
    # Recriação única do objeto em memória
    def __repr__(self):
        return f'Retangulo({self.base},{self.altura})'


retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(3.0, 14.0)

retangulo3 = eval('Retangulo(7.5, 12.3)') # Avalia um código passado (que pode ser representado como string) e executa esse código
retangulo4 = eval(repr(retangulo3))
print(retangulo1) # caso não tenha o __str__ ou __repr__, ele não vai mostrar os atributos e seus valores.
print(retangulo2)
print(retangulo3)
print(retangulo4)
