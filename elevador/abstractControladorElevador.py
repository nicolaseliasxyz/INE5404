from abc import ABC, abstractmethod
from elevador import Elevador


class AbstractControladorElevador(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    
