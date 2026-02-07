class Motor:
    def __init__(self,potencia):
        self.potencia = potencia

    def __str__(self):
        return f"Potência: {self.potencia} hp"

class Carro:
    def __init__(self,modelo,potencia):
        self.modelo = modelo
        #composicao
        self.motor = Motor(potencia)

try:
    carro = Carro("Gol 1.0",70)
    print(carro.modelo)
    print(carro.motor)
    del carro
    print(carro.motor)
except Exception as e:
    print(f"Erro({e})")