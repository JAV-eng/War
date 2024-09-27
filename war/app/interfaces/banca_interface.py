from abc import ABC, abstractmethod
from jogador_interface import JogadorInterface
class BancaInterface(ABC):
    
    async def criar_jogo(self):
        pass
    
    async def adicionar_jogador(self, jogador: JogadorInterface):
        pass
    
    async def jogador_escolhe_cor(self, nome, cor, jogador: JogadorInterface):
        pass
    
    async def atribuir_objetivos(self, jogador: JogadorInterface):
        pass
    
    async def get_objetivo_jogador(self, nome, jogador: JogadorInterface):
        pass
    
    async def distribuir_cartas_territorio(self, jogador: JogadorInterface, territorios: CartasTerritorios):
        pass
    
    async def definir_ordem_jogadores(self):
        pass
    
    async def atribuir_carta_territorio(self, jogador_id, carta_id):
        pass
