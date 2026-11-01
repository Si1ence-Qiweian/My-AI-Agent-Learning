import pytest
from calculator import(
    add,
    subtract,
    multiply,
    divide
)

def test_add():
    assert add(-4, 0) == -4

def test_substract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide():
    assert divide(10, 2) == 5