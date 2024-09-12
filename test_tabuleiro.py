import unittest
from tabuleiro import Tabuleiro
from exercito import Exercito
from territorio import Territorio

class TestTabuleiro(unittest.TestCase):
    def setUp(self):
        self.exercito = Exercito("Exercito1", "Infantaria", 100, 1)
        self.territorio = Territorio("Territorio1", [], 1)
        self.id_tabuleiro = 1
        self.cartas_terr = ["Carta1", "Carta2"]
        self.cartas_obj = ["Objetivo1", "Objetivo2"]
        self.tabuleiro = Tabuleiro(self.territorio, self.exercito, self.id_tabuleiro, self.cartas_terr, self.cartas_obj)

    def test_informacoes_Tabuleiro(self):
        expected_output = '{"nome": "Territorio1", "exercito": "Exercito1"}'
        self.assertEqual(self.tabuleiro.informacoes_Tabuleiro(), expected_output)

    def test_id_tabuleiro(self):
        self.assertEqual(self.tabuleiro.id_tabuleiro, 1)

    def test_cartas_terr(self):
        self.assertEqual(self.tabuleiro.cartas_terr, ["Carta1", "Carta2"])

    def test_cartas_obj(self):
        self.assertEqual(self.tabuleiro.cartas_obj, ["Objetivo1", "Objetivo2"])

if __name__ == '__main__':
    unittest.main()