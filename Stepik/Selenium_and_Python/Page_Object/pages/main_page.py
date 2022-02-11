from .base_page import BasePage


class MainPage(BasePage):
    # Заглушка
    # можно просто pass
    def __init__(self, *args, **kwargs):
        """Конструктор вызывает конструктор класса предка и передает ему все те аргументы,
         которые мы передали в конструктор MainPage
        :param args:
        :param kwargs:
        """
        super(MainPage, self).__init__(*args, **kwargs)
