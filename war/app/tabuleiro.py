import json
from .database_manager import Database
class Tabuleiro:
    def __init__(self, path):
        self.path = path
        with open(self.path, 'r') as file:
            self.data = json.load(file)
        self.cartas_territorios = self.data['cartas_territorio']

    async def carregar_territorios(self):
        db = await Database.get_instance()
        await db.criar_tabela_tabuleiro()

        for carta in self.cartas_territorios:
            territorio = carta['territorio']
            vizinhos = carta['vizinhos']
            continente = carta['continente']
            await self.inserir_territorio(territorio, vizinhos, continente)

    async def inserir_territorio(self, territorio, vizinhos, continente):
        db = await Database.get_instance()
        sql = """
            INSERT INTO tabuleiro (territorio, territorios_vizinhos, continente, exercitos_id)
            VALUES (?, ?, ?, ?)
        """
        await db.execute_query(sql, (territorio, json.dumps(vizinhos), continente, None))
    
    async def adicionar_exercito_territorio(self, territorio, id_exercito):
        db = await Database.get_instance()
        query = """
            UPDATE tabuleiro
            SET exercitos_id = ?
            WHERE territorio = ?
        """
        await db.execute_query(query, (id_exercito, territorio))
        
    async def remover_exercito_territorio(self, territorio):
        db = await Database.get_instance()
        query = """
            UPDATE tabuleiro
            SET exercitos_id = ''
            WHERE territorio = ?
        """
        await db.execute_query(query, (territorio))

    async def get_territorios(self):
        db = await Database.get_instance()
        sql = "SELECT * FROM tabuleiro"
        async with db.database.cursor() as cursor:
            await cursor.execute(sql)
            territorios = await cursor.fetchall()
        return territorios
