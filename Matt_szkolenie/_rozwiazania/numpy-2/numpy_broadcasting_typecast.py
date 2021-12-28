"""
* Assignment: Numpy Broadcasting Type Cast
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. For given: `a: np.ndarray`, `b: np.ndarray` (see below)
    2. Add `a` and `b`
    3. Add `b` and `a`
    4. What happened?
    5. Run doctests - all must succeed

Polish:
    1. Dla danych: `a: np.ndarray`, `b: np.ndarray` (patrz sekcja input)
    2. Dodaj `a` i `b`
    3. Dodaj `b` i `a`
    4. Co się stało?
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result_ab) is np.ndarray, \
    'Variable `result_ab` has invalid type, expected: np.ndarray'
    >>> assert type(result_ba) is np.ndarray, \
    'Variable `result_ba` has invalid type, expected: np.ndarray'

    >>> result_ab
    array([[5, 1],
           [2, 3]])

    >>> result_ba
    array([[5, 1],
           [2, 3]])
"""

import numpy as np


a = np.array([[1, 0], [0, 1]])
b = [[4, 1], [2, 2]]


result_ab = a + b
result_ba = b + a
