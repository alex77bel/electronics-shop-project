from src.item import Item


class Phone(Item):
    """
    Класс для представления Phone.
    """

    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.
        :number_of_sim: Количество сим-карт
        остальные наследуются от Item
        """
        super().__init__(name, price, quantity)
        self.number_of_sim: int = number_of_sim

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @classmethod
    def _verify_number_of_sim(cls, data) -> None:  # метод для проверки атрибута number_of_sim
        msg = 'Количество физических SIM-карт должно быть целым числом больше нуля.'
        if not isinstance(data, int): raise TypeError(msg)
        if data < 1: raise ValueError(msg)

    @property  # геттер для атрибута number_of_sim
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter  # сеттер для атрибута number_of_sim
    def number_of_sim(self, data) -> None:
        self._verify_number_of_sim(data)
        self.__number_of_sim = data
