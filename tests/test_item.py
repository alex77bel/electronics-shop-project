from src.item import Item
from pytest import fixture, raises


@fixture
def item1():  # Экземпляр товара
    return Item('Телефон', 10000, 5)


def test_init(item1):  # проверка правильности создания полей экземпляра
    assert item1.name == 'Телефон'
    assert item1.price == 10000
    assert item1.quantity == 5
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'
    assert len(Item.all) == 1
    with raises(Exception):
        item1.name = 'СуперСмартфон'


def test_instantiate_from_csv():  # проверка создания экземпляров из items.csv
    Item.all.clear()
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():  # проверка преобразования строки в int
    assert Item.string_to_number('5.5') == 5
    with raises(Exception):
        Item.string_to_number('пять')


def test_calculate_total_price(item1):  # проверка метода подсчета общей стоимости товара
    assert item1.calculate_total_price() == item1.price * item1.quantity


def test_apply_discount(item1):  # проверка метода применения скидки
    old_price = item1.price  # цена до скидки
    item1.apply_discount()  # применяем скидку
    assert item1.price == old_price * item1.pay_rate  # проверяем, как сработало


def test_str_repr(item1):
    assert repr(item1) == "Item('Телефон', 10000, 5)"
    assert str(item1) == 'Телефон'
