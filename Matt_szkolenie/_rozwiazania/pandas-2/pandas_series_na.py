"""
* Assignment: Series NA
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. From input data create `pd.Series`
    2. Fill first missing value with zero
    3. Drop missing values
    4. Reindex series (without old copy)
    5. Run doctests - all must succeed

Polish:
    1. Z danych wejściowych stwórz `pd.Series`
    2. Wypełnij pierwszą brakującą wartość zerem
    3. Usuń brakujące wartości
    4. Zresetuj indeks (bez kopii starego)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    0    1.0
    1    0.0
    2    5.0
    3    1.0
    4    2.0
    5    1.0
    dtype: float64
"""
import pandas as pd

DATA = [1, None, 5, None, 1, 2, 1]

result = pd.Series(DATA)
result[1] = 0
result.dropna(inplace=True)
result.reset_index(drop=True, inplace=True)
