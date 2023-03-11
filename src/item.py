from csv import DictReader
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name  # обращается к сеттеру
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def _verify_name(cls, name: str):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')

    @property  # геттер
    def name(self):
        return self.__name  # возвращаем __name

    @name.setter  # сеттер
    def name(self, name: str):
        self._verify_name(name)  # проверяем __name
        self.__name = name  # присваиваем __name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Создает экземпляры Item, инициализирует данными из src/items.csv
        """
        for item in cls._csv_reader(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\\src\\items.csv'))):
            Item(item['name'], float(item['price']), cls.string_to_number(item['quantity']))

    @staticmethod
    def _csv_reader(filename: str) -> list[dict]:
        """
        Получает данные из файла filename, возвращает список
        """
        with open(filename) as csvfile:
            return [*DictReader(csvfile)]

    @staticmethod
    def string_to_number(string: str) -> int | str:
        """
        Преобразует строку в int
        """
        try:
            return int(float(string))
        except (ValueError, TypeError) as error:
            raise Exception(error)
