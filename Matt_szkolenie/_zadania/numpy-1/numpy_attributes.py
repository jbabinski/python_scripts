"""
* Assignment: Numpy Attributes
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Define `result: dict` with:
        a. number of dimensions;
        b. number of elements;
        c. data type;
        d. element size;
        e. shape;
        f. strides.
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict` z:
        a. liczbę wymiarów,
        b. liczbę elementów,
        c. typ danych,
        d. rozmiar elementu,
        e. kształt,
        f. przeskoki (strides).
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, expected: dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'number of dimensions': 2,
     'number of elements': 6,
     'data type': dtype('float64'),
     'element size': 8,
     'shape': (2, 3),
     'strides': (24, 8)}
"""

import numpy as np

DATA = np.array([[-1.1, 0.0, 1.1],
                 [2.2, 3.3, 4.4]])

result = {
    'number of dimensions': ...,
    'number of elements': ...,
    'data type': ...,
    'element size': ...,
    'shape': ...,
    'strides': ...,
}
