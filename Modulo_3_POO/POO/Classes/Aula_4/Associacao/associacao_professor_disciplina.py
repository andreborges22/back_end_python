class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []  # associação: lista de disciplinas que o professor leciona
        print(f"(Professor(a)) '{self.nome}' criado.")

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
        if self.disciplinas:
            nomes = [d.nome for d in self.disciplinas]
            print(f"Professor(a) {self.nome} leciona: {', '.join(nomes)}")
        else:
            print(f"Professor(a) {self.nome} não leciona nenhuma disciplina.")

    def __del__(self):
        print(f"Professor(a) '{self.nome}' removido da memória.")

    def __str__(self):
        return f"Professor(a): {self.nome}"


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
            nomes = [p.nome for p in self.professores]
            print(
                f"Disciplina {self.nome} é ministrada por: {', '.join(nomes)}")
        else:
            print(f"Disciplina {self.nome} não possui professores no momento.")

    def __del__(self):
        print(f"Disciplina '{self.nome}' removida da memória.")

    def __str__(self):
        return f"Disciplina: {self.nome}"

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

    print("\nRemovendo a disciplina Física (d2)...")
    del d2  # remove a disciplina
    print("O professor Carlos ainda existe:")
    p2.listar_disciplinas()
except Exception as e:
    print(f"Erro: {e}")
