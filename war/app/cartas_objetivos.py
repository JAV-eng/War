import json
from database_gerenciador import Database

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