from constants import (
    get_numeral_for_power,
    get_numeral_for_thousands,
    UNITS,
    TENS,
    HUNDREDS,
)


def test_5():
    assert get_numeral_for_power(5, 0) == UNITS[5]


def test_3():
    assert get_numeral_for_power(3, 0) == UNITS[3]


def test_30():
    assert get_numeral_for_power(3, 1) == TENS[3]


def test_300():
    assert get_numeral_for_power(3, 2) == HUNDREDS[3]


def test_3000():
    assert get_numeral_for_thousands(3) == "MMM"
