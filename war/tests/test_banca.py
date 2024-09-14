import pytest
import httpx
from httpx import ASGITransport
from main import app

@pytest.mark.asyncio
async def test_adicionar_jogador():
    async with httpx.AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/adicionar_jogador/azul")
    assert response.status_code == 200
    assert response.json() == {"message": "Jogador da cor azul adicionado !"}
