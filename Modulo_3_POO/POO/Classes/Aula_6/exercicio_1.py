class NotaInvalidaError(Exception):
    def __init__(self, nota):
        super().__init__(f"Nota {nota} inválida!")


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.nota = 0

    def definir_nota(self, nota):
        if (nota < 0):
            raise NotaInvalidaError(nota)
        self.nota = nota


try:
    aluno = Aluno("André")
    aluno.definir_nota(-5)
    
except NotaInvalidaError as e:
    print(f"Erro:{e}")
