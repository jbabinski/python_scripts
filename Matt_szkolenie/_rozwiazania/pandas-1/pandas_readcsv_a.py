"""
* Assignment: Pandas Read CSV Dates
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Read data from `DATA` to `result: pd.DataFrame`
    2. Parse dates in "Mission Date" column
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` do `result: pd.DataFrame`
    2. Sparsuj daty w kolumnie "Mission Date"
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `parse_dates`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> result
       id First Name   Last Name Mission Date
    0   1        Jan  Twardowski   1988-01-05
    1   2       Mark      Watney   1969-07-21
    2   3       Ivan   Ivanovich   1961-04-12
    3   4    Melissa       Lewis   1970-01-01
    4   5       Alex       Vogel   1968-12-25
"""

import pandas as pd


DATA = 'https://python.astrotech.io/_static/martian-en.csv'


# pd.DataFrame: read DATA and parse dates in "Mission Date" column
result = pd.read_csv(DATA, parse_dates=['Mission Date'])
