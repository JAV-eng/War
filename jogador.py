class Jogador:
    def __init__(self,cor_jogador, objetivo, carta_territorio):
        self.carta_territorio = carta_territorio
        self.objetivo = objetivo
        self.cor_jogador = cor_jogador

    def escolhe_cor(self, escolha):
        cores_disponiveis = [[['Amarelo'],[]], [['Branco'],[]], [['Azul'],[]], [['Preto'],[]], [['Verde'],[]], [['Amarelo'],[]]]

        if 1 <= escolha <= len(cores_disponiveis):
            self.cor_jogador = cores_disponiveis[escolha - 1][0][0]
            return f"Você escolheu a cor: {self.cor_jogador}"
        else:
            return "Escolha inválida. Tente novamente."
        