class Pessoa:
    
    def __init__(self, nome, idade):  
        self.nome = nome
        self.idade = idade                
    
    def apresentar(self):      
      print(f"Sou {self.nome}, tenho {self.idade} anos.")
      
nome = input("Digite um nome ")
while (not nome.strip()):
   print("Nome não pode ficar em branco ")
   nome = input("Digite um nome ")
p1 = Pessoa(nome,30)
p1.apresentar()