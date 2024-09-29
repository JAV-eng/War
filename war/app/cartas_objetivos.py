import json
from .database_manager import Database

class Objetivos:
    def __init__(self, path, repository):
        self.path = path
        self.repository = repository
        with open(self.path, 'r') as file:
            self.data = json.load(file)
        self.objetivos = self.data['objetivos']

    async def inserir_objetivos(self):
        db = await Database.get_instance()
        await self.repository.inserir_cartas(db, self.objetivos)

    async def selecionar_objetivos(self, quantidade):
        db = await Database.get_instance()
        return await self.repository.selecionar_cartas(db, quantidade)

    async def set_selecionado(self, objetivo_id):
        db = await Database.get_instance()
        await self.repository.set_selecionado(db, objetivo_id)
