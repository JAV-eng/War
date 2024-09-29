import pytest
from unittest.mock import AsyncMock, MagicMock

# Supondo que InsertStrategy e SelectStrategy estão em um módulo chamado your_module
from war.app.cartas_statagy import InsertStrategy, SelectStrategy

@pytest.fixture
async def mock_db():
    """Fixture para simular um banco de dados."""
    db = MagicMock()  # Usamos MagicMock para criar um objeto com métodos customizáveis
    db.execute = AsyncMock()  # Adiciona o método execute como um método assíncrono
    db.execute.return_value.__aenter__.return_value.fetchall.return_value = [
        {"territorio": "Territorio1", "simbolo": 1, "jogador_id": 1, "selecionado": 0},
        {"territorio": "Territorio2", "simbolo": 2, "jogador_id": 2, "selecionado": 0},
    ]
    yield db

@pytest.mark.asyncio
async def test_insert_strategy(mock_db):
    """Teste para verificar a inserção de cartas."""
    db = MagicMock()  # Usamos MagicMock para criar um objeto com métodos customizáveis
    db.execute_query = AsyncMock() 
    insert_strategy = InsertStrategy()
    
    # Dados de exemplo para inserção
    cartas = [
        {"territorio": "Territorio1", "simbolo": 1, "jogador_id": 1},
        {"territorio": "Territorio2", "simbolo": 2, "jogador_id": 2}
    ]
    
    # Chama o método de inserção
    await insert_strategy.inserir(mock_db, "cartas_territorio", cartas)

    # Verifica se o método execute_query foi chamado corretamente
    expected_query = "INSERT OR IGNORE INTO cartas_territorio (territorio, simbolo, jogador_id, selecionado) VALUES (?, ?, ?, 0)"
    expected_values_1 = ("Territorio1", 1, 1)
    expected_values_2 = ("Territorio2", 2, 2)

    # Verifica se o método foi chamado com as cartas
    mock_db.execute_query.assert_any_call(expected_query, expected_values_1)
    mock_db.execute_query.assert_any_call(expected_query, expected_values_2)

@pytest.mark.asyncio
async def test_select_strategy(mock_db):
    """Teste para verificar a seleção de cartas."""
    select_strategy = SelectStrategy()
    
    # Chama o método de seleção
    resultado = await select_strategy.selecionar(mock_db, "cartas_territorio", 2)
    
    # Verifica se o resultado retornado é o esperado
    assert len(resultado) == 2
    assert resultado[0]["territorio"] == "Territorio1"
    assert resultado[1]["territorio"] == "Territorio2"
