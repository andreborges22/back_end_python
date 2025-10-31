class Retangulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura        

    def perimetro(self):
        return (self.altura*2)+(self.largura*2)
    
    def set_largura(self,nova_largura):
        self.largura = nova_largura
    
    def set_altura(self, nova_altura):
        self.altura = nova_altura

try:
    retangulo = Retangulo(6,4)
    print(f"Área: {retangulo.area()}")
    print(f"Perímetro: {retangulo.perimetro()}")
    retangulo.set_altura(8)
    retangulo.set_largura(10)
    print(f"Área: {retangulo.area()}")
    print(f"Perímetro: {retangulo.perimetro()}")
except Exception as e:
    print(f"Erro {e}")