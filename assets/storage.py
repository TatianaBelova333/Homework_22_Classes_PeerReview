from abc import ABC, abstractmethod

from .exceptions import StorageFull, ItemsNotFound


class Storage(ABC):
    """Abstract class"""

    @abstractmethod
    def __init__(self):
        self._items: dict[str: int] = {}
        self._capacity: str = 0

    def __repr__(self):
        return f'Это Storage типа {self.__class__.__name__} с емкостью {self._capacity}'

    def add(self, title: str, quantity: int) -> None:
        """Increase quantity of items stored

        :raises StorageFull: if not enough free space
        """
        if self._get_free_space() < quantity:
            raise StorageFull('Нет свободного места')
        self._items[title] = self._items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int) -> None:
        """Decrease quantity of items stored

        :raises ItemsNotFound: If no items with the specified title found in storage
        :raises ItemsNotFound: If quantity requested exceeds quantity stored
        """
        if title not in self._items.keys():
            raise ItemsNotFound(f'Товар с наименованием {title} не найден')
        if quantity > self._items.get(title):
            raise ItemsNotFound(f'Нет нужного количества товара с наименованием {title}')

        self._items[title] = self._items.get(title) - quantity
        if self._items[title] == 0:
            del self._items[title]

    def _get_free_space(self) -> int:
        """Get free space left in storage"""
        taken_space = sum([item for item in self._items.values()])
        return self._capacity - taken_space

    def get_items(self) -> dict:
        """Return dictionary with stored items"""
        return self._items

    def _get_unique_items_count(self) -> int:
        """Return number of unique goods stored"""
        return len([item for item in self._items.keys()])
