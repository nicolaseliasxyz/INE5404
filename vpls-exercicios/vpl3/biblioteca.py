from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if type(livro) is Livro:
            if livro in self.__livros:
                print()
            else:
                self.__livros.append(livro)
            

    def excluirLivro(self, livro: Livro):
        if livro in self.__livros:
            for i in range(len(self.__livros)):
                if self.__livros[i] == livro:
                    self.__livros.pop(i)
                    break
        

    @property
    def livros(self):
        return self.__livros
