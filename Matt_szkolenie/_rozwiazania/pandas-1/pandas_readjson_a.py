"""
* Assignment: Pandas Read JSON
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z DATA jako result: pd.DataFrame
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> result.loc[[0,10,20]]
        sepalLength  sepalWidth  petalLength  petalWidth     species
    0           5.1         3.5          1.4         0.2      setosa
    10          7.0         3.2          4.7         1.4  versicolor
    20          6.3         3.3          6.0         2.5   virginica
"""

import pandas as pd

DATA = 'https://python.astrotech.io/_static/iris.json'


# pd.DataFrame: read DATA from JSON
result = pd.read_json(DATA)
