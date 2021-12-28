"""
* Assignment: Series Sample
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Set random seed to zero
    2. Create `pd.Series` with 100 random numbers from standard normal distribution
    3. Series Index are following dates since 2000
    4. Print values:
        a. first in the series,
        b. last 5 elements in the series,
        c. first two weeks in the series,
        d. last month in the series,
        e. three random elements,
        f. 125% of random elements with replacement.
    5. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz `pd.Series` z 100 losowymi liczbami z rozkładu normalnego
    3. Indeksem w serii mają być kolejne dni od 2000 roku
    4. Wypisz wartości:
        a. pierwszy w serii,
        b. ostatnie 5 elementów w serii,
        c. dwa pierwsze tygodnie w serii,
        d. ostatni miesiąc w serii,
        e. trzy losowe element,
        f. 125% losowych elementów z powtórzeniami.
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.random.seed(0)`
    * `np.random.randn(n)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is dict
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'head': 2000-01-01    1.764052
    Freq: D, dtype: float64, 'tail': 2000-04-05    0.706573
    2000-04-06    0.010500
    2000-04-07    1.785870
    2000-04-08    0.126912
    2000-04-09    0.401989
    Freq: D, dtype: float64, 'first': 2000-01-01    1.764052
    2000-01-02    0.400157
    2000-01-03    0.978738
    2000-01-04    2.240893
    2000-01-05    1.867558
    2000-01-06   -0.977278
    2000-01-07    0.950088
    2000-01-08   -0.151357
    2000-01-09   -0.103219
    Freq: D, dtype: float64, 'last': 2000-04-01    1.222445
    2000-04-02    0.208275
    2000-04-03    0.976639
    2000-04-04    0.356366
    2000-04-05    0.706573
    2000-04-06    0.010500
    2000-04-07    1.785870
    2000-04-08    0.126912
    2000-04-09    0.401989
    Freq: D, dtype: float64, 'sample_n': 2000-01-20   -0.854096
    2000-01-07    0.950088
    2000-02-15   -0.438074
    dtype: float64, 'sample_frac': 2000-03-07   -1.630198
    2000-04-01    1.222445
    2000-03-26    1.895889
    2000-02-09   -0.302303
    2000-02-09   -0.302303
                    ...
    2000-01-08   -0.151357
    2000-03-21   -1.165150
    2000-01-23    0.864436
    2000-03-20    0.056165
    2000-03-30    1.054452
    Length: 125, dtype: float64}
"""

import pandas as pd
import numpy as np
np.random.seed(0)

data = np.random.randn(100)
index = pd.date_range('2000-01-01', freq='D', periods=len(data))
s = pd.Series(data, index)

result = {
    'head': s.head(n=1),
    'tail': s.tail(n=5),
    'first': s.first('2W'),
    'last': s.last('M'),
    'sample_n': s.sample(n=3),
    'sample_frac': s.sample(frac=1.25, replace=True),
}
