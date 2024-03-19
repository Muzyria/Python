from main import Calculator
import pytest


class TestCalculator:

    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 0.5),
            (2, 1, 2)
        ]
    )
    def test_divide(self, x, y, res):
        assert Calculator().divide(x, y) == res


    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 3),
            (2, 1, 3)
        ]
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res
