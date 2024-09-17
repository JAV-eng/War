import unittest
from unittest.mock import AsyncMock, patch
from banca import Banca
from interfaces.jogador_interface import JogadorInterface

class TestBanca(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.banca = Banca()

    @patch('banca.Database')
    @patch('banca.CoresManager')
    @patch('banca.Objetivos')
    async def test_criar_jogo(self, MockObjetivos, MockCoresManager, MockDatabase):
        # Mocking the database instance and methods
        mock_db_instance = AsyncMock()
        MockDatabase.get_instance.return_value = mock_db_instance

        # Mocking the CoresManager and Objetivos methods
        mock_cores_manager = AsyncMock()
        mock_objetivos = AsyncMock()
        MockCoresManager.return_value = mock_cores_manager
        MockObjetivos.return_value = mock_objetivos

        result = await self.banca.criar_jogo()
        self.assertEqual(result, "Jogo iniciado com sucecesso")

    @patch.object(JogadorInterface, 'adicionar_jogador', new_callable=AsyncMock)
    async def test_adicionar_jogador(self, mock_adicionar_jogador):
        mock_jogador = AsyncMock(spec=JogadorInterface)
        result = await self.banca.adicionar_jogador(mock_jogador)
        mock_adicionar_jogador.assert_awaited_once()
        self.assertEqual(result, mock_adicionar_jogador.return_value)

    @patch.object(JogadorInterface, 'escolher_cor_exercito', new_callable=AsyncMock)
    async def test_jogador_escolhe_cor(self, mock_escolher_cor_exercito):
        mock_jogador = AsyncMock(spec=JogadorInterface)
        result = await self.banca.jogador_escolhe_cor('nome', 'cor', mock_jogador)
        mock_escolher_cor_exercito.assert_awaited_once_with('nome', 'cor')
        self.assertEqual(result, mock_escolher_cor_exercito.return_value)

    @patch('banca.JogadorManager')
    async def test_atribuir_objetivos(self, MockJogadorManager):
        mock_jogador = AsyncMock(spec=JogadorInterface)
        mock_jogador_manager = AsyncMock()
        MockJogadorManager.return_value = mock_jogador_manager

        await self.banca.atribuir_objetivos(mock_jogador)
        mock_jogador_manager.atribuir_objetivos.assert_awaited_once()

    @patch.object(JogadorInterface, 'get_objetivo', new_callable=AsyncMock)
    async def test_get_objetivo_jogador(self, mock_get_objetivo):
        mock_jogador = AsyncMock(spec=JogadorInterface)
        result = await self.banca.get_objetivo_jogador('nome', mock_jogador)
        mock_get_objetivo.assert_awaited_once_with(self.banca, 'nome')
        self.assertEqual(result, mock_get_objetivo.return_value)

if __name__ == '__main__':
    unittest.main()