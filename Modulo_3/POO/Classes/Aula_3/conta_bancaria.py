class ContaBancaria:
    def __init__(self, titular, conta, saldo_inicial):
        self.titular = titular          # público
        self._numero_conta = conta    # protegido
        self.__saldo = saldo_inicial    # privado

    def get_saldo(self):
        return self.__saldo

    def depositar(self,valor):
        if(valor>0):
            self.__saldo += valor
            print("Depósito efetuado com sucesso.")
        else:
            raise ValueError("Valor do depósito deve ser maior que 0. Depósito não efetuado")
        
    def sacar(self,valor):
        if(valor>0):
            if(valor<=self.get_saldo()):
                self.__saldo -= valor
                print("Saque efetuado com sucesso!")
            else:
                raise ValueError("Saldo insuficiente. Saque não efetuado.")    
        else:
            raise ValueError("Valor deve ser maior que 0. Saque não efetuado.")
    
    def get_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo}")

    def exibir_saldo(self):
        return self.__saldo
    
    def transferir(self,valor, outra_conta):
        self.sacar(valor)
        outra_conta.depositar(valor)        

try:
    conta1 = ContaBancaria("Maria Silva", 123, 1000)
    print(conta1.get_dados())
    conta2 = ContaBancaria("João Santos", 324, 500)
    print(conta2.get_dados())
    conta1.transferir(100,conta2)
    print(conta1.get_dados())
    print(conta2.get_dados())
except Exception as e:
    print(f"Erro: {e}")