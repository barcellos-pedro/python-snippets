class Livro:
    def __init__(self, titulo, autor, qtd_pg):
        self.titulo = titulo
        self.autor = autor
        self.qtd_pg = qtd_pg

    def __repr__(self):
        return f"Livro('{self.titulo}', '{self.autor}', {self.qtd_pg})"

    def __str__(self):
        return f"titulo={self.titulo}, autor={self.autor}, qtd_pg={self.qtd_pg}"


livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 264)
livro2 = Livro("Poeira em alto mar", "Alan Bida", 100)

print(livro1)
print(repr(livro1))
print(str(livro1))

print()

print(livro2)
print(repr(livro2))
print(str(livro2))
