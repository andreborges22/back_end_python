class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

<<<<<<< HEAD

class Carro:
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        # composição: o motor nasce junto com o carro
        self.motor = Motor(potencia)


try:
    carro = Carro("Ferrari", 120)
    print(carro.motor.potencia)
    del carro
    print(carro.motor.potencia)
except Exception as e:
    print(f"Erro: {e}")
=======
class Carro:
    def __init__(self, modelo,potencia):
        self.modelo = modelo
        self.motor = Motor(potencia)  # composição: o motor nasce junto com o carro

try:
    carro1 = Carro("Ferrari",120)
    print(carro1.motor.potencia)
    del carro1
    print(carro1.motor.potencia)
except Exception as e:
    print(f"Erro: {e}")
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
