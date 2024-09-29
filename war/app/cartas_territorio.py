import json
from .database_manager import Database

class CartasTerritorios:
    def __init__(self, path, repository):
        self.path = path
        self.repository = repository
        with open(self.path, 'r') as file:
            self.data = json.load(file)
        self.cartas_territorios = self.data['cartas_territorio']

    async def inserir_cartas_territorio(self):
        db = await Database.get_instance()
        await self.repository.inserir_cartas(db, self.cartas_territorios)

    async def selecionar_cartas_territorio(self, quantidade):
        db = await Database.get_instance()
        return await self.repository.selecionar_cartas(db, quantidade)

    async def get_cartas_territorio_jogador(self, jogador_id):
        db = await Database.get_instance()
        sql = """
            SELECT *
            FROM cartas_territorio 
            WHERE jogador_id = ?
        """
        async with db.database.execute(sql, (jogador_id,)) as cursor:
            return await cursor.fetchall()