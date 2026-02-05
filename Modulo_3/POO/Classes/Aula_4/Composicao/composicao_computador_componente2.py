'''Crie um programa em Python com as classes Computador e Componente.

Um Computador é formado por vários Componentes (como processador, memória e armazenamento).

Os Componentes são criados dentro do objeto Computador (não existem sem ele).

Quando o Computador é destruído, todos os seus componentes deixam de existir.

👉 Implemente métodos que:

Adicionem componentes ao computador.

Mostrem todos os componentes instalados.

Simulem a destruição do computador (mostrando que os componentes são apagados junto).'''


class Componente:
    def __init__(self, nome, modelo):
        self.nome = nome
        self.modelo = modelo


class Computador:
    def __init__(self, nome):
        self.nome = nome
        self.componentes = []

    # Os Componentes são criados dentro do objeto Computador (não existem sem ele).
    def adicionar_componente(self, nome, modelo):
        # adicionar o componente à lista de componentes do computador
        self.componentes.append(Componente(nome, modelo))

    def listar_componentes(self):
        for componente in self.componentes:
            print(componente.nome)

    def __del__(self):
        print(f"Computador {self.nome} sendo destruído")

computador = Computador("PC")
computador.adicionar_componente("Processador","Intel")
computador.adicionar_componente("Memória RAM","Kingston")
computador.listar_componentes()
del computador