from animal import Animal

class Gato(Animal):
    def emitirSom(self):
        return (f"{self.nome} está miando")
    
gato = Gato("Tom")
print(gato.emitirSom())