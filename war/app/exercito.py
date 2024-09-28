from .database_manager import Database
class Exercitos():
    
    def __init__(self) -> None:
        pass
    
    async def adicionar_exercito(self, cor, tipo, quantidade, jogador_id):
        db = await Database.get_instance()
        query = """
            INSERT INTO exercito (cor, tipo, quantidade, jogador_id)
            VALUES (?, ?, ?, ?)
        """
        await db.execute_query(query, (cor, tipo, quantidade, jogador_id))
        
    async def remover_exercitos(self, jogador_id):
        db = await Database.get_instance()
        query = """
            DELETE FROM exercito
            WHERE jogador_id = ?
        """
        await db.execute_query(query, (jogador_id,))
        
    async def limpar_exercitos(self):
        db = await Database.get_instance()
        query = "DELETE FROM exercito"
        await db.execute_query(query)


