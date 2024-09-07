import unittest
from exercito import Exercito

class TestExercito(unittest.TestCase):
    def test_init(self):
        cor = "vermelho"
        tipo = "infantaria"
        quantidade = 100
        id_exercito = 1
        
        exercito = Exercito(cor, tipo, quantidade, id_exercito)
        
        self.assertEqual(exercito.cor, cor)
        self.assertEqual(exercito.tipo, tipo)
        self.assertEqual(exercito.quantidade, quantidade)
        self.assertEqual(exercito.id_exercito, id_exercito)

if __name__ == '__main__':
    unittest.main()