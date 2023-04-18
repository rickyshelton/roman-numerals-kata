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
    #return [M, D, C, L, X, V, I]
    return [I, V, X, L, C, D, M]

def get_numeral_for_base(number: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], base: Literal[1, 10, 100, 1000]) -> RomanNumeral:
    if base == 1000:
        return RomanNumeral(number * base, number * M.symbol)
    
    index_for_base = int(math.log10(base)) * 2
    unit_numeral = get_numerals_list()[index_for_base]
    midpoint_numeral = get_numerals_list()[index_for_base + 1]
    highpoint_numeral = get_numerals_list()[index_for_base + 2]

    numeral_list = [RomanNumeral(0, "")]
    for i in [1, 2, 3]:
        numeral_list.append(RomanNumeral(i * unit_numeral.value, i * unit_numeral.symbol))
    
    numeral_list.append(RomanNumeral(midpoint_numeral.value - unit_numeral.value, unit_numeral.symbol + midpoint_numeral.symbol))

    for i in [0, 1, 2, 3]:
        numeral_list.append(RomanNumeral(midpoint_numeral.value + (i * unit_numeral.value), midpoint_numeral.symbol + (i * unit_numeral.symbol)))

    numeral_list.append(RomanNumeral(unit_numeral.value + highpoint_numeral.value, unit_numeral.symbol + highpoint_numeral.symbol))

    return numeral_list[number]
