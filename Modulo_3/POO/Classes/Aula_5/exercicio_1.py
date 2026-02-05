class NotaInvalidaError(Exception):
    def __init__(self, valor):
        super().__init__(f"Nota inválida: {valor}. A nota deve estar entre 0 e 10.")


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.nota = None

    def definir_nota(self, valor):
        if valor < 0 or valor > 10:
            raise NotaInvalidaError(valor)
        self.nota = valor


# Teste
try:
    aluno = Aluno("Lucas")
    aluno.definir_nota(15)
except NotaInvalidaError as e:
    print("Erro ao definir nota:", e)
