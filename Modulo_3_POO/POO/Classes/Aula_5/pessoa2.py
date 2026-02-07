#Exemplo: Exceção propagada para fora da classe
class IdadeInvalidaError(Exception):
    def __init__(self, idade):
        super().__init__(f"Idade inválida: {idade}. Deve ser maior que 0.")

class Pessoa:
    def __init__(self, nome, idade):
        if idade < 0:
            raise IdadeInvalidaError(idade)
        self.nome = nome
        self.idade = idade

try:
    p = Pessoa("Ana", -5)
except IdadeInvalidaError as e:
    print("Erro ao criar pessoa:", e)
