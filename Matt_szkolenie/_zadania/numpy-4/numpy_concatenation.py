"""
* Assignment: Numpy Concatenation
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Given are one-dimensional: `a: np.ndarray`, `b: np.ndarray`
    2. Concatenate them as `result: np.ndarray`
    3. Reshape `result` into two rows and three columns
    4. Run doctests - all must succeed

Polish:
    1. Dane są jednowymiarowe: `a: np.ndarray`, `b: np.ndarray`
    2. Połącz je ze sobą jako `result: np.ndarray`
    3. Przekształć `result` w dwa wiersze na trzy kolumny
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([[1, 2, 3],
           [4, 5, 6]])
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# np.ndarray: Concatenate `a` and `b` and reshape as 2 by 3
result = ...
