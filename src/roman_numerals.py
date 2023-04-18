from dataclasses import dataclass

@dataclass
class RomanNumeral:
    value: int
    symbol: str


numerals = [RomanNumeral(1000, "M"),
            RomanNumeral(500, "D"),
            RomanNumeral(100, "C"),
            RomanNumeral(50, "L"),
            RomanNumeral(10, "X"),
            RomanNumeral(5, "V"),
            RomanNumeral(1, "I")]


def get_additive_modified_numerals(roman_numeral: RomanNumeral) -> list[RomanNumeral]:
    modified_numerals = []

    if roman_numeral == numerals[0]:
        return modified_numerals
    
    if roman_numeral == numerals[6]:
        for i in [2, 3]:
            modified_numerals.append(RomanNumeral(i, i * roman_numeral.symbol))
        
        return modified_numerals
    
    modifier = get_numeral_modifier(roman_numeral)
    for i in [1, 2, 3]:
        value = roman_numeral.value + (i * modifier.value)
        symbol = roman_numeral.symbol + (i * modifier.symbol) if i >= 0 else modifier.symbol + roman_numeral.symbol
        modified_numerals.append(RomanNumeral(value, symbol))

    return modified_numerals

def get_subtractive_modified_numerals(roman_numeral: RomanNumeral) -> list[RomanNumeral]:
    modified_numerals = []
    modifier = get_numeral_modifier(roman_numeral)
    for i in [-1]:
        value = roman_numeral.value + (i * modifier.value)
        symbol = roman_numeral.symbol + (i * modifier.symbol) if i >= 0 else modifier.symbol + roman_numeral.symbol
        modified_numerals.append(RomanNumeral(value, symbol))

    return modified_numerals


def get_numeral_modifier(roman_numeral: RomanNumeral) -> RomanNumeral:
    index = numerals.index(roman_numeral)
    next_index = index + 1
    try:
        modifier_index = next_index if numerals[next_index].value != roman_numeral.value/2 else index + 2
        return numerals[modifier_index]
    except:
        return None


def get_roman_numeral(num):
    roman_numeral = ""
    numeral_index = 0
    while num > 0:
        modified_numerals = []
        current_numeral = numerals[numeral_index]

        modified_numerals.append(current_numeral)
        modified_numerals.extend(get_additive_modified_numerals(current_numeral))

        if numeral_index > 0:
            previous_numeral = numerals[numeral_index - 1]
            modified_numerals.extend(get_subtractive_modified_numerals(previous_numeral))

        for numeral in reversed(modified_numerals):

            if num >= numeral.value:
                roman_numeral += numeral.symbol
                num -= numeral.value
                break

        if num < current_numeral.value:
            numeral_index += 1

    return roman_numeral
