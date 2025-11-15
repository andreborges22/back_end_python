<<<<<<< HEAD
class Aluno:
=======
class Aluno:    
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []  # associação: lista de cursos em que o aluno está inscrito
        print(f"Objeto '{self.nome}' sendo construído.")

<<<<<<< HEAD
    def __del__(self):
=======
    def __del__(self):          
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
        print(f"Objeto '{self.nome}' sendo destruído.")

    def inscrever(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.adicionar_aluno(self)  # estabelece a relação dos dois lados
<<<<<<< HEAD

=======
    
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
    def desinscrever(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)
            curso.remover_aluno(self)  # estabelece a relação dos dois lados

    def cancelar(self):
        print("Cancelando...")
        for curso in self.cursos:
<<<<<<< HEAD
            curso.remover_aluno(self)
=======
            curso.remover_aluno(self)            
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36

    def __str__(self):
        return f"Aluno: {self.nome}"

<<<<<<< HEAD

=======
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
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

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
<<<<<<< HEAD

    def cancelar(self):
        for aluno in self.alunos[:]:
=======
    
    def cancelar(self):
        for aluno in self.alunos[:]:                         
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
            aluno.desinscrever(self)

    def __str__(self):
        return f"Curso: {self.nome}"

<<<<<<< HEAD

try:
=======
try:    
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
    # --- Exemplo de uso ---

    # Criando alunos
    a1 = Aluno("Ana")
    a2 = Aluno("Carlos")
    a3 = Aluno("João")

    # Criando cursos
    c1 = Curso("Python Básico")
    c2 = Curso("Banco de Dados")

    # Associação (Aluno  Curso)
    a1.inscrever(c1)
    a1.inscrever(c2)
    a2.inscrever(c1)
    a2.inscrever(c2)
    a3.inscrever(c1)
    a3.inscrever(c2)

    # Exibindo as associações
    print(f"\nCursos de {a1.nome}: {[curso.nome for curso in a1.cursos]}")
    '''for curso in a1.cursos:
        print(curso.nome)'''
    print(f"Cursos de {a2.nome}: {[curso.nome for curso in a2.cursos]}")
    print(f"Cursos de {a3.nome}: {[curso.nome for curso in a3.cursos]}")

<<<<<<< HEAD
    print(
        f"\nAlunos do curso {c1.nome}: {[aluno.nome for aluno in c1.alunos]}")
=======
    print(f"\nAlunos do curso {c1.nome}: {[aluno.nome for aluno in c1.alunos]}")
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
    print(f"Alunos do curso {c2.nome}: {[aluno.nome for aluno in c2.alunos]}")

    # Demonstrando independência
    print("\n--- Exemplo de Independência ---")
    print("Se o aluno Ana (a1) desistir, o curso Python Básico (c1) continua existindo.")
    print("rodando o comando del a1")
<<<<<<< HEAD
    # a1.cancelar()
    del a1  # removendo o objeto 'Ana'
    print("Curso ainda existe:", c1.nome)
    print("Curso ainda existe:", c2.nome)
    print(
        f"\nAlunos do curso {c1.nome}: {[aluno.nome for aluno in c1.alunos]}")
=======
    #a1.cancelar()
    del a1  # removendo o objeto 'Ana'
    print("Curso ainda existe:", c1.nome)
    print("Curso ainda existe:", c2.nome)
    print(f"\nAlunos do curso {c1.nome}: {[aluno.nome for aluno in c1.alunos]}")
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
    print(f"Alunos do curso {c2.nome}: {[aluno.nome for aluno in c2.alunos]}")

    # Demonstrando independência
    print("\n--- Exemplo de Independência ---")
    print("Se o curso Banco de Dados (c2) terminar, O aluno Carlos (a2) ainda existe.")
    print("rodando o comando del c2")
<<<<<<< HEAD
    c2.cancelar()
=======
    #c2.cancelar()
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
    del c2  # removendo o objeto 'Banco de Dados'
    print("Aluno ainda existe:", a2.nome)
    print("Aluno ainda existe:", a3.nome)
    print(f"Cursos de {a2.nome}: {[curso.nome for curso in a2.cursos]}")
    print(f"Cursos de {a3.nome}: {[curso.nome for curso in a3.cursos]}")

except Exception as e:
<<<<<<< HEAD
    print(f"Erro: {e}")
=======
    print(f"Erro: {e}")
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
