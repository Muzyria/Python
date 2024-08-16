import pytest

@pytest.fixture
def check_condition(request):
    # Условие для пропуска теста
    if request.node.name == "test_to_skip":
        pytest.skip("Пропущено, потому что это test_to_skip")

    return "Тест не пропущен"




