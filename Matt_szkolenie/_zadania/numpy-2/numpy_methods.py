"""
* Assignment: Numpy Methods
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Reshape `result` to 3x4
    2. Fill last column with zeros (0)
    3. Transpose `result`
    4. Convert `result` to float
    5. Fill first row with `np.nan`
    6. Run doctests - all must succeed

Polish:
    1. Zmień kształt na 3x4
    2. Wypełnij ostatnią kolumnę zerami (0)
    3. Transponuj `result`
    4. Przekonwertuj `result` do float
    5. Wypełnij pierwszy wiersz `np.nan`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([[nan, nan, nan],
           [47.,  9., 87.],
           [64., 83., 70.],
           [ 0.,  0.,  0.]])
"""

import numpy as np

DATA = np.array([[44, 47, 64, 67],
                 [67,  9, 83, 21],
                 [36, 87, 70, 88]])


result = ...
