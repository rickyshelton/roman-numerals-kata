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


def get_modified_numerals(roman_numeral: RomanNumeral) -> list[RomanNumeral]:
    # return additive numerals
    # return sub
    return [RomanNumeral(4, "IV"), RomanNumeral(6, "VI"), RomanNumeral(7, "VII"), RomanNumeral(8, "VIII")]


def get_roman_numeral(num):
    roman_numeral = ""
    numeral_marker = 0
    while num > 0:
        current_numeral_value = numerals[numeral_marker].value
        current_numeral_symbol = numerals[numeral_marker].symbol

        if num >= current_numeral_value:
            roman_numeral += current_numeral_symbol
            num -= current_numeral_value
        else:
            numeral_marker += 1

    return roman_numeral
