from .storehouse import Storehouse
from .exceptions import StorageFull


class Shop(Storehouse):
    """Shop - any quantity of up to 5 items could be stored within capacity"""
    _item_limit = 5

    def __init__(self):
        super().__init__()
        self._capacity: int = 20

    @classmethod
    def _get_item_limit(cls):
        return cls._item_limit

    def add(self, item: str, quantity: int) -> None:
        """Increase quantity of items stored

        :raises StorageFull: if title in excess of 5 already stored is added
        """
        if self._get_unique_items_count() >= self._get_item_limit():  # было 5 - magic number
            raise StorageFull('В магазине нельзя хранить более 5 наименований товаров')
        return super().add(item, quantity)

    def remove(self, item: str, quantity: int) -> None:
        return super().remove(item, quantity)

    def _get_free_space(self) -> int:
        return super()._get_free_space()

    def get_items(self) -> dict:
        return super().get_items()

    def _get_unique_items_count(self) -> int:
        return super()._get_unique_items_count()





'''
class Shop(Storage):
    """Shop - any quantity of up to 5 titles could be stored within capacity"""
    title_limit = 5

    def __init__(self):
        super().__init__()
        self._capacity: str = 20

    @classmethod
    def _get_title_limit(cls):
        return cls.title_limit

    def add(self, title: str, quantity: int) -> None:
        """Increase quantity of items stored

        :raises StorageFull: if title in excess of 5 already stored is added
        """
        if self._get_unique_items_count() >= self._get_title_limit(): 
            raise StorageFull('В магазине нельзя хранить более 5 наименований товаров')
        super().add(title, quantity)
'''