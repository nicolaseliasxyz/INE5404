#Exercicio 2 da Lista 1 BIBLIOTECA
"""Neste exercicio criei uma class livros para instancias todos os livros com seus atributos titulo autor etc, e um mecanisco de pesquisa
esta pesquisando dentro de um array eu percorro todo meu vetor, possivel pesquisar por titulo, autor, data de publicacao e editora, diz q quantidade de livros ue possui,
se for por titulo da pra saber especificamente qual livro temos.

"""

class Livros:
    def __init__(self, titulo: str, autor: str, ano: int, editora: str, edicao: int, volume: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume

class Biblioteca:
    def __init__(self, livros = []):
        self.livros = livros
        
    def pesquisa_titulo(self, titulo):
        tem_livro = 0
        for i in range(len(self.livros)):
            if self.livros[i].titulo == titulo:
                tem_livro = 1
                break
        if tem_livro == 1:
            return f'Temos o livro {titulo} em nossa biblioteca'
        else:
            return 'Nao temos este livro'
    
    def pesquisa_autor(self, autor):
        tem_livro = 0
        for i in range(len(self.livros)):
            if self.livros[i].autor == autor:
                tem_livro += 1
        if tem_livro >= 1:
            return f'Temos {tem_livro} livros deste autor'
        else:
            return 'Nao temos livros deste autor'
    
    def pesquisa_ano(self, ano):
        tem_livro = 0
        for i in range(len(self.livros)):
            if self.livros[i].ano == ano:
                tem_livro += 1
        if tem_livro >= 1:
            return f'Temos {tem_livro} publicados neste ano em nossa biblioteca'
        else:
            return 'Nao temos livros desta data'
    
    def pesquisa_editora(self, editora):
        tem_livro = 0
        for i in range(len(self.livros)):
            if self.livros[i].editora == editora:
                tem_livro += 1
        if tem_livro >= 1:
            return f'Temos {tem_livro} desta editora em nossa biblioteca'
        else:
            return 'Nao temos livros desta editora'
    
    
                
                
    
def main():
    #-----------------Criando os Objetos livros-----------------------
    livro1 = Livros(titulo= 'a guerra dos tronos', autor= 'george r. r. martim', ano = 1996, editora= 'bantam spectra',edicao= 1, volume= 1)
    livro2 = Livros(titulo= 'a furia dos reis', autor= 'george r. r. martim', ano = 1998, editora= 'bantam spectra',edicao= 1, volume= 2)
    livro3 = Livros(titulo= 'a tormenta de espadas', autor= 'george r. r. martim', ano = 2000, editora= 'bantam spectra',edicao= 1, volume= 3)
    livro4 = Livros(titulo= 'o festim dos corvos', autor= 'george r. r. martim', ano = 2005, editora= 'bantam spectra',edicao= 1, volume= 4)
    
    prateleira1 = Biblioteca([livro1, livro2, livro3, livro4])
    
    print(prateleira1.pesquisa_titulo('a guerra dos tronos'))
    
    print(prateleira1.pesquisa_autor('george r. r. martim'))
    
    print(prateleira1.pesquisa_ano(1996))
    
    print(prateleira1.pesquisa_editora('bantam spectra'))
    


main()


