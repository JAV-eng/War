import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jogador import Jogador  

def test_escolhe_cor_valida():
    jogador = Jogador('Amarelo', 'Objetivo1', 'Carta1')
    resposta = jogador.escolhe_cor(1)
    assert resposta == "Você escolheu a cor: Amarelo"
    assert jogador.cor_jogador == 'Amarelo'

def test_escolhe_cor_invalida():
    jogador = Jogador('Amarelo', 'Objetivo1', 'Carta1')
    resposta = jogador.escolhe_cor(10)  
    assert resposta == "Escolha inválida. Tente novamente."
    assert jogador.cor_jogador == 'Amarelo'  

def test_escolhe_cor_com_index_duplicado():
    jogador = Jogador('Azul', 'Objetivo1', 'Carta1')
    resposta = jogador.escolhe_cor(6) 
    assert resposta == "Você escolheu a cor: Amarelo"
    assert jogador.cor_jogador == 'Amarelo'