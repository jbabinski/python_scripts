"""
* Assignment: Series Getitem
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Set random seed to zero
    2. Create `pd.Series` with 100 random numbers from standard normal distribution
    3. Series Index are following dates since 2000
    4. Define `result: dict` with values:
        a. at 2000-02-29,
        b. first value in the series (without using `.head()`),
        c. last value in the series (without using `.tail()`),
        d. middle value in the series.
    5. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz `pd.Series` z 100 losowymi liczbami z rozkładu normalnego
    3. Indeksem w serii mają być kolejne dni od 2000 roku
    4. Zdefiniuj `result: dict` ` wartościami:
        a. dnia 2000-02-29,
        b. pierwszą wartość w serii (nie używając `.head()`),
        c. ostatnią wartość w serii (nie używając `.tail()`),
        d. środkowa wartość serii.
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.random.seed(0)`
    * `np.random.randn(10)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Result must be a dict'



    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'2000-02-29': -0.3627411659871381,
     'first': 1.764052345967664,
     'last': 0.40198936344470165,
     'middle': -0.8954665611936756}
"""

import pandas as pd
import numpy as np
np.random.seed(0)


data = np.random.randn(100)
index = pd.date_range('2000-01-01', freq='D', periods=len(data))
s = pd.Series(data, index)

middle = int(s.size / 2)

result = {
    '2000-02-29': s['2000-02-29'],
    'first': s[0],
    'last': s[-1],
    'middle': s[middle],
}
