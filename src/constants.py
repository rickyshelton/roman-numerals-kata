from dataclasses import dataclass
from typing import Literal


@dataclass
class RomanNumeral:
    value: int
    symbol: str


SingleDigit = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PowersOfTen = Literal[0, 1, 2]

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


def get_numeral_for_power(number: SingleDigit, power: PowersOfTen) -> RomanNumeral:
    return get_list_for_power(power)[number]


def get_list_for_power(power: PowersOfTen) -> list[RomanNumeral]:
    if power == 0:
        return UNITS

    if power == 1:
        return TENS

    if power == 2:
        return HUNDREDS


def get_numeral_for_thousands(thousands: int) -> RomanNumeral:
    return RomanNumeral(thousands * 1000, thousands * M.symbol)
