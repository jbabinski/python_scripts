"""
* Assignment: DataFrame Mapping Translate
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Set header and index to data from file
    3. Convert Polish month names to English
    4. Parse dates to `datetime` objects
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Ustaw nagłówek i index na dane zaczytane z pliku
    3. Przekonwertuj polskie nazwy miesięcy na angielskie
    4. Sparsuj daty do obiektów `datetime`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.Series.replace(regex=True)`
    * `pd.to_datetime()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
       id First Name   Last Name Mission Date
    0   1        Jan  Twardowski   1988-01-05
    1   2       Mark      Watney   1969-07-21
    2   3       Ivan   Ivanovich   1961-04-12
    3   4    Melissa       Lewis   1970-01-01
    4   5       Alex       Vogel   1968-12-25
"""

import pandas as pd


DATA = 'https://python.astrotech.io/_static/martian-pl.csv'
MONTHS_PLEN = {'styczeń': 'January',
               'luty': 'February',
               'marzec': 'March',
               'kwiecień': 'April',
               'maj': 'May',
               'czerwiec': 'June',
               'lipiec': 'July',
               'sierpień': 'August',
               'wrzesień': 'September',
               'październik': 'October',
               'listopad': 'November',
               'grudzień': 'December'}

df = pd.read_csv(DATA,)
df['Mission Date'] = df['Mission Date'].replace(MONTHS_PLEN, regex=True)
df['Mission Date'] = df['Mission Date'].apply(pd.to_datetime)
result = df
