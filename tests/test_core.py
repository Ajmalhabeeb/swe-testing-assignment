import pytest
from quick_calc.core import evaluate, CalcError

def test_addition():
    assert evaluate("5+3") == 8.0

def test_subtraction():
    assert evaluate("10-4") == 6.0

def test_multiplication():
    assert evaluate("6*7") == 42.0

def test_division():
    assert evaluate("8/2") == 4.0

def test_division_by_zero_graceful():
    with pytest.raises(CalcError):
        evaluate("5/0")

def test_negative_numbers():
    assert evaluate("-5+2") == -3.0

def test_decimals():
    assert evaluate("0.1+0.2") == pytest.approx(0.3)

def test_very_large_numbers():
    assert evaluate("1000000000000000000*2") == 2000000000000000000.0