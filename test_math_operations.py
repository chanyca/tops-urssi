from math_operations import add, subtract, multiply
import pytest


@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (1.5, 2.5, 4)]
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(10, 5, 5), (-1, -1, 0), (0, 0, 0), (17.4, 3.2, 14.2)]
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(3, 5, 15), (-1, -1, 1), (0, 0, 0), (11, 0.1, 1.1)]
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
