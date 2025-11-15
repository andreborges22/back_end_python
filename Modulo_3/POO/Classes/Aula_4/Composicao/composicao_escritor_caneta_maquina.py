class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print(f"✍️ Escrevendo com a caneta {self.marca}...")


class MaquinaDeEscrever:
    def __init__(self, modelo):
        self.modelo = modelo

    def escrever(self):
        print(f"⌨️ Escrevendo com a máquina de escrever {self.modelo}...")


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        # Agora as ferramentas são criadas DENTRO do escritor (composição)
        self.caneta = Caneta("Bic")
        self.maquina = MaquinaDeEscrever("Olivetti")

    def escrever_com_caneta(self):
        print(f"{self.nome} começa a escrever com a caneta:")
        self.caneta.escrever()

    def escrever_com_maquina(self):
        print(f"{self.nome} começa a escrever com a máquina:")
        self.maquina.escrever()

<<<<<<< HEAD

try:
    # --- Demonstração ---
    escritor = Escritor("André")
    escritor.escrever_com_caneta()
    escritor.escrever_com_maquina()

    # Agora, ao apagar o escritor, suas ferramentas também deixam de existir
    del escritor

    # Tentativa de usar as ferramentas (não é possível)
=======
    def escrever(self,ferramenta):
        print(f"{self.nome} começa a escrever com a {ferramenta.nome}:")
        ferramenta.escrever()


# --- Demonstração ---
escritor = Escritor("André")
escritor.escrever_com_caneta()
escritor.escrever_com_maquina()


# Agora, ao apagar o escritor, suas ferramentas também deixam de existir
del escritor

# Tentativa de usar as ferramentas (não é possível)
try:
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
    escritor.caneta.escrever()
except NameError:
    print("\n❌ O escritor e suas ferramentas foram destruídos.")
