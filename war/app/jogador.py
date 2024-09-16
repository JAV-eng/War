import asyncio
from interfaces import JogadorInterface
from database_gerenciador import Database

class Jogador(JogadorInterface):
    
    def __init__(self, nome):
        self.nome = nome

    async def adicionar_jogador(self):
        db = await Database.get_instance()
        try:
            query = 'INSERT INTO jogador (nome) VALUES (?)'
            await db.execute_query(query, (self.nome,))
            return(f'Jogador "{self.nome}" adicionado com sucesso!')
        except Exception as e:
            return(f'Erro ao adicionar jogador: {e}')


    async def escolher_cor_exercito(self, nome,cor):
        db = await Database.get_instance()

        try:
            query_cor = 'SELECT id, selecionado FROM cores WHERE nome = ?'
            async with db.database.cursor() as cursor:
                await cursor.execute(query_cor, (cor,))
                cor_info = await cursor.fetchone()
            
            if cor_info is None:
                return f'A cor "{cor}" não existe no banco de dados.'
            
            cor_id, selecionado = cor_info

            if selecionado:
                return f'A cor "{cor}" já foi selecionada por outro jogador.'

            query_atualizar_jogador = 'UPDATE jogador SET cor_id = ? WHERE nome = ?'
            await db.execute_query(query_atualizar_jogador, (cor_id,nome))

            query_atualizar_cor = 'UPDATE cores SET selecionado = 1 WHERE id = ?'
            await db.execute_query(query_atualizar_cor, (cor_id,))

            self.cor = cor
            return f'Cor do jogador "{nome}" atualizada para "{cor}" com sucesso!'

        except Exception as e:
            return f'Erro ao atualizar cor do jogador: {e}'
        

    
    async def get_cor_exercito(self):
        # Implementação necessária
        pass
    
    async def set_objetivo(self):
        # Implementação necessária
        pass
    
    async def get_objetivo(self):
        # Implementação necessária
        pass
    
    async def adicionar_exercito(self, exercito, quantidade, territorio):
        # Implementação necessária
        pass

