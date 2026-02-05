class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []
    #adiciona uma disciplina ao professor
    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            #adiciona o professor à lista de professores da disciplina passada como parâmetro
            disciplina.adicionar_professor(self)

    #remover professor da disciplina
    def remover_disciplina(self,disciplina):
        #verificar se disciplina esta na lista
        if disciplina in self.disciplinas:
        #se estiver, remove
            self.disciplinas.remove(disciplina)
            #chamar o método remover professor da disciplina passada como parâmetro
            disciplina.remover_professor(self)

    def listar_disciplinas(self):
        lista = ''
        for disciplina in self.disciplinas:
            lista += f"{disciplina.nome},"
        lista = lista.strip(",")
        if (lista):
            return (f"lista de disciplinas do professor {self.nome}: {lista}")
        return f"O professor {self.nome} não leciona nenhuma disciplina"

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    #adiciona um professor à disciplina
    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
    
    #remove um professor da disciplina
    def remover_professor(self,professor):
        #exatamente o contrário do método adicionar professor
        if professor in self.professores:
            # se o professor estiver na lista de professores, remova
            self.professores.remove(professor)



    def listar_professores(self):
        lista = ''
        for professor in self.professores:
            lista += f"{professor.nome},"
        lista = lista.strip(",")
        if (lista):
            return (f"lista de professores da disciplina {self.nome}: {lista}")
        return f"A disciplina {self.nome} não possui professor"


disciplina1 = Disciplina("Python")
disciplina2 = Disciplina("BD")
disciplina3 = Disciplina("Java")
professor1 = Professor("André")
professor2 = Professor("João")
professor1.adicionar_disciplina(disciplina1)
professor2.adicionar_disciplina(disciplina1)
# del disciplina
# print(professor.nome)
# del professor
# print(disciplina.nome)

print(disciplina1.listar_professores())
print(professor1.listar_disciplinas())
print(disciplina2.listar_professores())
print(professor2.listar_disciplinas())
