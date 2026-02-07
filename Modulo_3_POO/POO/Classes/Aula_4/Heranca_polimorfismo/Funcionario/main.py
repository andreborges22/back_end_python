from funcionario import Funcionario
from gerente import Gerente
from vendedor import Vendedor

try:
    funcionario = Funcionario("João",1000)
    gerente = Gerente("André",5000,1000)
    vendedor = Vendedor("José",3000,500)

    funcionario.exibirInformacoes()
    gerente.exibirInformacoes()
    vendedor.exibirInformacoes()
except AttributeError as a:
    print(f"AttributeError: {a}")
except Exception as e:
    print(f"Exception: {e}")