from constants import (
    get_numeral_for_power,
    get_numeral_for_thousands,
    UNITS,
    TENS,
    HUNDREDS,
    RomanNumeral,
)


def test_base_1_5():
    assert get_numeral_for_power(5, 1) == UNITS[5]


def test_base_1_3():
    assert get_numeral_for_power(3, 1) == UNITS[3]


def test_base_10_3():
    assert get_numeral_for_power(3, 10) == TENS[3]


def test_base_100_3():
    assert get_numeral_for_power(3, 100) == HUNDREDS[3]


def test_base_1000_3():
    assert get_numeral_for_thousands(3) == RomanNumeral(3000, "MMM")
