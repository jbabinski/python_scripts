"""
* Assignment: Series Create Randint
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Create `result: pd.Series` with 10 random digits (`int` from `0` to `9`)
    3. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz `result: pd.Series` z 10 losowymi cyframi  (`int` from `0` to `9`)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    0    5
    1    0
    2    3
    3    3
    4    7
    5    9
    6    3
    7    5
    8    2
    9    4
    dtype: int64
"""

import numpy as np
import pandas as pd
np.random.seed(0)


result = ...
