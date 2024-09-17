class TestJogadorManager(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.mock_jogador_interface = AsyncMock(spec=JogadorInterface)
        self.mock_objetivos = AsyncMock(spec=Objetivos)
        self.jogador_manager = JogadorManager(self.mock_jogador_interface, self.mock_objetivos)

    @patch('jogador_manager.Database')
    async def test_atribuir_objetivos(self, mock_database):
        # Mock database instance and cursor
        mock_db_instance = AsyncMock()
        mock_cursor = AsyncMock()
        mock_database.get_instance.return_value = mock_db_instance
        mock_db_instance.database.cursor.return_value.__aenter__.return_value = mock_cursor

        #