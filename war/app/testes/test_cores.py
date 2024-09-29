import pytest
import json
from unittest.mock import patch, mock_open, AsyncMock
from war.app.database_manager import InsertStrategy, SelectStrategy  # Ajuste o nome do módulo conforme necessário
from war.app.database_manager import Database
# Mock data for the tests
mock_cartas_data = json.dumps([
    {"territorio": "Territorio1", "simbolo": 1, "jogador_id": 1},
    {"territorio": "Territorio2", "simbolo": 2, "jogador_id": 2}
])

@pytest.fixture
def mock_open_cartas_file():
    with patch("builtins.open", mock_open(read_data=mock_cartas_data)) as mock_file:
        yield mock_file

@pytest.mark.asyncio
async def test_inserir_cartas_sucesso(mock_open_cartas_file):
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_db.return_value.execute_query = AsyncMock()

        insert_strategy = InsertStrategy()
        
        # Simulando a leitura das cartas do JSON
        cartas = json.loads(mock_cartas_data)

        await insert_strategy.inserir(mock_db, "cartas_territorio", cartas)

        expected_query = """INSERT OR IGNORE INTO cartas_territorio (territorio, simbolo, jogador_id, selecionado) VALUES (?, ?, ?, 0)"""
        
        # Verificamos se a função execute_query foi chamada com os valores corretos
        mock_db.return_value.execute_query.assert_any_call(expected_query, ("Territorio1", 1, 1))
        mock_db.return_value.execute_query.assert_any_call(expected_query, ("Territorio2", 2, 2))

        assert mock_db.return_value.execute_query.call_count == 2

@pytest.mark.asyncio
async def test_inserir_cartas_arquivo_vazio():
    empty_json = json.dumps([])
    
    with patch("builtins.open", mock_open(read_data=empty_json)):
        with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
            mock_db.return_value.execute_query = AsyncMock()

            insert_strategy = InsertStrategy()

            await insert_strategy.inserir(mock_db, "cartas_territorio", [])

            # Verifica se a função execute_query não foi chamada
            mock_db.return_value.execute_query.assert_not_called()

@pytest.mark.asyncio
async def test_selecionar_cartas_sucesso():
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_db.return_value.execute = AsyncMock()
        mock_db.return_value.execute.return_value.__aenter__.return_value.fetchall.return_value = [
            {"territorio": "Territorio1", "simbolo": 1, "jogador_id": 1, "selecionado": 0},
            {"territorio": "Territorio2", "simbolo": 2, "jogador_id": 2, "selecionado": 0}
        ]
        
        select_strategy = SelectStrategy()
        resultado = await select_strategy.selecionar(mock_db, "cartas_territorio", 2)

        # Verifica se o resultado contém as cartas esperadas
        assert len(resultado) == 2
        assert resultado[0]["territorio"] == "Territorio1"
        assert resultado[1]["territorio"] == "Territorio2"

@pytest.mark.asyncio
async def test_selecionar_cartas_sem_resultados():
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_db.return_value.execute = AsyncMock()
        mock_db.return_value.execute.return_value.__aenter__.return_value.fetchall.return_value = []

        select_strategy = SelectStrategy()
        resultado = await select_strategy.selecionar(mock_db, "cartas_territorio", 2)

        # Verifica se o resultado é uma lista vazia
        assert len(resultado) == 0
