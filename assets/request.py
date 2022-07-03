from typing import Tuple, Any
import re
from .exceptions import UserRequestError


class Request:
    """Process requests for item movement"""
    sample_request = 'Доставить 3 печеньки из склад в магазин'
    request_pattern = r'Доставить \d{1,} [а-яё]{1,} из (?:склад|магазин) в (?:склад|магазин)'

    def __init__(self, storages: dict, user_request: str):
        """
        :param storages: dict with Store and Shop instances
        :param message: message example 'Доставить 3 печеньки из склад в магазин'
        """
        self._storages = storages
        self._user_request = user_request.capitalize()
        try:
            self.product: str = self._split_request(self._user_request)['product']
            self.from_: str = self._split_request(self._user_request)['from']
            self.to: str = self._split_request(self._user_request)['to']
            self.amount: int = int(self._split_request(self._user_request)['amount'])
        except UserRequestError:
            print("Запрос не может быть создан")

    def _split_request(self, user_request: str) -> dict:
        """Splits user's request"""
        self._validate_request(user_request)
        user_request = user_request.split()
        split_request = {'from': user_request[4], 'to': user_request[6], 'amount': user_request[1], 'product': user_request[2]}
        return split_request

    def _validate_request(self, user_request: str):
        """raises MessageError: if incorrect message passed"""

        if not re.fullmatch(Request.request_pattern, user_request):
            raise UserRequestError('Вы ввели некорректное сообщение')

    def process(self) -> Tuple[Any, Any]:
        """Use Storage methods to manipulate data"""
        self._validate_request(self._user_request)
        self._storages[self.from_].remove(self.product, self.amount)
        self._storages[self.to].add(self.product, self.amount)
        return self._storages[self.from_], self._storages[self.to]

    def __repr__(self):
        try:
            self._validate_request(self._user_request)
            return f'from: {self.from_}, to: {self.to}, amount: {self.amount}, product: {self.product}'
        except UserRequestError:
            return 'Некорректный запрос'