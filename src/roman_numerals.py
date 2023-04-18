from constants import get_numeral_for_base, get_numeral_for_base_1000, RomanNumeral

def get_roman_numeral(num):

    num_string = str(num)
    result = ""
    base = 1

    for i in reversed(get_hundreds(num_string)):
        result = get_numeral_for_base(int(i), base).symbol + result
        base = base * 10
    
    thousands = get_thousands(num_string)

    if thousands:
        result = get_numeral_for_base_1000(int(thousands)).symbol + result

    return result

def get_hundreds(num_string):
    return num_string[-3:]

def get_thousands(num_string):
    return num_string[0:-3]
