from roman_numerals import get_modified_numerals, RomanNumeral

def test_V():
    v_list = [RomanNumeral(4, "IV"), RomanNumeral(6, "VI"), RomanNumeral(7, "VII"), RomanNumeral(8, "VIII")]
    assert get_modified_numerals(RomanNumeral(5, "V")) == v_list
