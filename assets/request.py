from .exceptions import MessageError


class Request:
    """Process requests for item movement"""

    def __init__(self, storages: dict, message: str):
        """
        :param storages: dict with Store and Shop instances
        :param message: message example 'Доставить 3 печеньки из склад в магазин'
        """
        self._storages = storages
        self._message = message

        split_message = Request._split_message(message)
        self._product: str = split_message['product']
        self._from: str = split_message['from']
        self._to: str = split_message['to']
        self._amount: int = int(split_message['amount'])

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str) -> None:
        Request._split_message(value)
        self._message = value

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

    @staticmethod
    def _split_message(message: str) -> dict:
        """Check message and get fields from it

        :raises MessageError: if incorrect message passed
        """
        # Check length
        message = message.split(' ')

        if len(message) < 7:
            raise MessageError('Некорректное сообщение')

        # Check fields
        split_message = {'from': message[4], 'to': message[6], 'amount': message[1], 'product': message[2]}
        if (
                split_message['from'] not in ['склад', 'магазин']
                or split_message['to'] not in ['склад', 'магазин']
                or not split_message['amount'].isdigit()
        ):
            raise MessageError('Вы ввели некорректное сообщение')

        return split_message

    def process(self) -> None:
        """Use Storage methods to manipulate data"""
        self._storages[self._from].remove(self._product, self._amount)
        self._storages[self._to].add(self._product, self._amount)
        return self._storages[self._from], self._storages[self._to]

    def __repr__(self):
        return f'from: {self._from}, to: {self._to}, amount: {self._amount}, product: {self._product}'
