"""
* Assignment: Numpy Random Float
* Complexity: medium
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Define `result: np.ndarray` of 10 random floats
    3. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Zdefiniuj `result: np.ndarray` z 10 losowymi liczbami zmiennoprzecinkowymi
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> result
    array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
           0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152])
"""

import numpy as np
np.random.seed(0)


result = ...
