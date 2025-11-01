from animal import Animal

class Passaro(Animal):
    def emitirSom(self):
        return (f"{self.nome} está piando")
    
passaro = Passaro("Piu piu")
print(passaro.emitirSom())