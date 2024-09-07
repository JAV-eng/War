class Exercito:
    def __init__(self, cor,tipo,quantidade, id_exercito):
        self.tipo = tipo
        self.cor =cor
        self.id_exercito = id_exercito
        self.quantidade = quantidade

    def somar_quantidade(self, valor):
        self.quantidade = self.quantidade + valor
    
    def subtrair_quantidade(self, valor):
        self.quantidade = self.quantidade - valor
    




    def get_cor(self):
        return self.cor
    def set_cor(self, cor):
        self.cor = cor
    def get_tipo(self):
        return self.tipo
    def set_tipo(self, tipo):
        self.tipo = tipo
    def get_quantidade(self):
        return self.quantidade
    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
    def get_id_exercito(self):
        return self.id_exercito
    def set_id_exercito(self, id_exercito):
        self.id_exercito = id_exercito