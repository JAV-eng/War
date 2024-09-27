import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from war.app.jogador import Jogador
from war.app.database_manager import Database


@pytest.mark.asyncio
async def test_adicionar_jogador_sucesso():
    jogador = Jogador("José")

    # Mock do Database
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_db.return_value.execute_query = AsyncMock(return_value=None)

        resultado = await jogador.adicionar_jogador()

        mock_db.return_value.execute_query.assert_called_once_with(
            'INSERT INTO jogador (nome) VALUES (?)', ("José",)
        )

        assert resultado == 'Jogador "José" adicionado com sucesso!'


@pytest.mark.asyncio
async def test_adicionar_jogador_erro():
    jogador = Jogador("José")

    # Simulando um erro no banco de dados
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_db.return_value.execute_query = AsyncMock(side_effect=Exception("Falha ao inserir"))

        resultado = await jogador.adicionar_jogador()

        mock_db.return_value.execute_query.assert_called_once_with(
            'INSERT INTO jogador (nome) VALUES (?)', ("José",)
        )

        assert resultado == 'Erro ao adicionar jogador: Falha ao inserir'


@pytest.mark.asyncio
async def test_escolher_cor_exercito_sucesso():
    jogador = Jogador("José")

    # Mock do Database
    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_cursor = AsyncMock()
        mock_db.return_value.database.cursor.return_value = mock_cursor

        # Simulando a cor encontrada e não selecionada
        mock_cursor.fetchone.return_value = (1, False)

        resultado = await jogador.escolher_cor_exercito("José", "Azul")

        mock_cursor.execute.assert_called_once_with('SELECT id, selecionado FROM cores WHERE nome = ?', ('Azul',))
        mock_db.return_value.execute_query.assert_any_call(
            'UPDATE jogador SET cor_id = ? WHERE nome = ?', (1, "José")
        )
        mock_db.return_value.execute_query.assert_any_call(
            'UPDATE cores SET selecionado = 1 WHERE id = ?', (1,)
        )

        assert resultado == 'Cor do jogador "José" atualizada para "Azul" com sucesso!'


@pytest.mark.asyncio
async def test_escolher_cor_exercito_cor_ja_selecionada():
    jogador = Jogador("José")

    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_cursor = AsyncMock()
        mock_db.return_value.database.cursor.return_value = mock_cursor

        # Simulando a cor encontrada e já selecionada
        mock_cursor.fetchone.return_value = (1, True)

        resultado = await jogador.escolher_cor_exercito("José", "Azul")

        assert resultado == 'A cor "Azul" já foi selecionada por outro jogador.'


@pytest.mark.asyncio
async def test_escolher_cor_exercito_cor_inexistente():
    jogador = Jogador("José")

    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_cursor = AsyncMock()
        mock_db.return_value.database.cursor.return_value = mock_cursor

        # Simulando que a cor não foi encontrada
        mock_cursor.fetchone.return_value = None

        resultado = await jogador.escolher_cor_exercito("José", "Azul")

        assert resultado == 'A cor "Azul" não existe no banco de dados.'


@pytest.mark.asyncio
async def test_get_objetivo_sucesso():
    jogador = Jogador("José")

    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_cursor = AsyncMock()
        mock_db.return_value.database.cursor.return_value = mock_cursor

        # Simulando a obtenção de um objetivo
        mock_cursor.fetchone.return_value = {"id": 1, "descricao": "Conquistar o mundo"}

        resultado = await jogador.get_objetivo("José")

        mock_cursor.execute.assert_called_once_with(
            '''
            SELECT o.*
            FROM objetivos o
            JOIN jogador j ON j.objetivo_id = o.id
            WHERE j.nome = ?
            ''',
            ("José",)
        )

        assert resultado == {"id": 1, "descricao": "Conquistar o mundo"}


@pytest.mark.asyncio
async def test_get_objetivo_nao_encontrado():
    jogador = Jogador("José")

    with patch.object(Database, 'get_instance', return_value=AsyncMock()) as mock_db:
        mock_cursor = AsyncMock()
        mock_db.return_value.database.cursor.return_value = mock_cursor

        # Simulando a ausência de objetivo
        mock_cursor.fetchone.return_value = None

        resultado = await jogador.get_objetivo("José")

        assert resultado == "Nenhum objetivo encontrado para o jogador com o nome fornecido."
