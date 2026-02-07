class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, saque):
        super().__init__(f"Saldo insuficiente! Saldo: {saldo}, Saque: {saque}")


class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor


conta = Conta(101, 100)

try:
    conta.sacar(250)
except SaldoInsuficienteError as e:
    print("Operação cancelada:", e)
