import pytest as pytest

import tests.conftest
from classes.exceptions import ShopFull, StorageFull, NotFound, NotEnough


class TestShop:

    def test_create(self, shop):
        assert str(shop) == 'Это Storage типа Shop с емкостью 20', 'Ошибка при создании объекта shop'


class TestShopAdd:

    def test_add_okay(self, shop, goods_2):
        for item in goods_2:
            shop.add(*item)
        assert str(shop) == 'Это Storage типа Shop с емкостью 20', 'Ошибка при создании объекта shop'

    @pytest.mark.xfail()
    def test_add_titles_exceeded(self, shop, goods_6):
        for item in goods_6:
            shop.add(*item)
        raise ShopFull

    @pytest.mark.xfail()
    def test_add_capacity_exceeded(self, shop, goods_120):
        for item in goods_120:
            shop.add(*item)
        raise StorageFull


class TestShopAdd:

    def test_okay(self, shop, goods_2):
        for item in goods_2:
            shop.add(*item)

    @pytest.mark.xfail()
    def test_titles_exceeded(self, shop, goods_6):
        for item in goods_6:
            shop.add(*item)
        raise ShopFull

    @pytest.mark.xfail()
    def test_capacity_exceeded(self, shop, goods_120):
        for item in goods_120:
            shop.add(*item)
        raise StorageFull


class TestShopRemove():

    def test_okay(self, shop, goods_2):
        for item in goods_2:
            shop.add(*item)
        for item in goods_2:
            shop.remove(*item)

    @pytest.mark.xfail()
    def test_title_not_found(self, shop, goods_2, goods_6):
        for item in goods_2:
            shop.add(*item)
        for item in goods_6:
            shop.remove(*item)
        raise NotFound

    @pytest.mark.xfail()
    def test_quantity_exceeded(self, shop, goods_2, goods_2_remove):
        for item in goods_2:
            shop.add(*item)
        for item in goods_2_remove:
            shop.remove(*item)
        raise NotEnough


class TestShopGetItems():

    def test_dictionary(self, shop, goods_2, goods_2_dict):
        for item in goods_2:
            shop.add(*item)
        assert shop.get_items() == goods_2_dict

