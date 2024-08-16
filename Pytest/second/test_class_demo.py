import pytest



def test_to_skip(check_condition):
    # Этот тест будет пропущен
    assert check_condition == "Тест не пропущен"

def test_not_skipped(check_condition):
    # Этот тест будет выполнен
    assert check_condition == "Тест не пропущен"