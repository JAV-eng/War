from .cartas_repository import CartasRepository
from .cartas_statagy import InsertStrategy,SelectStrategy
from .cartas_objetivos import Objetivos
from .cartas_territorio import CartasTerritorios

class CartasFactory:
    @staticmethod
    def create_objetivos(path):
        insert_strategy = InsertStrategy()
        select_strategy = SelectStrategy()
        repository = CartasRepository('objetivos', insert_strategy, select_strategy)
        return Objetivos(path, repository)

    @staticmethod
    def create_cartas_territorios(path):
        insert_strategy = InsertStrategy()
        select_strategy = SelectStrategy()
        repository = CartasRepository('cartas_territorio', insert_strategy, select_strategy)
        return CartasTerritorios(path, repository)
