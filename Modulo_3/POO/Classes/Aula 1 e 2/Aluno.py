class Aluno:
    def __init__(self,nota1,nota2):
        self.nota1 = nota1
        self.nota2 = nota2
    
    def media(self):
        return (self.nota1+self.nota2)/2
    
    def situacao(self):
        if(self.media()>=6):
            return "Aprovado"
        else:
            return "Reprovado"
    
aluno = Aluno(4,6)
print(aluno.media())
print(aluno.situacao())