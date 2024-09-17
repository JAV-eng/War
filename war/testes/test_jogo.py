import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from jogo import Jogo

@pytest.fixture
def app():
    app = FastAPI()
    jogo = Jogo(app)
    return app

@pytest.fixture
async def client(app):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_criar_jogo(client):
    response = await client.get('/criar_jogo')
    assert response.status_code == 200
    # Add more assertions based on the expected response

@pytest.mark.asyncio
async def test_get_objetivos(client):
    response = await client.get('/get_objetivos/test_player')
    assert response.status_code == 200
    # Add more assertions based on the expected response

@pytest.mark.asyncio
async def test_adicionar_jogador(client):
    response = await client.get('/adicionar_jogador/test_player')
    assert response.status_code == 200
    # Add more assertions based on the expected response

@pytest.mark.asyncio
async def test_jogador_escolhe_cor(client):
    response = await client.get('/jogador_escolhe_cor/test_player/red')
    assert response.status_code == 200
    # Add more assertions based on the expected response

@pytest.mark.asyncio
async def test_sortear_objetivos(client):
    response = await client.get('/sortear_objetivos')
    assert response.status_code == 200
    # Add more assertions based on the expected response

# Add more tests for the remaining endpoints when they are implemented