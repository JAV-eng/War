class Territorio:
    def __init__(self, nome, vizinhos, id_territorio):
        self.nome = nome
        self.vizinhos = []
        self.id_territorio = id_territorio

    def vizinhos(self):
        return self.vizinhos

    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome
    def get_id_territorio(self):
        return self.id_territorio
    def set_id_territorio(self, id_territorio):
        self.id_territorio = id_territorio