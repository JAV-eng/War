from abc import ABC,abstractmethod


class JogadorInterface(ABC):
    
    @abstractmethod
    def __init__(self,nome):
        pass
    
    @abstractmethod
    async def adicionar_jogador(self):
        pass
    
    @abstractmethod
    async def escolher_cor_exercito(self,nome,cor):
        pass
    
    @abstractmethod
    async def get_cor_exercito():
        pass
    
    @abstractmethod
    async def set_objetivo(self,jogador_id,objetivo_id):
        pass
    
    @abstractmethod
    async def get_objetivo(self,nome):
        pass
    
    async def adicionar_exercito(self,exercito,quantidade,territorio):
        pass
    
    