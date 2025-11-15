from veiculo import Veiculo
from veiculo_voador import VeiculoVoador
from veiculo_flutuante import VeiculoFlutuante

class VeiculoAnfibio(VeiculoVoador, VeiculoFlutuante):
    def __init__(self, nome):
        super().__init__(nome)

# Criando uma instância de VeiculoAnfibio
carro_anfibio = VeiculoAnfibio("Carro Anfíbio")

# Usando métodos herdados
carro_anfibio.dirigir()  # Saída: Carro Anfíbio está dirigindo.
carro_anfibio.voar()     # Saída: Carro Anfíbio está voando.
carro_anfibio.flutuar()  # Saída: Carro Anfíbio está flutuando.