from roman_numerals import get_roman_numeral, RomanNumeral

def test_1():
    assert get_roman_numeral(1) == "I"

def test_2():
    assert get_roman_numeral(2) == "II"

def test_5():
    assert get_roman_numeral(5) == "V"

def test_10():
    assert get_roman_numeral(10) == "X"

def test_1000():
    assert get_roman_numeral(1000) == "M"

def test_9():
    assert get_roman_numeral(9) == "IX"
