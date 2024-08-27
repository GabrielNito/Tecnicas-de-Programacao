class Autor:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def mostrarDetalhes(self):
        print(f"Nome = {self.nome}")
        print(f"CPF = {self.cpf}")
        print(f"Email = {self.email}")


class Livro:
    def __init__(self, nome, descricao, valor, isbn, autor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.isbn = isbn
        self.autor = autor

    def mostrarDetalhes(self):
        print("===== livro =====")
        print(f"Nome = {self.nome}")
        print(f"Descrição = {self.descricao}")
        print(f"Valor = {self.valor}")
        print(f"ISBN = {self.isbn}")
        print("===== autor =====")
        self.autor.mostrarDetalhes()


autor01 = Autor("Autor Desconhecido", "489.123.781-27",
                "autor@desconhecido.com")
livro01 = Livro("A", "Um livro", "30,00", "01984", autor01)

livro01.mostrarDetalhes()
