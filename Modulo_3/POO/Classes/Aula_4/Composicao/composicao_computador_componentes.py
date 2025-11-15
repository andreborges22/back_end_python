class Componente:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        print(f"Componente '{self.nome}' ({self.tipo}) criado.")

    def __str__(self):
        return f"{self.tipo}: {self.nome}"

    def __del__(self):
        print(f"Componente '{self.nome}' destruído.")


class Computador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.componentes = []  # composição: os componentes pertencem ao computador
        print(f"Computador '{self.modelo}' criado.")

    def adicionar_componente(self, nome, tipo):
        """Cria um novo componente como parte do computador."""
        componente = Componente(nome, tipo)
        self.componentes.append(componente)

    def listar_componentes(self):
        """Exibe todos os componentes do computador."""
        print(f"\nComponentes do computador '{self.modelo}':")
        for comp in self.componentes:
            print(f" - {comp}")

    def __del__(self):
        print(f"\nComputador '{self.modelo}' sendo destruído...")
        print("Destruindo todos os componentes:")
        for comp in self.componentes:
            del comp  # os componentes deixam de existir junto
        print(f"Computador '{self.modelo}' e seus componentes foram removidos.")


# --- Exemplo de uso ---

pc1 = Computador("Dell Inspiron")

pc1.adicionar_componente("Intel Core i7", "Processador")
pc1.adicionar_componente("16GB DDR4", "Memória RAM")
pc1.adicionar_componente("SSD 512GB", "Armazenamento")

pc1.listar_componentes()

print("\n--- Agora, destruindo o computador ---")
del pc1  # destrói o computador e automaticamente seus componentes
