from veiculo import Veiculo

class VeiculoVoador(Veiculo):
    def voar(self):
        print(f"{self.nome} está voando.")