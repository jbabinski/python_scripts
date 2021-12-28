"""
* Assignment: Series Create Dates
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Gagarin flown to space on 1961-04-12
    2. Armstrong set foot on the Moon on 1969-07-21
    3. Create `result: pd.Series` with days between Gagarin's launch and Armstrong's first step
    4. How many days passed?
    5. Run doctests - all must succeed

Polish:
    1. Gagarin poleciał w kosmos w 1961-04-12
    2. Armstrong postawił stopę na Księżycu w 1969-07-21
    3. Stwórz `result: pd.Series` z dniami pomiędzy startem Gagarina a pierwszym krokiem Armstronga
    4. Jak wiele dni upłynęło?
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    0      1961-04-12
    1      1961-04-13
    2      1961-04-14
    3      1961-04-15
    4      1961-04-16
              ...
    3018   1969-07-17
    3019   1969-07-18
    3020   1969-07-19
    3021   1969-07-20
    3022   1969-07-21
    Length: 3023, dtype: datetime64[ns]
"""

import pandas as pd


data = pd.date_range(start='1961-04-12', end='1969-07-21')
result = pd.Series(data)
