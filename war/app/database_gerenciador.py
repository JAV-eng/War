import aiosqlite
import asyncio

class Database:
    _instance = None
    _lock = asyncio.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.db_path = "Database.db"
            self.connection = None
            self.initialized = True

    async def connect(self):
        if not self.connection:
            self.connection = await aiosqlite.connect(self.db_path)

    async def criar_tabela_exercito(self):
        sql = """CREATE TABLE IF NOT EXISTS exercito(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cor TEXT, 
        tipo INTEGER,
        quantidade INTEGER,
        jogador_id INTEGER,
        FOREIGN KEY (jogador_id) REFERENCES jogador(id))"""
        await self.execute_query(sql)

    async def criar_tabela_jogador(self):
        sql = '''CREATE TABLE IF NOT EXISTS jogador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cor TEXT,
            objetivo TEXT
        )'''
        await self.execute_query(sql)

    async def criar_tabela_cartas_territorio(self):
        sql = """CREATE TABLE IF NOT EXISTS cartas_territorio(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        territorio TEXT, 
        simbulo INTEGER,
        jogador_id INTEGER,
        FOREIGN KEY (jogador_id) REFERENCES jogador(id))"""
        await self.execute_query(sql)

    async def criar_jogo(self):
        await self.criar_tabela_jogador()
        await self.criar_tabela_cartas_territorio()
        await self.criar_tabela_exercito()

    async def execute_query(self, query, params=None):
        async with self.connection.cursor() as cursor:
            if params:
                await cursor.execute(query, params)
            else:
                await cursor.execute(query)
            await self.connection.commit()

    async def close(self):
        if self.connection:
            await self.connection.close()
            self.connection = None


