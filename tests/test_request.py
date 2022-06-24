import pytest as pytest

import tests.conftest
from assets import Request


class TestRequest:

    def test_create(self, shop, store):
        request = Request([shop, store], 'Доставить 3 печеньки из склад в магазин')
        assert request._from == 'склад', "Error in 'from' field"
        assert request._to == 'магазин', "Error in 'from' field"
        assert request._amount == 3, "Error in 'from' field"
        assert request._product == 'печеньки', "Error in 'from' field"
