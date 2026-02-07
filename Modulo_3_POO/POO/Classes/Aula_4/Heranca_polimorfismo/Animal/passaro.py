from animal import Animal

class Passaro(Animal):
    def emitirSom(self):
        return (f"{self.__class__.__name__ }:{self.nome} está piando")
    