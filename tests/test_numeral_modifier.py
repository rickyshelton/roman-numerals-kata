from roman_numerals import get_numeral_modifier, RomanNumeral

def test_I():
    assert get_numeral_modifier(RomanNumeral(1, "I")) is None

def test_V():
    assert get_numeral_modifier(RomanNumeral(5, "V")) == RomanNumeral(1, "I")

def test_X():
    assert get_numeral_modifier(RomanNumeral(10, "X")) == RomanNumeral(1, "I")

def test_M():
    assert get_numeral_modifier(RomanNumeral(1000, "M")) == RomanNumeral(100, "C")
