from constants import get_numeral_for_base, V, RomanNumeral

def test_base_1_5():
    assert get_numeral_for_base(5, 1) == V

def test_base_1_3():
    assert get_numeral_for_base(3, 1) == RomanNumeral(3, "III")

def test_base_10_3():
    assert get_numeral_for_base(3, 10) == RomanNumeral(30, "XXX")

def test_base_100_3():
    assert get_numeral_for_base(3, 100) == RomanNumeral(300, "CCC")

def test_base_1000_3():
    assert get_numeral_for_base(3, 1000) == RomanNumeral(3000, "MMM")
