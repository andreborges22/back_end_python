class Pessoa:
 def __init__(self, nome, idade):
     self.__nome = nome
     self.__idade = idade
 
 # Getter para nome
 def get_nome(self):
     return self.__nome
 
 # Setter para nome
 def set_nome(self, novo_nome):
    if isinstance(novo_nome, str) and len(novo_nome) > 0:
        self.__nome = novo_nome
    else:
        raise ValueError("Nome inválido")
 
 # Getter para idade
 def get_idade(self):
     return self.__idade
 
 # Setter para idade
 def set_idade(self, nova_idade):
     if 0 <= nova_idade <= 150:
         self.__idade = nova_idade
     else:
         raise ValueError("Idade deve estar entre 0 e 150")

try:
    pessoa = Pessoa("João", 25)
    print(pessoa.get_nome()) # João
    pessoa.set_nome("José") # Válido
    print(pessoa.get_nome()) # José
    #pessoa.set_nome("") # Levanta exceção!
    pessoa.set_idade(26) # Válido
    pessoa.set_idade(-5) # Levanta exceção!
except Exception as e:
    print(f"Erro: {e}")