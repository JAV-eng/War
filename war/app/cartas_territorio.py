import json
from database_manager import Database

class CartasTerritorios():
    def __init__(self,path):
        self.path = path
        with open(self.path, 'r') as file:
            self.data = json.load(file)
        self.cartas_territorios = self.data['cartas_territorio']
        
    async def inserir_cartas_territorio(self):
        db = await Database.get_instance()
        cartas_territorio = self.cartas_territorios
        for carta_territorio in cartas_territorio:
            territorio = carta_territorio['territorio']
            simbolo = carta_territorio['simbolo']
            query = """INSERT OR IGNORE INTO cartas_territorio (territorio, simbolo, selecionado) VALUES (?, ?, 0)"""
            await db.execute_query(query, (territorio, simbolo))
            
    async def get_cartas_territorio(self):
        db = await Database.get_instance()
        sql = f"""SELECT id FROM cartas_territorio ORDER BY RANDOM()"""
        async with db.execute(sql) as cursor:
            self.cartas_territorios_id = await cursor.fetchall()
        return self.cartas_territorios_id
        