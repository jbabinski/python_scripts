"""
* Assignment: Slicing Slice Str
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Create `pd.Series` with 26 random integers in range `[10, 100)`
    2. Name indexes like letters from ASCII alphabet (`ASCII_LOWERCASE: str`)
    3. Find middle letter of alphabet
    4. Slice from series 3 elements up and down from middle
    5. Run doctests - all must succeed

Polish:
    1. Stwórz `pd.Series` z 26 losowymi liczbami całkowitymi z przedziału `<10; 100)`
    2. Nazwij indeksy jak kolejne litery alfabetu ASCII (`ASCII_LOWERCASE: str`)
    3. Znajdź środkową literę alfabetu
    4. Wytnij z serii po 3 elementy w górę i w dół od wyszukanego środka
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.random.randint(..., ..., size=...)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    j    97
    k    80
    l    98
    m    98
    n    22
    o    68
    p    75
    dtype: int64
"""

from statistics import median_low
import pandas as pd
import numpy as np
np.random.seed(0)


ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'

result = ...
