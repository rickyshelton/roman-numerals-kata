from typing import Literal


SingleDigit = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PowersOfTen = Literal[0, 1, 2]

ZERO = ""
ONE_THOUSAND = "M"

UNITS = [
    ZERO,
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
]

TENS = [
    ZERO,
    "X",
    "XX",
    "XXX",
    "XL",
    "L",
    "LX",
    "LXX",
    "LXXX",
    "XC",
]

HUNDREDS = [
    ZERO,
    "C",
    "CC",
    "CCC",
    "CD",
    "D",
    "DC",
    "DCC",
    "DCCC",
    "CM",
]


def get_numeral_for_power_of_ten(number: SingleDigit, power: PowersOfTen) -> str:
    return get_list_for_power_of_ten(power)[number]


def get_list_for_power_of_ten(power: PowersOfTen) -> list[str]:
    if power == 0:
        return UNITS

    if power == 1:
        return TENS

    if power == 2:
        return HUNDREDS


def get_numeral_for_thousands(thousands: int) -> str:
    return thousands * ONE_THOUSAND
