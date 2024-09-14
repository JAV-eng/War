from abc import ABC,abstractmethod
from exercito_interface import ExercitoInterface

class JogadorInterface(ABC):
    
    @abstractmethod
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def escolher_cor_exercito(self,cor):
        pass
    
    @abstractmethod
    def get_cor_exercito():
        pass
    
    @abstractmethod
    def set_objetivo(self):
        pass
    
    @abstractmethod
    def get_objetivo(self):
        pass
    
    def adicionar_exercito(self,exercito,quantidade,territorio):
        pass
    
    