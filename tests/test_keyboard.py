from src.keyboard import Keyboard
from pytest import fixture, raises


@fixture
def Keyboard1():  # Экземпляр товара
    return Keyboard('KD87A', 9600, 5)


def test_init(Keyboard1):  # проверка правильности создания полей экземпляра
    assert Keyboard1.name == 'KD87A'
    assert Keyboard1.price == 9600
    assert Keyboard1.quantity == 5
    assert str(Keyboard1.language) == "EN"


def test_change_lang(Keyboard1):
    Keyboard1.change_lang()
    assert str(Keyboard1.language) == "RU"
    Keyboard1.change_lang().change_lang()
    assert str(Keyboard1.language) == "RU"
    with raises(Exception):
        Keyboard1.language = 'CH'

