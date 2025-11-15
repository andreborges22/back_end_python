from animal import Animal

class Gato(Animal):
    def emitirSom(self):
        return (f"{self.__class__.__name__ }:{self.nome} está miando")
