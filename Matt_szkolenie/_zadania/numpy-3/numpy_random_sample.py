"""
* Assignment: Numpy Random Sample
* Complexity: medium
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Print 6 random integers without repetition in range from 1 to 49
    3. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Wyświetl 6 losowych i nie powtarzających się liczb całkowitych z zakresu od 1 do 49.
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([30,  5, 27, 31, 33, 38])
"""

import numpy as np
np.random.seed(0)

result = ...
