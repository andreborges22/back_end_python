class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []  # associação: lista de cursos em que o aluno está inscrito
        print(f"Objeto '{self.nome}' sendo construído.")

    def __del__(self):             
        print(f"Objeto '{self.nome}' sendo destruído.")

    def inscrever(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.adicionar_aluno(self)  # estabelece a relação dos dois lados

    def __str__(self):
        return f"Aluno: {self.nome}"

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # associação: lista de alunos matriculados
        print(f"Objeto '{self.nome}' sendo construído.")

    def __del__(self):
        print(f"Objeto '{self.nome}' sendo destruído.")

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def deletar_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def __str__(self):
        return f"Curso: {self.nome}"
    
    # --- Exemplo de uso ---

# Criando alunos
a1 = Aluno("Ana")
a2 = Aluno("Carlos")

# Criando cursos
c1 = Curso("Python Básico")
c2 = Curso("Banco de Dados")

# Associação (Aluno  Curso)
a1.inscrever(c1)
a1.inscrever(c2)
a2.inscrever(c1)
a2.inscrever(c2)


# Exibindo as associações
print(f"\nCursos de {a1.nome}: {[curso.nome for curso in a1.cursos]}")
'''for curso in a1.cursos:
    print(curso.nome)'''
print(f"Cursos de {a2.nome}: {[curso.nome for curso in a2.cursos]}")

print(f"\nAlunos do curso {c1.nome}: {[aluno.nome for aluno in c1.alunos]}")
print(f"Alunos do curso {c2.nome}: {[aluno.nome for aluno in c2.alunos]}")

# Demonstrando independência
print("\n--- Exemplo de Independência ---")
print("Se o aluno Ana (a1) desistir, o curso Python Básico (c1) continua existindo.")
del a1  # removendo o objeto 'Ana'
print("Curso ainda existe:", c1.nome)
print("Alunos restantes:", [aluno.nome for aluno in c1.alunos])

# Demonstrando independência
print("\n--- Exemplo de Independência ---")
print("Se o curso Banco de Dados (c2) terminar, O aluno Carlos (a2) ainda existe.")
del c2  # removendo o objeto 'Banco de Dados'
print("Aluno ainda existe:", a2.nome)
print("Cursos restantes:", [curso.nome for curso in a2.cursos])