import aiosqlite
import asyncio

class Database:
    _instance = None
    
    @classmethod
    async def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            await cls._instance._init_db()
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):  
            self.database = None
            self.initialized = False
    
    async def _init_db(self):
        self.database = await aiosqlite.connect("./Database.db")
        self.execute = self.database.execute
        self.initialized = True  
    
    async def criar_tabela_jogador(self):
        sql = '''CREATE TABLE IF NOT EXISTS jogador (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                cor_id INTEGER,
                objetivo_id INTEGER,
                FOREIGN KEY (cor_id) REFERENCES cores(id),
                FOREIGN KEY (objetivo_id) REFERENCES objetivos(id)
            )'''
        await self.execute_query(sql)

    async def criar_tabela_cartas_territorio(self):
        sql = """CREATE TABLE IF NOT EXISTS cartas_territorio(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            territorio TEXT, 
            simbolo INTEGER,
            continente TEXT,
            vizinhos TEXT,
            jogador_id INTEGER,
            selecionado INTEGER DEFAULT 0,
            FOREIGN KEY (jogador_id) REFERENCES jogador(id))"""
        await self.execute_query(sql)
  
    async def criar_tabela_exercito(self):
        sql = """CREATE TABLE IF NOT EXISTS exercito(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cor TEXT, 
            tipo INTEGER,
            quantidade INTEGER,
            jogador_id INTEGER,
            FOREIGN KEY (jogador_id) REFERENCES jogador(id))"""
        await self.execute_query(sql)
    
    async def criar_tabela_cores(self):
        sql = """CREATE TABLE IF NOT EXISTS cores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE,
            codigo_hex TEXT UNIQUE,
            selecionado INTEGER DEFAULT 0
            )"""
        await self.execute_query(sql)

    async def criar_tabela_objetivos(self):
        sql = """CREATE TABLE IF NOT EXISTS objetivos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE,
                descricao TEXT UNIQUE,
                selecionado INTEGER DEFAULT 0
            )"""
        await self.execute_query(sql)
    async def criar_tabela_tabuleiro(self):
        sql = """
            CREATE TABLE IF NOT EXISTS tabuleiro(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                territorio TEXT,
                continente TEXT,
                territorios_vizinhos TEXT,
                exercitos_id INTEGER,
                FOREIGN KEY (exercitos_id) REFERENCES exercito(id)
            )
        """
        await self.execute_query(sql)

    async def execute_query(self, query, parameters=()):
        async with self.database.execute(query, parameters) as cursor:
            await self.database.commit()
    
    async def close(self):
        if self.database:
            await self.database.close()
