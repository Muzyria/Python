from debug_2 import Calculator

import pytest

@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 0.5),
        (2, 1, 1),
        (1, 0, "Zero")
    ]

)
def test_one(x, y, res):
    assert Calculator().divide(x, y) == res
