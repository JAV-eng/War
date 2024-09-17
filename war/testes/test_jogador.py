import pytest
from unittest.mock import AsyncMock, patch
from jogador import Jogador
from database_manager import Database

@pytest.mark.asyncio
async def test_adicionar_jogador():
    # Cria um mock para a instância do banco de dados
    mock_db = AsyncMock()
    
    # Substitui o método get_instance da classe Database para retornar o mock_db
    with patch.object(Database, 'get_instance', return_value=mock_db):
        # Cria uma instância do Jogador
        jogador = Jogador(nome="JogadorTeste")
        
        # Define o mock para o método execute_query
        mock_db.execute_query = AsyncMock()
        
        # Chama o método adicionar_jogador
        await jogador.adicionar_jogador()
        
        # Verifica se execute_query foi chamado com os parâmetros corretos
        mock_db.execute_query.assert_called_once_with(
            'INSERT INTO jogador (nome) VALUES (?)', ("JogadorTeste",)
        )
        print("Teste passou!")
