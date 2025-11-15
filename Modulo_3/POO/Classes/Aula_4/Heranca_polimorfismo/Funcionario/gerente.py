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
<<<<<<< HEAD
        print(f"Gerente: {self.nome} - Salário: R${self.calcularPagamento()}")
=======
        print(f"Gerente: {self.nome} - Salário: R${self.calcularPagamento()}")
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
