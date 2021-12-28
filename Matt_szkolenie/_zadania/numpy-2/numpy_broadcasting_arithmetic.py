"""
* Assignment: Numpy Broadcasting Arithmetic
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define `a: np.ndarray` with square root of each element in `A`
    2. Define `b: np.ndarray` with square root of each element in `B`
    3. Define `c: np.ndarray` with second power (square) of each element in `C`
    4. Add elements from `a` to `b`
    5. Multiply the result by `c`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `a: np.ndarray` z pierwiastkiem kwadratowym każdego elementu `A`
    2. Zdefiniuj `b: np.ndarray` z pierwiastkiem kwadratowym każdego elementu `B`
    3. Zdefiniu `c: np.ndarray` z drugą potęgą (kwadratem) każdego z elementu w `C`
    4. Dodaj elementy z `a` do `b`
    5. Przemnóż wynik przez `c`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([[ 1.41421356,  2.73205081],
           [45.254834  ,  0.        ]])
"""

import numpy as np


A = np.array([[0, 1], [2, 3]], float)
B = np.array([2, 3], float)
C = np.array([[1, 1], [4, 0]], float)

# np.ndarray: Add elements from `a` to `b` and then multiply by `c`
result = ...
