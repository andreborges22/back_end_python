from animal import Animal

class Cachorro(Animal):
    def __init__(self,nome,raca):
        super().__init__(nome)
        self.raca = raca
        
    def emitirSom(self):
        return (f"{self.__class__.__name__ }:{self.nome} está latindo")
