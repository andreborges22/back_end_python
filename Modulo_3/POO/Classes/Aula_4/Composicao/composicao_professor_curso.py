class Professor:
    def __init__(self, nome):
        self.nome = nome

class Curso:
    def __init__(self, nome, nome_professor):
        self.nome = nome
        self.professor = Professor(nome_professor)  # Composição

    def get_professor(self):
        return self.professor

# Criação dos objetos
try:
    curso = Curso("POO em Python", "João Silva")
    print(f"Professor do curso de {curso.nome}: {curso.professor.nome}")
    del curso
    print(f"Professor do curso de {curso.nome}: {curso.professor.nome}")        
except Exception as e:
    print(f"Erro: {e}")