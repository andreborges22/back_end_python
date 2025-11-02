class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitirSom(self):
            return (f"{self.nome} está emitindo um som genérico")