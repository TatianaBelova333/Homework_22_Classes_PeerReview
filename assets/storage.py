from abc import ABC, abstractmethod


class Storage(ABC):
    """Abstract class"""

    @abstractmethod
    def __init__(self):
        self._items: dict[str: int] = {}
        self._capacity: int = 0

    def __repr__(self):
        return f'Это Storage типа {self.__class__.__name__} с емкостью {self._capacity}'

    @abstractmethod
    def add(self, item: str, quantity: int) -> None:
        pass

    @abstractmethod
    def remove(self, item: str, quantity: int) -> None:
        pass

    @abstractmethod
    def _get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict:
        pass

    @abstractmethod
    def _get_unique_items_count(self) -> int:
        pass