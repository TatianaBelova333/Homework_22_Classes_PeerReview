from .storage import Storage


class Store(Storage):
    """Store - any quantity of any titles could be stored within capacity"""

    def __init__(self):
        super().__init__()
        self._capacity: str = 100
