class Veiculo:
    def dirigir(self):
        return "Veículo em movimento"

    def descricao(self):
        return f"{self.__class__.__name__}: {self.dirigir()}"


class Carro(Veiculo):
    def dirigir(self):
        return ""


class Moto(Veiculo):
    def dirigir(self):
        return ""


class Caminhao(Veiculo):
    def dirigir(self):
        return ""


# Programa principal
veiculos = [Carro(), Moto(), Caminhao()]

for v in veiculos:
    print(v.descricao())
