import json
import pytest
from unittest.mock import patch, mock_open, AsyncMock
from war.app.cartas_territorio import CartasTerritorios  # Ajuste o caminho conforme necessário.
from war.app.database_manager import Database

mock_json_data = json.dumps({
    "cartas_territorio": [
        { 
            "territorio": "Alasca", 
            "simbolo": "cavalaria", 
            "continente": "América do Norte",
            "vizinhos": ["Vancouver", "Sibéria"]
        },
        { 
            "territorio": "Vancouver", 
            "simbolo": "infantaria", 
            "continente": "América do Norte",
            "vizinhos": ["Alasca", "Califórnia", "Groelândia"]
        }
    ]
})

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data=mock_json_data)) as mock_file:
        yield mock_file

@pytest.mark.asyncio
async def test_inserir_cartas_territorio_sucesso(mock_open_file):
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_db.return_value.execute_query = AsyncMock()

        cartas_manager = CartasTerritorios('path/to/mock/file.json')

        await cartas_manager.inserir_cartas_territorio()

        mock_db.return_value.execute_query.assert_any_call(
            """INSERT OR IGNORE INTO cartas_territorio (territorio, simbolo, selecionado) VALUES (?, ?, 0)""",
            ("Alasca", "cavalaria")
        )
        mock_db.return_value.execute_query.assert_any_call(
            """INSERT OR IGNORE INTO cartas_territorio (territorio, simbolo, selecionado) VALUES (?, ?, 0)""",
            ("Vancouver", "infantaria")
        )

        assert mock_db.return_value.execute_query.call_count == 2

@pytest.mark.asyncio
async def test_get_cartas_territorio(mock_open_file):
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_cursor = AsyncMock()
        mock_cursor.fetchall.return_value = [(1,), (2,)]
        mock_db.return_value.execute.return_value.__aenter__.return_value = mock_cursor

        cartas_manager = CartasTerritorios('path/to/mock/file.json')

        result = await cartas_manager.get_cartas_territorio()

        assert result == [(1,), (2,)]
        mock_db.return_value.execute.assert_called_once_with(
            """SELECT id FROM cartas_territorio ORDER BY RANDOM()"""
        )

@pytest.mark.asyncio
async def test_get_cartas_territorio_jogador2(mock_open_file):
    jogador_id = 1
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        # Configurando o mock para o método execute_query
        mock_db.return_value.execute_query = AsyncMock()

        # Simulando o retorno da consulta SQL
        mock_db.return_value.execute_query.return_value = [(3,), (4,)]

        cartas_manager = CartasTerritorios('path/to/mock/file.json')

        result = await cartas_manager.get_cartas_territorio_jogador(jogador_id)

        assert result == [(3,), (4,)]
        mock_db.return_value.execute_query.assert_called_once_with(
            """
            SELECT id 
            FROM cartas_territorio 
            WHERE jogador_id = ?
            """, (jogador_id,)
        )
