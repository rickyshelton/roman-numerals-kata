from dataclasses import dataclass
from typing import Literal
import math

@dataclass
class RomanNumeral:
    value: int
    symbol: str

M = RomanNumeral(1000, "M")
D = RomanNumeral(500, "D")
C = RomanNumeral(100, "C")
L = RomanNumeral(50, "L")
X = RomanNumeral(10, "X")
V = RomanNumeral(5, "V")
I = RomanNumeral(1, "I")

def get_numerals_list():
    return [I, V, X, L, C, D, M]

def get_numeral_for_base(number: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], base: Literal[1, 10, 100]) -> RomanNumeral:

    index_for_base = int(math.log10(base)) * 2
    unit_numeral, mid_numeral, high_numeral = get_numerals_list()[index_for_base: index_for_base + 3]

    numeral_list = [RomanNumeral(0, "")]
    numeral_list.extend(get_first_three_numerals_for_base(unit_numeral))
    numeral_list.append(get_fourth_numeral_for_base(unit_numeral, mid_numeral))
    numeral_list.extend(get_fifth_to_eighth_numerals_for_base(unit_numeral, mid_numeral))
    numeral_list.append(get_ninth_numeral_for_base(unit_numeral, high_numeral))

    return numeral_list[number]

def get_numeral_for_base_1000(number):
    return RomanNumeral(number * 1000, number * M.symbol)


def get_first_three_numerals_for_base(unit_numeral: RomanNumeral) -> list[RomanNumeral]:
    first_three = []
    for i in [1, 2, 3]:
        first_three.append(RomanNumeral(i * unit_numeral.value, i * unit_numeral.symbol))
    return first_three


def get_fourth_numeral_for_base(unit_numeral: RomanNumeral, midpoint_numeral: RomanNumeral) -> RomanNumeral:
    value = midpoint_numeral.value - unit_numeral.value
    symbol = unit_numeral.symbol + midpoint_numeral.symbol

    return RomanNumeral(value, symbol)


def get_fifth_to_eighth_numerals_for_base(unit_numeral: RomanNumeral, midpoint_numeral: RomanNumeral) -> list[RomanNumeral]:
    fifth_to_eighth = []

    for i in [0, 1, 2, 3]:
        value = midpoint_numeral.value + (i * unit_numeral.value)
        symbol = midpoint_numeral.symbol + (i * unit_numeral.symbol)
        fifth_to_eighth.append(RomanNumeral(value, symbol))

    return fifth_to_eighth

def get_ninth_numeral_for_base(unit_numeral: RomanNumeral, highpoint_numeral: RomanNumeral) -> RomanNumeral:
    value = unit_numeral.value + highpoint_numeral.value
    symbol = unit_numeral.symbol + highpoint_numeral.symbol

    return RomanNumeral(value, symbol)
