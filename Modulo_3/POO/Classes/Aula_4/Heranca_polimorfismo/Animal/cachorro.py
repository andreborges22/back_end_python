from animal import Animal

class Cachorro(Animal):
    def emitirSom(self):
        return (f"{self.nome} está latindo")
    
cachorro = Cachorro("Caramelo")
print(cachorro.emitirSom())