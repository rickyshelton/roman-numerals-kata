from roman_numerals import get_additive_modified_numerals, get_subtractive_modified_numerals, RomanNumeral

def test_V_additive():
    v_list = [RomanNumeral(6, "VI"), RomanNumeral(7, "VII"), RomanNumeral(8, "VIII")]
    assert get_additive_modified_numerals(RomanNumeral(5, "V")) == v_list

def test_V_subtractive():
    v_list = [RomanNumeral(4, "IV")]
    assert get_subtractive_modified_numerals(RomanNumeral(5, "V")) == v_list

def test_M_additive():
    assert get_additive_modified_numerals(RomanNumeral(1000, "M")) == []
