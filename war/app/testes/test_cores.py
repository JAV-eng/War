import pytest
import json
from unittest.mock import patch, mock_open, AsyncMock
from war.app.cores import CoresManager
from war.app.database_manager import Database

mock_json_data = json.dumps({
    "cores": [
        {"nome": "Azul", "codigo_hex": "#0000FF"},
        {"nome": "Vermelho", "codigo_hex": "#FF0000"},
    ]
})

@pytest.fixture
def mock_open_file():
    with patch("builtins.open", mock_open(read_data=mock_json_data)) as mock_file:
        yield mock_file


@pytest.mark.asyncio
async def test_inserir_cores_do_json_sucesso(mock_open_file):
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_db.return_value.execute_query = AsyncMock()

        cores_manager = CoresManager('path/to/mock/file.json')

        await cores_manager.inserir_cores_do_json()

        mock_db.return_value.execute_query.assert_any_call(
            """INSERT OR IGNORE INTO cores (nome, codigo_hex, selecionado) VALUES (?, ?, 0)""",
            ("Azul", "#0000FF")
        )
        mock_db.return_value.execute_query.assert_any_call(
            """INSERT OR IGNORE INTO cores (nome, codigo_hex, selecionado) VALUES (?, ?, 0)""",
            ("Vermelho", "#FF0000")
        )

        assert mock_db.return_value.execute_query.call_count == 2


@pytest.mark.asyncio
async def test_inserir_cores_do_json_arquivo_vazio():
    empty_json = json.dumps({"cores": []})
    
    with patch("builtins.open", mock_open(read_data=empty_json)):
        with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
            mock_db.return_value.execute_query = AsyncMock()

            cores_manager = CoresManager('path/to/mock/file.json')

            await cores_manager.inserir_cores_do_json()

            mock_db.return_value.execute_query.assert_not_called()


@pytest.mark.asyncio
async def test_inserir_cores_do_json_erro_leitura():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            cores_manager = CoresManager('path/to/invalid/file.json')
