"""
* Assignment: Numpy Round Clip
* Complexity: medium
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Create `result: np.ndarray` copy of `DATA`
    2. Clip numbers only in first column to 50 (inclusive) to 80 (exclusive)
    3. Print `result`
    4. Run doctests - all must succeed

Polish:
    1. Stwórz `result: np.ndarray` z kopią danych z `DATA`
    2. Przytnij liczby w pierwszej kolumnie od 50 (włącznie) do 80 (rozłącznie)
    3. Wypisz `result`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `result[:, 0]`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([[50, 47, 64],
           [67, 67,  9],
           [80, 21, 36],
           [80, 70, 88],
           [80, 12, 58],
           [65, 39, 87],
           [50, 88, 81]])
"""

import numpy as np


DATA = np.array([[44, 47, 64],
                 [67, 67,  9],
                 [83, 21, 36],
                 [87, 70, 88],
                 [88, 12, 58],
                 [65, 39, 87],
                 [46, 88, 81]])

result = ...
