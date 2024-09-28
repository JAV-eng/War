import json
from .database_manager import Database

class Objetivos():
    def __init__(self,path):
        self.path = path
        with open(self.path, 'r') as file:
            self.data = json.load(file)
        self.objetivos = self.data['objetivos']
    
    async def inserir_objetivos(self):
        db = await Database.get_instance()
        objetivos  = self.objetivos
        for objetivo in objetivos:
            nome = objetivo['nome']
            descricao = objetivo['descricao']
            query = """INSERT OR IGNORE INTO objetivos (nome, descricao, selecionado) VALUES (?, ?, 0)"""
            await db.execute_query(query, (nome, descricao))
            
    async def selecionar_objetivos(self,quantidade):
        db = await Database.get_instance()
        sql = f"""SELECT * FROM objetivos ORDER BY RANDOM() LIMIT {quantidade}"""
        async with db.execute(sql) as cursor:
            self.objetivo_selecionados = await cursor.fetchall()
        return self.objetivo_selecionados
    
    async def set_selecionado(self,objetivo_id):
        db = await Database.get_instance()
        async with db.database.cursor() as cursor:
            await cursor.execute(
                    "UPDATE objetivos SET selecionado = 1 WHERE id = ?",
                    (objetivo_id,)
                )
        await db.database.commit()
