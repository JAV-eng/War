from database_manager import Database
from cartas_objetivos import Objetivos
from interfaces import JogadorInterface

class JogadorManager:
    def __init__(self,Jogador:JogadorInterface,Objetivos):
        self.Objetivos = Objetivos
        self.Jogador = Jogador

    async def get_numero_jogadores(self):
        db = await Database.get_instance()
        async with db.database.cursor() as cursor:
            await cursor.execute("SELECT COUNT(*) FROM jogador")
            result = await cursor.fetchone()
        return result[0]
        
    async def atribuir_objetivos(self):
        
        db = await Database.get_instance()
        Objetivo = self.Objetivos
        
        await self.limpar_atribuicoes()
        
        numero_jogadores = await self.get_numero_jogadores()
        objetivos_selecionados = await Objetivo.selecionar_objetivos(numero_jogadores)
        
        async with db.database.cursor() as cursor:

            await cursor.execute("SELECT id, nome FROM jogador")
            jogadores = await cursor.fetchall()

            for jogador, objetivo in zip(jogadores, objetivos_selecionados):
                jogador_id = jogador[0]
                objetivo_id = objetivo[0]
                await self.Jogador.set_objetivo(self,jogador_id,objetivo_id)
                await self.Objetivos.set_selecionado(objetivo_id)
                
        await db.database.commit()
        return "Objetivos atribuídos com sucesso!"
    
    async def limpar_atribuicoes(self):
        db = await Database.get_instance()

        async with db.database.cursor() as cursor:
            
            await cursor.execute("UPDATE jogador SET objetivo_id = NULL")
            await cursor.execute("UPDATE objetivos SET selecionado = 0")

        await db.database.commit()