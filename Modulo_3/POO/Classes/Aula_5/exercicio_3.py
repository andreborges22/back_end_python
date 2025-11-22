class QuantidadeInvalidaError(Exception):
    pass


class Pedido:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = 1
        self.definir_quantidade(quantidade)

    def definir_quantidade(self, qtd):
        try:
            if not isinstance(qtd, int) or qtd <= 0:
                raise QuantidadeInvalidaError("Quantidade deve ser um inteiro maior que zero.")
            self.quantidade = qtd
        except QuantidadeInvalidaError as e:
            print(f"Erro ao definir quantidade do item '{self.item}': {e}")

    def resumo(self):
        print(f"Pedido: {self.quantidade}x {self.item}")


# Teste
p = Pedido("Camiseta", 0)
p.resumo()
