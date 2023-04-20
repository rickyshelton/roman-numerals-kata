from constants import get_numeral_for_power, get_numeral_for_thousands, RomanNumeral


def get_roman_numeral(num):
    num_string = str(num)
    result = ""
    base = 1

    for digit in reversed(get_hundreds(num_string)):
        numeral = get_numeral_for_power(int(digit), base)
        result = numeral.symbol + result
        base = base * 10

    thousands = get_thousands(num_string)

    if thousands:
        result = get_numeral_for_thousands(int(thousands)).symbol + result

    return result


def get_hundreds(num_string):
    return num_string[-3:]


def get_thousands(num_string):
    return num_string[0:-3]
