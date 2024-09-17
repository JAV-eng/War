
from banca import Banca
from jogador import Jogador
from cartas_territorio import CartasTerritorios

class Jogo:
    def __init__(self, app):
        self.app = app
        self.banca = Banca()
        self.setup_routes(self.banca)

    def setup_routes(self,banca):
        
        @self.app.get('/criar_jogo')
        async def criar():
            return await banca.criar_jogo()
        
        @self.app.get('/get_objetivos/{nome}')
        async def get_objetivos(nome:str):
            return await banca.get_objetivo_jogador(nome,Jogador)
            
        
        @self.app.get('/adicionar_jogador/{nome}')
        async def adicionar_jogador(nome: str):
            jogador = Jogador(nome)  # Criar uma instância de Jogador
            result = await self.banca.adicionar_jogador(jogador)
            return {"message": result}
        
        @self.app.get('/jogador_escolhe_cor/{nome}/{cor}')
        async def jogador_escolher_cor(nome:str ,cor:str):
            jogador = Jogador(nome)
            return await self.banca.jogador_escolhe_cor(nome,cor,jogador)
            
        
        @self.app.get('/sortear_objetivos')
        async def sortear_objetivos():
            return await self.banca.atribuir_objetivos(Jogador)
        
        @self.app.get('/definir_ordem_jogadores')
        async def definir_ordem_jogadores():
            return await self.banca.definir_ordem_jogadores()
        
        @self.app.get('/distribuir_territorios_iniciais')
        async def distribuir_territorios_iniciais(self):
            return await banca.distribuir_cartas_territorio(Jogador,CartasTerritorios)