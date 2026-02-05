class BaseDeDados:
    def __init__(self):
        self.__dados = {'clientes':{}}

    @property
    def dados(self):
        return self.__dados
    
    def inserir_clientes(self,id,nome):
        self.__dados['clientes'].update({id:nome})
        
    def listar_clientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(id,nome)

    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]

try:
    bd = BaseDeDados()
    bd.inserir_clientes(1,'João')
    bd.inserir_clientes(2,'Maria')
    bd.inserir_clientes(3,'José')
    bd.__dados = 'outra coisa'
    bd.inserir_clientes(4,'José')
    print(bd.dados)
except Exception as e:
    print(f"Erro: {e}")
else:
    pass