from dataclasses import dataclass
from typing import Literal
import math


@dataclass
class RomanNumeral:
    value: int
    symbol: str


ZERO = RomanNumeral(0, "")
M = RomanNumeral(1000, "M")

UNITS = [
    ZERO,
    RomanNumeral(1, "I"),
    RomanNumeral(2, "II"),
    RomanNumeral(3, "III"),
    RomanNumeral(4, "IV"),
    RomanNumeral(5, "V"),
    RomanNumeral(6, "VI"),
    RomanNumeral(7, "VII"),
    RomanNumeral(8, "VIII"),
    RomanNumeral(9, "IX"),
]

TENS = [
    ZERO,
    RomanNumeral(10, "X"),
    RomanNumeral(20, "XX"),
    RomanNumeral(30, "XXX"),
    RomanNumeral(40, "XL"),
    RomanNumeral(50, "L"),
    RomanNumeral(60, "LX"),
    RomanNumeral(70, "LXX"),
    RomanNumeral(80, "LXXX"),
    RomanNumeral(90, "XC"),
]

HUNDREDS = [
    ZERO,
    RomanNumeral(100, "C"),
    RomanNumeral(200, "CC"),
    RomanNumeral(300, "CCC"),
    RomanNumeral(400, "CD"),
    RomanNumeral(500, "D"),
    RomanNumeral(600, "DC"),
    RomanNumeral(700, "DCC"),
    RomanNumeral(800, "DCCC"),
    RomanNumeral(900, "CM"),
]


def get_numeral_for_base(
    number: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], base: Literal[1, 10, 100]
) -> RomanNumeral:
    index_for_base = int(math.log10(base)) * 2

    return get_list_for_base(base)[number]


def get_list_for_base(base: Literal[1, 10, 100]) -> list[RomanNumeral]:
    if base == 1:
        return UNITS

    if base == 10:
        return TENS

    if base == 100:
        return HUNDREDS


def get_numeral_for_base_1000(number) -> RomanNumeral:
    return RomanNumeral(number * 1000, number * M.symbol)
