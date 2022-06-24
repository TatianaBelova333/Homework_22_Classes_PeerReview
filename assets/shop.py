from .storage import Storage
from .exceptions import StorageFull


class Shop(Storage):
    """Shop - any quantity of up to 5 titles could be stored within capacity"""

    def __init__(self):
        super().__init__()
        self._capacity: str = 20

    def add(self, title: str, quantity: int) -> None:
        """Increase quantity of items stored
=
        :raises StorageFull: if title in excess of 5 already stored is added
        """
        if self._get_unique_items_count() >= 5:
            raise StorageFull('В магазине нельзя хранить более 5 наименований товаров')
        super().add(title, quantity)
