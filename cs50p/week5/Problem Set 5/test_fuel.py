from fuel import convert , gauge
from pytest import raises

def test_fraction():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_percentage():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

    assert gauge(99) == "F"
    assert gauge(100) == "F"

    assert gauge(50) == "50%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"

def test_raises():
    with raises(ValueError):
        convert("4/3")

    with raises(ValueError):
        convert("-1/3")

    with raises(ValueError):
        convert("cat/dog")

    with raises(ZeroDivisionError):
        convert("1/0") 