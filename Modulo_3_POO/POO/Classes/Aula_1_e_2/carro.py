class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"Acelerando! Velocidade: {self.velocidade} km/h")
    
    def frear(self):
        self.velocidade = 0
        print("Freando...")
        print("Carro parado.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo} Ano: {self.ano}")
    
    def ligar(self):
        print("Carro ligado")

# Criando objetos
meu_carro = Carro("Toyota", "Corolla", 2023)
meu_carro.exibir_informacoes()
meu_carro.ligar()
#meu_carro.acelerar(50)
#meu_carro.frear()