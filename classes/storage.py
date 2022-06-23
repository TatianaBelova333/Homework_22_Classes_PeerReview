from abc import ABC, abstractmethod

from .exceptions import StorageFull, NotFound, NotEnough


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
            raise StorageFull
        self._items[title] = self._items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int) -> None:
        """Decrease quantity of items stored

        :raises NotFound: If no items with the specified title found in storage
        :raises NotEnough: If quantity requested exceeds quantity stored
        """
        if title not in self._items.keys():
            raise NotFound
        if quantity > self._items.get(title):
            raise NotEnough

        self._items[title] = self._items.get(title) - quantity
        if self._items[title] == 0:
            del self._items[title]

    def _get_free_space(self) -> int:
        """Get free space left in storage"""
        taken_space = sum([item for item in self._items.values()])
        return self._capacity - taken_space

    def _get_items(self) -> dict:
        """Return dictionary with stored items"""
        return self._items

    def _get_unique_items_count(self) -> int:
        """Return number of unique goods stored"""
        return len([item for item in self._items.keys()])

    def populate(self, goods: list) -> None:
        """Add items from list"""
        for item in goods:
            self.add(*item)

    def items_for_print(self) -> str:
        """Create message with stored items"""
        return '\n'.join([f'{value} {key}' for key, value in self._get_items().items()])
