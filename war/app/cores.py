import json
from database_manager import Database 
class CoresManager:
    
    def __init__(self, path):
        
        self.path = path
        with open(self.path, 'r') as file:
            self.data = json.load(file)
        self.cores = self.data['cores']
        
    async def inserir_cores_do_json(self):
        db = await Database.get_instance()
        cores = self.cores
        for cor in cores:
            nome = cor['nome']
            codigo_hex = cor['codigo_hex']
            query = """INSERT OR IGNORE INTO cores (nome, codigo_hex, selecionado) VALUES (?, ?, 0)"""
            await db.execute_query(query, (nome, codigo_hex))