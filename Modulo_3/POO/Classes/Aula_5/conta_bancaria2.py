# Exemplo Completo: Conta Bancária com Tratamento Interno
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, saque):
        super().__init__(
            f"Erro: saldo insuficiente! Saldo: R${saldo}, Saque: R${saque}")


class Conta:
    # Se não for especificado um valor, o saldo inicial é 0
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def sacar(self, valor):
        try:
            if valor > self.saldo:
                raise SaldoInsuficienteError(self.saldo, valor)
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso!")
        except SaldoInsuficienteError as e:
            print(f"[Conta {self.numero}] Falha ao sacar: {e}")

    def depositar(self, valor):
        try:
            if valor <= 0:
                raise ValueError("O depósito deve ser maior que zero.")
            self.saldo += valor
        except ValueError as e:
            print(f"Erro ao depositar: {e}")


conta = Conta('001', 1000)
conta.sacar(2000)
