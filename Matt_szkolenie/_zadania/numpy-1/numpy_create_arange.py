"""
* Assignment: Numpy Create Arange
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Create `result: np.ndarray` with even numbers from 0 to 100 (without 100)
    2. Numbers must be `float` type
    3. Run doctests - all must succeed

Polish:
    1. Stwórz `result: np.ndarray` z liczbami parzystymi od 0 do 100 (bez 100)
    2. Liczby muszą być typu `float`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24.,
           26., 28., 30., 32., 34., 36., 38., 40., 42., 44., 46., 48., 50.,
           52., 54., 56., 58., 60., 62., 64., 66., 68., 70., 72., 74., 76.,
           78., 80., 82., 84., 86., 88., 90., 92., 94., 96., 98.])
"""

import numpy as np


result = ...
