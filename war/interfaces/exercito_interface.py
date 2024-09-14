from abc import ABC, abstractmethod

class ExercitoInterface(ABC):
    
    @abstractmethod
    def __init__(self,cor,tipo):
        super().__init__()
        
    @abstractmethod
    def get_jogador(self):
        pass
    
    @abstractmethod
    def get_cor(self):
        pass
    
    @abstractmethod
    def get_tipo(self):
        pass
    