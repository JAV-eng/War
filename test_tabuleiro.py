import unittest
from tabuleiro import Tabuleiro

class TestTabuleiro(unittest.TestCase):
    def test_init(self):
        exercito = "Exercito1"
        id_tabuleiro = 1
        cartas_terr = ["Territorio1", "Territorio2"]
        cartas_obj = ["Objetivo1", "Objetivo2"]
        
        tabuleiro = Tabuleiro(exercito, id_tabuleiro, cartas_terr, cartas_obj)
        
        self.assertEqual(tabuleiro.exercito, exercito)
        self.assertEqual(tabuleiro.id_tabuleiro, id_tabuleiro)
        self.assertEqual(tabuleiro.cartas_terr, cartas_terr)
        self.assertEqual(tabuleiro.cartas_obj, cartas_obj)

if __name__ == '__main__':
    unittest.main()