""" Aula 04 - Propriedades """

# As propriedades são uma forma de controlar acesso aos atributos de uma instância
# formas personalizadas de obter e alterar o valor de um atributo.

class Retangulo:
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura
    # getter
    @property # Propriedade para acessar o valor de base
    def base(self):
        return self._base # está com underline pois o setter vai utilizar assim
    
    # setter 
    @base.setter # Propriedade para mudar o valor de base
    def base(self, value):
        # Antes de atribuir o valor passado pra base, podemos criar uma validac'~ao
        if value <= 0.0:
            raise ValueError('A base deve ser maior que zero')
        self._base = value
        
    # getter
    @property
    def altura(self):
        return self._altura

    # setter
    @altura.setter
    def altura(self, value):
        if value <= 0.0: # Para a execução do programa caso seja true (if de claúsula de guarda)
            raise ValueError('A altura deve ser maior que zero') # Para o programa e não atribui o valor.
        self._altura = value

    @classmethod 
    def from_list(cls, lista): 
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
retangulo1 = Retangulo(2.0, 3.0)
retangulo2 = Retangulo(2.0, -1)

# retangulo1.base = -30.0 # Não pode ser esse valor, sendo necessário dar propriedades para a classe não aceitar qualquer valor.
print(retangulo1.base)