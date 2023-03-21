from src.phone import Phone
from src.item import Item

from pytest import fixture, raises


@fixture
def item1():  # Экземпляр товара
    return Item('Смартфон', 10000, 10)


@fixture
def phone1():  # Экземпляр телефона
    return Phone('iPhone 14', 120000, 5, 2)


def test_init(phone1):  # проверка правильности создания полей экземпляра
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_add(item1, phone1):
    assert item1 + phone1 == 15
    assert phone1 + phone1 == 10
    with raises(Exception):
        phone1 + 3

def test_str_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(phone1) == 'iPhone 14'




