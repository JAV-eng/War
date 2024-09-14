from abc import ABC, abstractmethod

class TerritorioInterface(ABC):
    
    @abstractmethod
    def __init__(self,nome,vizinhos) -> None:
        super().__init__()