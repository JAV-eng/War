import unittest
from territorio import Territorio

class TestTerritorio(unittest.TestCase):

    def setUp(self):
        self.territorio = Territorio("Territorio1", [], 1)

    def test_get_nome(self):
        self.assertEqual(self.territorio.get_nome(), "Territorio1")

    def test_set_nome(self):
        self.territorio.set_nome("NovoNome")
        self.assertEqual(self.territorio.get_nome(), "NovoNome")

    def test_get_id_territorio(self):
        self.assertEqual(self.territorio.get_id_territorio(), 1)

    def test_set_id_territorio(self):
        self.territorio.set_id_territorio(2)
        self.assertEqual(self.territorio.get_id_territorio(), 2)

    def test_vizinhos_initially_empty(self):
        self.assertEqual(self.territorio.vizinhos(), [])

if __name__ == '__main__':
    unittest.main()