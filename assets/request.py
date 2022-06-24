from .exceptions import MessageError


class Request:
    """Process requests for item movement"""

    def __init__(self, storages: dict, message: str):
        """
        :param storages: dict with Store and Shop instances
        :param message: message example 'Доставить 3 печеньки из склад в магазин'
        """

        self._storages: dict = storages
        self._message: str = message
        self._create_fields_from_message()

    def _create_fields_from_message(self):
        """Check message and get fields from it

        :raises MessageError: if incorrect message passed
        """

        # Check length
        message = self._message.split(' ')
        if len(message) < 7:
            raise MessageError('Некорректное сообщение')

        # Check fields
        _amount, _product, _from, _to = message[1], message[2], message[4], message[6]

        if (
            _from not in ['склад', 'магазин']
            or _to not in ['склад', 'магазин']
            or not _amount.isdigit()
        ):
            raise MessageError('Вы ввели некорректное сообщение')

        # Create fields
        self._from: str = _from
        self._to: str = _to
        self._amount: int = int(_amount)
        self._product: str = _product

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def product(self):
        return self._product

    @property
    def amount(self):
        return self._amount

    def process(self):
        """Use Storage methods to manipulate data"""
        self._storages[self._from].remove(self._product, self._amount)
        self._storages[self._to].add(self._product, self._amount)
        return self._storages[self._from], self._storages[self._to]

    def __repr__(self):
        return f'from: {self._from}, to: {self._to}, amount: {self._amount}, product: {self._product}'
