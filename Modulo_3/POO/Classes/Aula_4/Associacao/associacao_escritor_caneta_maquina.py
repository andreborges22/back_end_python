class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None  # Associação — não é criada dentro da classe

    def escrever(self):
        if self.ferramenta is not None:
            self.ferramenta.escrever()
        else:
            print(f"{self.nome} não tem nenhuma ferramenta para escrever.")


class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print(f"Escrevendo com a caneta {self.marca}...")


class MaquinaDeEscrever:
    def escrever(self):
        print("Escrevendo com a máquina de escrever...")


# --- Demonstração ---
escritor = Escritor("André")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

# Associação: o escritor usa a caneta
escritor.ferramenta = caneta
escritor.escrever()

# Troca de ferramenta
escritor.ferramenta = maquina
escritor.escrever()

# Mesmo após apagar o escritor, os outros objetos continuam existindo
del escritor
print("\nMesmo sem o escritor, ainda posso usar a caneta e a máquina:")

caneta.escrever()
maquina.escrever()
