from abc import ABC, abstractmethod

class TabuleiroInterface(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()