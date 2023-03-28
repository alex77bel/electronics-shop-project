class InstantiateCSVError(Exception):
    """Класс исключения для обработки ошибок при создании экземпляра из csv файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка'

    def __str__(self):
        return self.message