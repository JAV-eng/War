import pytest
import aiosqlite
from app.database_gerenciador import Database

@pytest.mark.asyncio
async def test_database_connection():
    
    db = Database()
    db.db_path = ":memory:"  
    await db.connect()
    await db.criar_jogo()

    async with db.connection.cursor() as cursor:
        await cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='jogador';")
        result = await cursor.fetchone()
        assert result is not None, "Tabela 'jogador' não foi criada"

        await cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='exercito';")
        result = await cursor.fetchone()
        assert result is not None, "Tabela 'exercito' não foi criada"

    await db.execute_query("INSERT INTO jogador (cor, objetivo) VALUES (?, ?)", ("Azul", "Conquistar territórios"))

  
    async with db.connection.cursor() as cursor:
        await cursor.execute("SELECT * FROM jogador WHERE cor = ?", ("Azul",))
        jogador = await cursor.fetchone()
        assert jogador is not None, "Jogador não foi inserido corretamente"
        assert jogador[1] == "Azul", "A cor do jogador está incorreta"
        assert jogador[2] == "Conquistar territórios", "O objetivo do jogador está incorreto"

    await db.close()

