import json
from exercito import Exercito
from territorio import Territorio
class Tabuleiro:
    def __init__(self, territorio, exercito, id_tabuleiro, cartas_terr, cartas_obj):
        self.exercito = exercito
        self.territorio = territorio
        self.id_tabuleiro = id_tabuleiro
        self.cartas_terr = cartas_terr
        self.cartas_obj = cartas_obj

    def informacoes_Tabuleiro(self):
        territorio_json = json.dumps({"nome": self.territorio.get_nome(), "exercito": self.exercito.cor})
        return territorio_json

