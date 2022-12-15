"""------------Exercicio 6; Lista 1; Baralho de cartas-------------
<<<<<<< HEAD
Neste exercicio busquei fazer um baralho padrao, que instanciando os objetos criando cartas, criando quantas cartas quiser podem fazer quaisquer
jogos que envolvam esse tipo de cartas, sei que pode existir formar mais automatizadas de criar um baralho, porem sou muito novo em programacao
tentei usar a logica de um baralho padrao, e fiz uma forma de insntaciar cartas, formar baralhos com metodos de embaralhar usando random,
adicionar e remover cartas do baralho, mostrar cartas de forma textual para exibi-las afim de mostrar que o codigo funciona.
"""
"""
None no inicio do array paracomecar no 1 para me organizar de forma melhor

=======

"""
"""
>>>>>>> 942fc78a2dfe524b39f64ea5ea95f4b1543b08ad
Paus = 1
Ouro = 2
Copa = 3
Espadas = 4

A = 1
Valete = 11
Dama = 12
Rei = 13
"""
from random import shuffle

naipe = [None,'Paus', 'Ouro', 'Copa', 'Espadas']
        
ranks = [None, 'A', '2', '3', '4', '5', '6', '7',
        '8', '9', '10', 'Valete', 'Dama', 'Rei']

class Baralho:
    def __init__(self, cards= []):
        self.cards = cards
        
    def imprime_baralho(self):
        
        for i in range(len(self.cards)):
            print(f'{ranks[self.cards[i].rank]} de {naipe[self.cards[i].naipe]}')
    
    def embaralhar(self):
        embaralhado = self.cards.copy()
        shuffle(embaralhado)
        return embaralhado
    
    def add(self, card):
        self.cards.append(card)
        return Baralho(self.cards)
    
    def remover(self, card):
        for i in range(len(self.cards)):
            if self.cards[i].rank == card.rank and self.cards[i].naipe == card.naipe:
                del(self.cards[i])
                break
        return Baralho(self.cards)
        
        
class Card:
    def __init__(self, naipe= int, rank= int):
        self.naipe = naipe
        self.rank = rank
        

    def imprime(self):
        return f'{ranks[self.rank]} de {naipe[self.naipe]}'
    
    
def main():
<<<<<<< HEAD
    #-------criado cada carta em forma de um objeto que possui um rank e um naipe listado no array
=======
    #-------criado cada carta em forma de um objeto que possui um rank e um naipe listado no array--=----
    #feito alguns exemplos sendo possivel mapear n combinacoes de baralhos de acordo com o rank e naipe desclito no array
>>>>>>> 942fc78a2dfe524b39f64ea5ea95f4b1543b08ad
    card1= Card(1, 1)
    card2= Card(1, 2)
    
    
    card3= Card(2, 11)
    card4= Card(2, 6)
    
    card5= Card(3, 2)
    card6= Card(3, 12)
    
    card7= Card(4, 1)
    card8= Card(4, 13)
    
    #------ colocando as cartas criadas no baralho----------
    
    baralho_8_cartas = Baralho([card1, card2, card3, card4, card5, card6, card7, card8])
    
    
    #------ print do baralho base-------
    print('Baralho Base ORDENADO')
    print(baralho_8_cartas.imprime_baralho())#baralho ordenado
    print()
    #------ print do baralho base embaralhado-------
    baralho_8_cartas_embaralhado = Baralho(baralho_8_cartas.embaralhar())
    print('Apos metodo embaralhar EMBARALHADO')
    print(baralho_8_cartas_embaralhado.imprime_baralho())
    print()
    #------ adcionando nova carta ao baralho-------
    
    card9 = Card(1, 13)
    
    novo_baralho = baralho_8_cartas.add(card9)
    
    print('Baralho apos adicionar mais uma carta')
    print(novo_baralho.imprime_baralho())
    print()
    
    #------ retirando carta ao baralho-------
    novo_baralho = novo_baralho.remover(card9)# objeto card9 ultilizado como demonstracao
    
    
    print('Baralho apos remover uma carta')
    print(novo_baralho.imprime_baralho())
    print()

main()


