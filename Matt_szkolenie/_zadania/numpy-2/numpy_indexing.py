"""
* Assignment: Numpy Indexing
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Create `result: np.ndarray`
    2. Add to `result` elements from `DATA` at indexes:
        a. row 0, column 2
        b. row 2, column 2
        c. row 0, column 0
        d. row 1, column 0
    3. `result` size must be 2x2
    4. `result` type must be float
    5. Run doctests - all must succeed

Polish:
    1. Stwórz `result: np.ndarray`
    2. Dodaj do `result` elementy z `DATA` o indeksach:
        a. wiersz 0, kolumna 2
        b. wiersz 2, kolumna 2
        c. wiersz 0, kolumna 0
        d. wiersz 1, kolumna 0
    3. Rozmiar `result` musi być 2x2
    4. Typ `result` musi być float
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.zeros(shape, dtype)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([[3., 9.],
           [1., 4.]])
"""

import numpy as np


DATA = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = ...
