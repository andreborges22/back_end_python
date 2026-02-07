class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        self.__salario+=valor
        return self.__salario

    def calcularPagamento(self):
        return self.salario
    
    def exibirInformacoes(self):
        print(f"Funcionário: {self.nome} - Salário: R${self.calcularPagamento()}")