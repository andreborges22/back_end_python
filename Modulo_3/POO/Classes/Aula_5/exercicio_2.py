class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco if preco >= 0 else 0
        '''if preco >= 0:
            self.preco = preco
        else: 
            self.preco = 0'''

    def alterar_preco(self, valor):
        try:
            if valor < 0:
                raise ValueError("O preço não pode ser negativo.")
            self.preco = valor
        except ValueError as e:
            print(f"Erro ao alterar preço do produto '{self.nome}': {e}")

    def detalhes(self):
        print(f"Produto: {self.nome} - Preço: R$ {self.preco:.2f}")


# Teste
p = Produto("Mouse", 50)
p.alterar_preco(-20)  # tratado dentro da classe
p.detalhes()
