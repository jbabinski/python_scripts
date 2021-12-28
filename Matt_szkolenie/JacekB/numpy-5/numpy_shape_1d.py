"""
* Assignment: Numpy Shape 1d
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `result_ravel` with result of flattening `DATA` using `.ravel()` method
    2. Define `result_flatten` with result of flattening `DATA` using `.flatten()` method
    3. Define `result_reshape` with result of reshaping `DATA` into 1x9
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result_ravel` z wynikiem spłaszczenia `DATA` używając metody `.ravel()`
    2. Zdefiniuj `result_flatten` z wynikiem spłaszczenia `DATA` używając metody `.flatten()`
    3. Zdefiniuj `result_reshape` z wynikiem zmiany kształtu `DATA` na 1x9
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_ravel is not Ellipsis, \
    'Assign result to variable: `result_ravel`'
    >>> assert type(result_ravel) is np.ndarray, \
    'Variable `result_ravel` has invalid type, expected: np.ndarray'

    >>> assert result_flatten is not Ellipsis, \
    'Assign result to variable: `result_flatten`'
    >>> assert type(result_flatten) is np.ndarray, \
    'Variable `result_flatten` has invalid type, expected: np.ndarray'

    >>> assert result_reshape is not Ellipsis, \
    'Assign result to variable: `result_reshape`'
    >>> assert type(result_reshape) is np.ndarray, \
    'Variable `result_reshape` has invalid type, expected: np.ndarray'

    >>> result_flatten
    array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    >>> result_ravel
    array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    >>> result_reshape
    array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
"""

import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


result_ravel = ...
result_flatten = ...
result_reshape = ...
