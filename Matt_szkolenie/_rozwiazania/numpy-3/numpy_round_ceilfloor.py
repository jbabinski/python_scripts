"""
* Assignment: Numpy Round Floor and Ceil
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Ceil round `data` values and assign to `result_ceil`
    2. Floor round `data` values and assign to `result_floor`
    3. Round `data` values and assign to `result_round`
    4. Run doctests - all must succeed

Polish:
    1. Zaokrąglij wartości `data` w górę (ceil) i przypisz do `result_ceil`
    2. Zaokrąglij wartości `data` w dół (floor) i przypisz do `result_floor`
    3. Zaokrąglij wartości `data` i przypisz do `result_round`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_ceil is not Ellipsis, \
    'Assign result to variable: `result_ceil`'
    >>> assert type(result_ceil) is np.ndarray, \
    'Variable `result_ceil` has invalid type, expected: np.ndarray'

    >>> assert result_floor is not Ellipsis, \
    'Assign result to variable: `result_floor`'
    >>> assert type(result_floor) is np.ndarray, \
    'Variable `result_floor` has invalid type, expected: np.ndarray'

    >>> assert result_round is not Ellipsis, \
    'Assign result to variable: `result_round`'
    >>> assert type(result_round) is np.ndarray, \
    'Variable `result_round` has invalid type, expected: np.ndarray'

    >>> result_ceil
    array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
           1., 1., 1., 1.])

    >>> result_floor
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0.])

    >>> result_round
    array([1., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 0., 0., 0.,
           1., 1., 1., 1.])
"""

import numpy as np
np.random.seed(0)


DATA = np.array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
                 0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152,
                 0.79172504, 0.52889492, 0.56804456, 0.92559664, 0.07103606,
                 0.0871293 , 0.0202184 , 0.83261985, 0.77815675, 0.87001215,
                 0.97861834])

result_ceil = ...
result_floor = ...
result_round = ...
