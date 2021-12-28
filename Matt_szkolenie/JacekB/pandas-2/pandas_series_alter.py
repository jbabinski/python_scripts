"""
* Assignment: Series Alter
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. From input data create `s: pd.Series`
    2. Drop values at index 2, 4, 6
    3. Drop duplicates
    4. Reindex series (without old copy)
    5. Run doctests - all must succeed

Polish:
    1. Z danych wejściowych stwórz `s: pd.Series`
    2. Usuń wartości na indeksach 2, 4, 6
    3. Usuń duplikujące się wartości
    4. Zresetuj indeks (bez kopii starego)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    0    1.0
    1    NaN
    2    2.0
    dtype: float64
"""

import pandas as pd

DATA = [1, None, 5, None, 1, 2, 1]

result = (pd.Series(DATA)
          .drop([2, 4, 6])
          .drop_duplicates()
          .reset_index(drop=True)
          )
