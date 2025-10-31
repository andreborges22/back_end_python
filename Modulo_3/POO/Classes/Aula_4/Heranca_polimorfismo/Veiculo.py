class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def dirigir(self):
        print(f"{self.nome} está dirigindo.")

class Voador:
    def voar(self):
        print(f"{self.nome} está voando.")

class Flutuante:
    def flutuar(self):
        print(f"{self.nome} está flutuando.")

class VeiculoAnfibio(Veiculo, Voador, Flutuante):
    def __init__(self, nome):
        super().__init__(nome)

# Criando uma instância de VeiculoAnfibio
carro_anfibio = VeiculoAnfibio("Carro Anfíbio")

# Usando métodos herdados
carro_anfibio.dirigir()  # Saída: Carro Anfíbio está dirigindo.
carro_anfibio.voar()     # Saída: Carro Anfíbio está voando.
carro_anfibio.flutuar()  # Saída: Carro Anfíbio está flutuando.
