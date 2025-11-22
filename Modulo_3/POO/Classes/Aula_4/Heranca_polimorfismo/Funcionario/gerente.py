from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        # Chama o construtor da classe pai (Funcionario) para inicializar
        # os atributos herdados (nome, salario base).
        super().__init__(nome, salario) 
        self.__bonus = bonus

    def calcularPagamento(self):
        self.salario = self.__bonus
        return self.salario
    
    def exibirInformacoes(self):
        print(f"Gerente: {self.nome} - Salário: R${self.calcularPagamento()}")