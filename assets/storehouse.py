from .exceptions import StorageFull, ItemsNotFound
from .storage import Storage


class Storehouse(Storage):
    """Storehouse - any quantity of any items could be stored within capacity"""

    def __init__(self):
        super().__init__()
        self._capacity: int = 100

    def add(self, item: str, quantity: int) -> None:
        """Increase quantity of items stored
          :raises StorageFull: if not enough free space
        """
        if self._get_free_space() < quantity:
            raise StorageFull('Нет свободного места')
        self._items[item] = self._items.get(item, 0) + quantity

    def remove(self, item: str, quantity: int) -> None:
        """Decrease quantity of items stored
        :raises ItemsNotFound: If no items with the specified title found in storage
                :raises ItemsNotFound: If quantity requested exceeds quantity stored
                """
        # было if title not in self._items.keys()
        if item not in self._items:
            raise ItemsNotFound(f'Товар с наименованием {item} не найден')
        if quantity > self._items.get(item):
            raise ItemsNotFound(f'Нет нужного количества товара с наименованием {item}')

        # было - self._items[title] = self._items.get(title) - quantity
        self._items[item] -= quantity
        if self._items[item] == 0:
            del self._items[item]

    def _get_free_space(self) -> int:
        """Get free space left in storage"""
        #  было: taken_space = sum([item for item in self._items.values()])
        taken_space = sum(self._items.values())
        return self._capacity - taken_space

    def get_items(self) -> dict:
        """Return dictionary with stored items"""
        return self._items

    def _get_unique_items_count(self) -> int:
        """Return number of unique goods stored"""
        # было:  return len([item for item in self._items.keys()])
        return len(self._items)
