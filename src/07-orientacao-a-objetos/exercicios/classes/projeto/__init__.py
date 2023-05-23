numeros_inteiros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Projeto:
    
    def __init__(self, dados):
        codigo, titulo, responsavel = dados.split(sep=',')
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value == "":
            raise ValueError("Insira algum valor no codigo!")
        for caracter in value:
            if caracter not in numeros_inteiros:
                raise TypeError("Insira apenas um número de tipo inteiro no código!")
        self._codigo = value
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if value == "":
            raise ValueError("Insira algum valor no nome!")
        self._titulo = value
    
    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if value == "":
            raise ValueError("Insira algum valor no email!")
        self._responsavel = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)
    
    def __repr__(self):
        return f'Projeto(código = {self.codigo}, título = {self.titulo}, responsável = {self.responsavel})'