import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, patch
from cartas_objetivos import Objetivos

@pytest_asyncio.fixture
async def mock_db():
    with patch('cartas_objetivos.Database') as MockDatabase:
        mock_db_instance = AsyncMock()
        MockDatabase.get_instance.return_value = mock_db_instance
        yield mock_db_instance

@pytest_asyncio.fixture
async def objetivos_instance():
    data = {
        "objetivos": [
            {"nome": "Objetivo 1", "descricao": "Descricao 1"},
            {"nome": "Objetivo 2", "descricao": "Descricao 2"}
        ]
    }
    with patch('builtins.open', patch('json.load', return_value=data)):
        objetivos = Objetivos('fake_path')
        yield objetivos

@pytest.mark.asyncio
async def test_inserir_objetivos(mock_db, objetivos_instance):
    await objetivos_instance.inserir_objetivos()
    
    assert mock_db.execute_query.call_count == 2
    mock_db.execute_query.assert_any_call(
        "INSERT OR IGNORE INTO objetivos (nome, descricao, selecionado) VALUES (?, ?, 0)",
        ("Objetivo 1", "Descricao 1")
    )
    mock_db.execute_query.assert_any_call(
        "INSERT OR IGNORE INTO objetivos (nome, descricao, selecionado) VALUES (?, ?, 0)",
        ("Objetivo 2", "Descricao 2")
    )