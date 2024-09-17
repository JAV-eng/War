import pytest
import aiosqlite
from war.app.database_manager import Database

@pytest.mark.asyncio
async def test_get_instance_singleton():
    # Ensure that get_instance returns the same instance every time
    instance1 = await Database.get_instance()
    instance2 = await Database.get_instance()
    assert instance1 is instance2

@pytest.mark.asyncio
async def test_get_instance_initialization():
    # Ensure that the database is initialized properly
    instance = await Database.get_instance()
    assert instance.database is not None
    assert instance.initialized is True

@pytest.mark.asyncio
async def test_get_instance_database_connection():
    # Ensure that the database connection is established
    instance = await Database.get_instance()
    async with instance.database.execute("SELECT name FROM sqlite_master WHERE type='table';") as cursor:
        tables = await cursor.fetchall()
        assert tables is not None

# Clean up the database after tests
@pytest.fixture(scope="module", autouse=True)
async def cleanup():
    yield
    instance = await Database.get_instance()
    await instance.close()