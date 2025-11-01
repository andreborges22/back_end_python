class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self._salario = salario

    def calcularPagamento(self):
        return self._salario
    
    def exibirInformacoes(self):
        print(f"Funcionário: {self.nome} - Salário: R${self.calcularPagamento()}")