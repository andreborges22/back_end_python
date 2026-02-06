class Pessoa:
    def __init__(self, nome, idade, sexo, altura, peso):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
    
    def apresentar(self):
            print(f"Sou {self.nome}, tenho {self.idade} anos.")

    def envelhecer(self):
            self.idade += 1
            print(f"{self.nome} fez aniversário! Agora tem {self.idade} anos.")

    def calcular_imc(self):
            imc = self.peso / self.altura**2
            return round(imc, 2)
    
p1 = Pessoa("Carlos", 30, 'm', 1.75, 80)
p1.apresentar()

p2 = Pessoa("Maria", 30, 'f', 1.75, 80)
p2.apresentar()
p2.envelhecer()
print(f"IMC: {p2.calcular_imc()}")