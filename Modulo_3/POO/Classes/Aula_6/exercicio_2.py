
class Produto:
    def __init__(self, nome, preco=0):
        self.nome = nome
        self.preco = preco

    def alterar_preco(self, valor):
        try:
            if (valor < 0):
                raise ValueError(f"Valor não pode ser negativo! {valor}")
            self.valor = valor
        except ValueError as ve:
            print(f"Erro:{ve}")

    def detalhes(self):
        print(f"Nome : {self.nome}")
        print(f"@Idade {self.preco}")


produto = Produto("mouse")
produto.alterar_preco(-10)
produto.detalhes()
