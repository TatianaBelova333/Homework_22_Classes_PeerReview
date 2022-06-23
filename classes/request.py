

class Request:
    """Process requests for item movement"""

    def __init__(self, storages: list, message: str):
        """
        :param message: message example 'Доставить 3 печеньки из склад в магазин'
        """

        self._list: list = storages
        self._message: str = message

        message_as_list = message.split(' ')

        self._from: str = message_as_list[4]
        self._to: str = message_as_list[6]
        self._amount: int = int(message_as_list[1])
        self._product: str = message_as_list[2]

    def __repr__(self):
        return f'from: {self._from}, to: {self._to}, amount: {self._amount}, product: {self._product}'
