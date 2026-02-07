class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


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
