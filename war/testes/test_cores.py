import unittest
from unittest.mock import AsyncMock, patch, mock_open
from app.cores import CoresManager

class TestCoresManager(unittest.IsolatedAsyncioTestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"cores": [{"nome": "vermelho", "codigo_hex": "#FF0000"}]}')
    @patch('app.cores.Database')
    async def test_inserir_cores_do_json(self, mock_database, mock_file):
        # Arrange
        mock_db_instance = AsyncMock()
        mock_database.get_instance.return_value = mock_db_instance
        cores_manager = CoresManager('fake_path')

        # Act
        await cores_manager.inserir_cores_do_json()

        # Assert
        mock_database.get_instance.assert_called_once()
        mock_db_instance.execute_query.assert_called_once_with(
            """INSERT OR IGNORE INTO cores (nome, codigo_hex, selecionado) VALUES (?, ?, 0)""",
            ('vermelho', '#FF0000')
        )

if __name__ == '__main__':
    unittest.main()