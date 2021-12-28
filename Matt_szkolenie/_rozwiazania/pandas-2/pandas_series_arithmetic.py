"""
* Assignment: Series Arithmetic
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Set random seed to zero
    2. Generate `data: ndarray` with 5 random digits [0, 9]
    3. Create `index: list` with index names as sequential letters in english alphabet
    4. Create `s: pd.Series` from `data` and `index`
    5. Multiply `s` by 10
    6. Multiply `s` by `s`
    7. Run doctests - all must succeed

Polish:
    1. Ustaw random ziarno losowości na zero
    2. Wygeneruj `data: np.ndarray` z 5 losowymi cyframi <0, 9>
    3. Stwórz `index: list` z indeksami jak kolejne listery alfabetu angielskiego
    4. Stwórz `s: pd.Series` z `data` oraz `index`
    5. Pomnóż `s` przez 10
    6. Pomnóż `s` przez  wartości `s`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    a    2500
    b       0
    c     900
    d     900
    e    4900
    dtype: int64
"""
import string

import pandas as pd
import numpy as np
np.random.seed(0)


data = np.random.randint(0,10, size=5)
index = list(string.ascii_lowercase[:5])
s = pd.Series(data, index)

s *= 10
s *= s

result = s
