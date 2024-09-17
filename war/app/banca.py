import asyncio
from database_manager import Database
from interfaces.jogador_interface import JogadorInterface
from cores import CoresManager
from cartas_objetivos import Objetivos
from jogador_manager import JogadorManager
from dado import Dado
from cartas_territorio import CartasTerritorios
class Banca():
    
    def __init__(self):
        self.cores = CoresManager('war/app/rsc/cores.json')
        self.objetivos = Objetivos('war/app/rsc/cartas_objetivos.json')
        self.cartas_territorio = CartasTerritorios('war/app/rsc/cartas_territorio.json')
        self.dado_amarelo_1 = Dado('amarelo')
        self.dado_amarelo_2 = Dado('amarelo')
        self.dado_vermelho_1 = Dado('vermelho')
        self.dado_vermelho_2 = Dado('vermelho')
        self.ordem_jogadores = None
        self.ultimo_jogador_jogando = None
        
    async def criar_jogo(self):
        try:
            db = await Database.get_instance()
            await db.criar_tabela_cores()
            await db.criar_tabela_jogador()
            await db.criar_tabela_cartas_territorio()
            await db.criar_tabela_exercito()
            await db.criar_tabela_objetivos()
            await self.cores.inserir_cores_do_json()
            await self.objetivos.inserir_objetivos()
            await self.cartas_territorio.inserir_cartas_territorio()
            return "Jogo iniciado com sucecesso"
        except Exception as e:
            return f"Não foi possível criar o jogo devido ao erro: {str(e)}"    
        
    async def adicionar_jogador(self, jogador :JogadorInterface):
        return await jogador.adicionar_jogador()
    
    async def jogador_escolhe_cor(self,nome,cor,jogador:JogadorInterface):
        return await jogador.escolher_cor_exercito(nome,cor)
    
    async def atribuir_objetivos(self,jogador:JogadorInterface):
        self.jogador_manager = JogadorManager(jogador,self.objetivos)
        await self.jogador_manager.atribuir_objetivos()
    
    async def get_objetivo_jogador(self,nome,jogador:JogadorInterface):
       return await jogador.get_objetivo(self,nome)
   
    async def distribuir_cartas_territorio(self, jogador: JogadorInterface, territorios: CartasTerritorios):
        
        self.jogador_manager = JogadorManager(jogador, self.objetivos)
        jogadores = await self.jogador_manager.get_jogadores()
        cartas = await territorios.get_cartas_territorio(self)
        numero_jogadores = await self.jogador_manager.get_numero_jogadores()
        resultado_sorteio = await self.jogador_manager.sortear_maior_numero(self.dado_amarelo_1)
        id_jogador_vencedor = resultado_sorteio['id_jogador_vencedor']
        
        
        jogadores_ordenados = sorted(
            jogadores,
            key=lambda x: (x[0] - id_jogador_vencedor) % numero_jogadores
        )
        self.ordem_jogadores = jogadores_ordenados
        for index, carta in enumerate(cartas):
            jogador_atual = jogadores_ordenados[index % numero_jogadores]
            await self.atribuir_carta_territorio(jogador_atual[0], carta[0])
            
        self.ultimo_jogador_jogando = jogadores_ordenados[(index % len(jogadores))]
        return {"status": "Cartas distribuídas com sucesso"}

    async def definir_ordem_jogadores(self):
        if self.ordem_jogadores == None:
            return "Por favor distribua as cartas antes de definir a ordem"
        else:
            posicao_ultimo = self.ordem_jogadores.index(self.ultimo_jogador_jogando)
            jogadores_reordenados = self.ordem_jogadores[posicao_ultimo+1:] + self.ordem_jogadores[:posicao_ultimo+1]
            self.ordem_jogadores = jogadores_reordenados
            return self.ordem_jogadores
   
    async def atribuir_carta_territorio(self,  jogador_id,carta_id):
        db = await Database.get_instance()
        query = """
        UPDATE cartas_territorio 
        SET jogador_id = ?, selecionado = 1 
        WHERE id = ? AND selecionado != 1
        """
        await db.execute_query(query, (jogador_id, carta_id))

            
            
            
    


