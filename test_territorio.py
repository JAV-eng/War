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
    def test_set_vizinhos(self):
        self.territorio._vizinhos = ["Territorio2", "Territorio3"]
        self.assertEqual(self.territorio.vizinhos(), ["Territorio2", "Territorio3"])

    def test_add_vizinho(self):
        self.territorio._vizinhos.append("Territorio2")
        self.assertIn("Territorio2", self.territorio.vizinhos())

    def test_remove_vizinho(self):
        self.territorio._vizinhos = ["Territorio2", "Territorio3"]
        self.territorio._vizinhos.remove("Territorio2")
        self.assertNotIn("Territorio2", self.territorio.vizinhos())
if __name__ == '__main__':
    unittest.main()