class Professor:
    def __init__(self, nome):
        self.nome = nome
        print(f"Objeto '{self.nome}' sendo criado.")

    def __del__(self):
        print(f"Objeto '{self.nome}' sendo destruído.")

class Curso:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor  # associação

# Criação dos objetos
prof = Professor("João Silva")
curso = Curso("POO em Python", prof)

print(f"Professor do curso de {curso.nome}: {curso.professor.nome}")
# Saída: Professor do curso de POO em Python: João Silva

# destruição de objetos
print("Deletando o curso")
del curso
print(prof.nome)

'''print("Deletando o professor")
del prof
print(curso.nome)'''
