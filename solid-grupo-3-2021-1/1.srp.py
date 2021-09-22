"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

class Save:
    def __init__(self):
        self.__save = []
    
    def save(self, animal: Animal):
        self.__save.append(animal)
