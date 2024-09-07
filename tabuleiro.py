
import json
import territorio
import exercito
class Tabuleiro:
    def __init__(self, exercito, id_tabuleiro,  cartas_terr, cartas_obj):
        self.exercito = exercito
        self.id_tabuleiro = id_tabuleiro
        self.cartas_terr = cartas_terr
        self.cartas_obj = cartas_obj
    territorio_json = json.dumps({"nome": territorio , "exercito": exercito, "id_tabuleiro": self.id_tabuleiro})
    def informacoes_Tabuleiro(self):
        return self.territorio_json