import os

from dotenv import load_dotenv
from interval_sdk import Interval, IO
from roman_numerals import get_roman_numeral


load_dotenv()

interval = Interval(api_key=os.environ["INTERVAL_KEY"])


@interval.action
async def roman_numerals(io: IO):
    number = await io.input.number("Enter number")
    return get_roman_numeral(number)


interval.listen()
