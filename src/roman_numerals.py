from constants import get_numeral, RomanNumeral, M, I

def get_roman_numeral(num):

    num_string = str(num)
    result = ""

    for index, digit in reversed_string(num_string):
        result += get_numeral(digit, 10 * index).symbol

    return result

def reversed_string(a_string):
    return a_string[::-1]
