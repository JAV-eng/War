from abc import ABC, abstractmethod

class BancaInterface(ABC):
    
    @abstractmethod
    def iniciar_jogo(numero_jogadores):
        pass
    
    
    