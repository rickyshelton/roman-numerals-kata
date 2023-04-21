from constants import get_numeral_for_power, get_numeral_for_thousands


def get_roman_numeral(num: int) -> str:
    num_string = str(num)
    result = ""
    hundreds_digits_reversed = reversed(get_hundreds(num_string))

    for power, digit in enumerate(hundreds_digits_reversed):
        numeral = get_numeral_for_power(int(digit), power)
        result = numeral + result

    thousands = get_thousands(num_string)

    if thousands:
        numeral = get_numeral_for_thousands(int(thousands))
        result = numeral + result

    return result


def get_hundreds(num_string: str) -> str:
    return num_string[-3:]


def get_thousands(num_string: str) -> str:
    return num_string[0:-3]
