import random
class Dado():
    
    def __init__(self,tipo):

        self.tipo = self.validar_tipo(tipo)
        
    def validar_tipo(self,tipo):
        if tipo == 'Amarelo' or tipo == 'amarelo':
            return 'amarelo'
        elif tipo =='Vermelho' or tipo == 'vermelho':
            return 'vermelho'
        else :
            raise ValueError('Tipo de dado não suportado ')
    def sortear_numero(self):
        return random.randrange(1,6)