"""
* Assignment: Numpy Iteration
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use `for` to iterate over `DATA`
    2. Define `result: list[int]` with even numbers from `DATA`
    3. Run doctests - all must succeed

Polish:
    1. Używając `for` iteruj po `DATA`
    2. Zdefiniuj `result: list[int]` z liczbami parzystymi z `DATA`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `number % 2 == 0`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, expected: list'
    >>> assert all(type(x) is np.int64 for x in result), \
    'All values in `result` must be type int'

    >>> result
    [2, 4, 6, 8]
"""

import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


result = ...
