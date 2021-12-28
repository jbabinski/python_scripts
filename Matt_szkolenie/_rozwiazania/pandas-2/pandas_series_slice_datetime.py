"""
* Assignment: Series Slice Datetime
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Create `s: pd.Series` with 100 random numbers from standard distribution
    3. Series Index are following dates since 2000
    4. Define `result: pd.Series` with values for dates between 2000-02-14 and end of February 2000
    5. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz `s: pd.Series` z 100 losowymi liczbami z rozkładu normalnego
    3. Indeksem w serii mają być kolejne dni od 2000 roku
    4. Zdefiniuj `result: pd.Series` z wartościami pomiędzy datami od 2000-02-14 do końca lutego 2000
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.random.randn()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    2000-02-14   -0.509652
    2000-02-15   -0.438074
    2000-02-16   -1.252795
    2000-02-17    0.777490
    2000-02-18   -1.613898
                    ...
    2000-02-25    0.428332
    2000-02-26    0.066517
    2000-02-27    0.302472
    2000-02-28   -0.634322
    2000-02-29   -0.362741
    Freq: D, Length: 16, dtype: float64
"""

import pandas as pd
import numpy as np
np.random.seed(0)

NUMBER = 100

data = np.random.randn(100)
index = pd.date_range('2000-01-01', freq='D', periods=len(data))
s = pd.Series(data, index)


result = s['2000-02-14':'2000-02']
