import asyncio
from database_manager import Database
from interfaces.jogador_interface import JogadorInterface
from cores import CoresManager
from cartas_objetivos import Objetivos
from jogador_manager import JogadorManager

class Banca():
    
    def __init__(self):
        self.cores = CoresManager('war/app/rsc/cores.json')
        self.objetivos = Objetivos('war/app/rsc/cartas_objetivos.json')
        
    async def criar_jogo(self):
        try:
            db = await Database.get_instance()
            await db.criar_tabela_cores()
            await db.criar_tabela_jogador()
            await db.criar_tabela_cartas_territorio()
            await db.criar_tabela_exercito()
            await db.criar_tabela_objetivos()
            await self.cores.inserir_cores_do_json()
            await self.objetivos.inserir_objetivos()
            return "Jogo iniciado com sucecesso"
        except Exception as e:
            return f"Não foi possível criar o jogo devido ao erro: {str(e)}"    
        
    async def adicionar_jogador(self, jogador :JogadorInterface):
        return await jogador.adicionar_jogador()
    
    async def jogador_escolhe_cor(self,nome,cor,jogador:JogadorInterface):
        return await jogador.escolher_cor_exercito(nome,cor)
    
    async def atribuir_objetivos(self,jogador:JogadorInterface):
        self.jogador_manager = JogadorManager(jogador,self.objetivos)
        await self.jogador_manager.atribuir_objetivos()
    
    async def get_objetivo_jogador(self,nome,jogador:JogadorInterface):
       return await jogador.get_objetivo(self,nome)
        
    


