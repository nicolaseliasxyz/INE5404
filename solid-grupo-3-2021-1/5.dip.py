"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""

class Player:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self):
        pass

    def report(self, char):
        print(f'Name:{char.name()}')
        print(f'HP:{char.hp()}')
