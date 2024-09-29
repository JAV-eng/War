import pytest
import asyncio
from war.app.database_manager import Database  # Substitua pelo seu módulo real

@pytest.fixture
async def db_instance():
    
    db = Database()  # Cria uma nova instância do gerenciador de banco de dados
    await db.get_instance()
    yield db  
    await db.close()  # Fecha a conexão após os testes

@pytest.mark.asyncio
async def test_init_db(db_instance):
    
    assert db_instance is not None, "Database instance should be initialized."
    assert db_instance.get_instance() is not None, "Database should be initialized." 
    