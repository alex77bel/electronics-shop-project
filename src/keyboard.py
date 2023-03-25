from src.item import Item


class Layout:

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        self.__language = 'EN' if self.__language == 'RU' else 'RU'
        return self


class Keyboard(Layout, Item):
    pass
