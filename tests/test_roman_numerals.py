from roman_numerals import get_roman_numeral, RomanNumeral

def test_1():
    assert get_roman_numeral(1) == "I"

def test_2():
    assert get_roman_numeral(2) == "II"

def test_5():
    assert get_roman_numeral(5) == "V"

def test_10():
    assert get_roman_numeral(10) == "X"

def test_400():
    assert get_roman_numeral(400) == "CD"

def test_666():
    assert get_roman_numeral(666) == "DCLXVI"

def test_999():
    assert get_roman_numeral(999) == "CMXCIX"

def test_1000():
    assert get_roman_numeral(1000) == "M"

def test_2000():
    assert get_roman_numeral(2000) == "MM"

def test_8():
    assert get_roman_numeral(8) == "VIII"

def test_9():
    assert get_roman_numeral(9) == "IX"

def test_322():
    assert get_roman_numeral(322) == "CCCXXII"

def test_10000():
    assert get_roman_numeral(10000) == "MMMMMMMMMM"
