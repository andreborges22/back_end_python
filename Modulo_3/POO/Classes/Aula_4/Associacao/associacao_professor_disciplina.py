class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []  # associação: lista de disciplinas que o professor leciona
<<<<<<< HEAD
        print(f"(Professor(a)) '{self.nome}' criado.")
=======
        print(f"Professor '{self.nome}' criado.")
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36

    def adicionar_disciplina(self, disciplina):
        """Associa uma disciplina ao professor (dos dois lados)."""
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.adicionar_professor(self)

    def remover_disciplina(self, disciplina):
        """Remove a disciplina da lista do professor (dos dois lados)."""
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            disciplina.remover_professor(self)

    def listar_disciplinas(self):
        """Exibe as disciplinas que o professor leciona."""
<<<<<<< HEAD
        if self.disciplinas:
            nomes = [d.nome for d in self.disciplinas]
            print(f"Professor(a) {self.nome} leciona: {', '.join(nomes)}")
        else:
            print(f"Professor(a) {self.nome} não leciona nenhuma disciplina.")

    def __del__(self):
        print(f"Professor(a) '{self.nome}' removido da memória.")

    def __str__(self):
        return f"Professor(a): {self.nome}"
=======
        for disciplina in self.disciplinas:
            print(f"Professor: {self.nome}, {disciplina}")
        '''if self.disciplinas:
            nomes = [d.nome for d in self.disciplinas]
            print(f"Professor {self.nome} leciona: {', '.join(nomes)}")
        else:
            print(f"Professor {self.nome} não leciona nenhuma disciplina.")'''

    def __del__(self):
        print(f"Professor '{self.nome}' removido da memória.")

    def __str__(self):
        return f"Professor: {self.nome}"
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []  # associação: lista de professores que ministram esta disciplina
        print(f"Disciplina '{self.nome}' criada.")

    def adicionar_professor(self, professor):
        """Associa um professor à disciplina (dos dois lados)."""
        if professor not in self.professores:
            self.professores.append(professor)

    def remover_professor(self, professor):
        """Remove um professor da disciplina (dos dois lados)."""
        if professor in self.professores:
            self.professores.remove(professor)

    def listar_professores(self):
        """Exibe os professores que lecionam esta disciplina."""
        if self.professores:
<<<<<<< HEAD
            nomes = [p.nome for p in self.professores]
            print(
                f"Disciplina {self.nome} é ministrada por: {', '.join(nomes)}")
=======
            for professor in self.professores:
                print(f"Disciplina: {self.nome}, {professor}")
            '''nomes = [p.nome for p in self.professores]
            print(f"Disciplina {self.nome} é ministrada por: {', '.join(nomes)}")'''
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
        else:
            print(f"Disciplina {self.nome} não possui professores no momento.")

    def __del__(self):
        print(f"Disciplina '{self.nome}' removida da memória.")

    def __str__(self):
        return f"Disciplina: {self.nome}"

<<<<<<< HEAD

=======
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36
try:
    # --- Exemplo de uso prático ---

    # Criando professores
    p1 = Professor("Ana")
    p2 = Professor("Carlos")

    # Criando disciplinas
    d1 = Disciplina("Matemática")
    d2 = Disciplina("Física")

    # Estabelecendo associações
    p1.adicionar_disciplina(d1)
    p1.adicionar_disciplina(d2)
    p2.adicionar_disciplina(d1)

    # Exibindo associações
    print("\n--- Relações ---")
    p1.listar_disciplinas()
    p2.listar_disciplinas()
    d1.listar_professores()
    d2.listar_professores()

    # Demonstrando independência
    print("\n--- Independência ---")
    print("Removendo o professor Ana (p1)...")
    del p1  # remove o professor
    print("A disciplina Matemática ainda existe:")
    d1.listar_professores()
<<<<<<< HEAD
=======
    d1.listar_professores()
>>>>>>> 63172a34a13137afd6bbd75fb6a7e71649664f36

    print("\nRemovendo a disciplina Física (d2)...")
    del d2  # remove a disciplina
    print("O professor Carlos ainda existe:")
    p2.listar_disciplinas()
except Exception as e:
    print(f"Erro: {e}")
