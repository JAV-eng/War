class Jogo:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        
        @self.app.get('/sortear_objetivos')
        async def sortear_objetivos(self):
            pass
        
        @self.app.get('/definir_ordem_jogadores')
        async def definir_ordem_jogadores(self):
            pass
        
        @self.app.get('/distribuir_territorios_iniciais')
        async def distribuir_territorios_iniciais(self):
            pass

    
    def routes(self):
        
        @self.app.get('/adicionar_jogador/{cor}')
        async def adiciona_jogador(cor: str):
            return {"message": f"Async 2 Hello {cor}"}

       