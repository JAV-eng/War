import random
class Dado():
    
    def __init__(self,tipo):
        self.tipo = tipo
        
    def sortear_numero(self):
        return random.randrange(1,6)