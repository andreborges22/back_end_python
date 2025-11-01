class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

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