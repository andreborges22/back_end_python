class Pessoa:
    
    def __init__(self, nome, idade):  
                  
        if (isinstance(nome, str) and (len(nome)>0)):  
            self.nome = nome
        else:
            raise ValueError('Nome não pode ser vazio!')
        
        #if(type(idade)==int):        
        if (isinstance(idade, int) and (idade>0)):                    
            self.idade = idade        
        else:
            raise ValueError("Idade tem que ser um número inteiro positivo!")        

    def apresentar(self):      
      print(f"Sou {self.nome}, tenho {self.idade} anos.")
      
   
try:
  p1 = Pessoa('Ana',-20)
  p1.apresentar()
except ValueError as v:
  print(f"Erro: {v}")
except Exception as e:
  print(f"Erro: {e}")
else:  
  print("Tudo ok.")
finally:
  print("Programa finalizado.")