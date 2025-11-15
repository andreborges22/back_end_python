class Livro:
    livros = []
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao    
        self.biblioteca = {}     
    
    def detalhes(self):
        print(f"Título: {self.titulo}\n Autor: {self.autor}\n Ano de Publicação: {self.ano_publicacao}\n")

    def set_livros(self, titulo):       
        if(titulo not in self.livros):
            self.livros.append(titulo)   

    def inserir_livro(self,id,livro):    
        if 'livros' not in self.biblioteca:
            self.biblioteca['livros']: {id: livro}
        else:
            self.biblioteca['livros'].update({id: livro})


    def get_livros(self):
        for livro in self.biblioteca:
            print(livro.titulo)

livros = []
livro = Livro("O homem mais rico da babilônia","André",2025)
livro.inserir_livro(1,livro)
#livros.append(livro)
livro2 = Livro("Pai rico, pai pobre","André",2025)
livro2.inserir_livro(2,livro)
#livros.append(livro2)
#for livro in livros:    
    #print(f"- {livro.titulo}")
livro.get_livros()