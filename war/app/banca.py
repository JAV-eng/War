import asyncio
from database_gerenciador import Database
from interfaces.jogador_interface import JogadorInterface
from cores import CoresManager
from cartas_objetivos import Objetivos

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
    
    async def get_numero_jogadores(self):
        db = await Database.get_instance()
        async with db.execute("SELECT COUNT(*) FROM jogador") as cursor:
            row_count = await cursor.fetchone()
        return row_count[0] if row_count else 0


