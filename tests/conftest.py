import pytest

from assets import Shop, Store


@pytest.fixture()
def shop():
    return Shop()


@pytest.fixture()
def store():
    return Store()


@pytest.fixture()
def goods_2():
    return [('зерно', 2), ('яблоки', 4)]


@pytest.fixture()
def goods_2_remove():
    return [('зерно', 2), ('яблоки', 6)]


@pytest.fixture()
def goods_2_dict():
    return {'зерно': 2, 'яблоки': 4}


@pytest.fixture()
def goods_6():
    return [('зерно', 2), ('яблоки', 4), ('хлеб', 1), ('молоко', 1), ('кефир', 1), ('бананы', 1)]


@pytest.fixture()
def goods_120():
    return [('зерно', 20), ('яблоки', 100)]
