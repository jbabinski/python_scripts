"""
* Assignment: Numpy Select Isin
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Set random seed to 0
    2. Generate `a: np.ndarray` of size 50x50
    3. `a` must contains random integers from 0 to 1024 inclusive
    4. Create `result: np.ndarray` with elements selected from `a` which are power of two
    5. Sort `result` in descending order
    6. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na 0
    2. Wygeneruj `a: np.ndarray` rozmiaru 50x50
    3. `a` musi zawierać losowe liczby całkowite z zakresu od 0 do 1024 włącznie
    4. Stwórz `result: np.ndarray` z elementami wybranymi z `a`, które są potęgami dwójki
    5. Posortuj `result` w kolejności malejącej
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.isin(a, b)`
    * `np.flip(a)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([1024, 1024, 1024, 1024, 1024, 1024,  512,  512,  512,  512,  256,
            256,  256,  256,  256,  128,  128,  128,  128,  128,   64,   32,
             32,   32,   32,   32,   16,   16,   16,   16,   16,   16,    8,
              8,    4,    2,    2,    2,    2,    2])
"""

import numpy as np
np.random.seed(0)


result = ...
