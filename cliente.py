class Cliente: 
    def __init__(self,nome):
        self.__nome = nome
    
    # Fazendo um get (Atributo precisa ser privada e precisa ter o @property )
    @property
    def nome(self):
        return self.__nome.title()
    
    # Fazendo um set (Atributo precisa ser privada e precisa ter o @Atributo.setter )
    @nome.setter
    def nome(self,nome):
        self.__nome = nome