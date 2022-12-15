import pytest


@pytest.fixture()
def set_up():
    print('Вход в систему')
    yield
    print('Выход из системы')
