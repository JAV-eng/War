import sqlite3 as db

class Database:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):  # Garante que a inicialização ocorra apenas uma vez
            self.banco = db.connect("Database.db")
            self.cursor = self.banco.cursor()
            self.initialized = True  # Marca que a inicialização foi realizada
    
    def criar_tabela_exercito(self):
        cursor = self.cursor
        sql = """CREATE TABLE IF NOT EXISTS exercito(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cor TEXT, 
        tipo INTEGER,
        quantidade INTEGER,
        jogador_id INTEGER,
        FOREIGN KEY (jogador_id) REFERENCES jogador(id))"""
        cursor.execute(sql)
    
    def criar_tabela_jogador(self):
        sql = '''CREATE TABLE IF NOT EXISTS jogador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cor TEXT,
            objetivo TEXT
        )'''
        cursor = self.cursor
        cursor.execute(sql)
    
    def criar_tabela_cartas_territorio(self):
        sql = """CREATE TABLE IF NOT EXISTS cartas_territorio(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        territorio TEXT, 
        simbulo INTEGER,
        jogador_id INTEGER,
        FOREIGN KEY (jogador_id) REFERENCES jogador(id))"""
        cursor = self.cursor
        cursor.execute(sql)
    
    def criar_jogo(self):
        self.criar_tabela_jogador()
        self.criar_tabela_cartas_territorio()
        self.criar_tabela_exercito()


