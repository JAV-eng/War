from war.app.dado import Dado
import pytest

def test_criar_dado_vermelho():
    dado = Dado('Vermelho')
    assert dado.tipo == 'vermelho'
def test_criar_dado_amarelo():
    dado = Dado('Amarelo')
    assert dado.tipo =='amarelo'
def test_criar_dado_invalido():
   with pytest.raises(ValueError, match="Tipo de dado não suportado "):
        dado = Dado('azul')
def test_sorteio():
    numeros = [1,2,3,4,5,6]
    dado = Dado('Vermelho')
    valor = dado.sortear_numero()
    assert valor in numeros
    