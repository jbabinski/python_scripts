"""
* Assignment: Numpy Trigonometry
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Define function `trigonometry(angle_deg: int|float) -> dict`
    2. Return angle in radians and trigonometric function values (sin, cos, tg, ctg)
    3. Ctg for angle 180 and Tan for 90 degrees has infinite value, return `np.inf`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `trigonometry(angle_deg: int|float) -> dict`
    2. Zwróć kąt w radianach oraz wartości funkcji trygonometrycznych (sin, cos, tg, ctg)
    3. Ctg dla angle 180 oraz Tan dla 0 i 90 stopni ma wartość nieskończoną, zwróć `np.inf`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert trigonometry(0) is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert all(type(v) is not Ellipsis for v in trigonometry(0).values()), \
    'All values in the result must not be empty Ellipsis `...`'

    >>> trigonometry(180)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': 3.141592653589793,
     'sin': 1.2246467991473532e-16,
     'cos': -1.0,
     'tan': inf,
     'ctg': -8165619676597685.0}

    >>> trigonometry(90)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': 1.5707963267948966,
     'sin': 1.0,
     'cos': 6.123233995736766e-17,
     'tan': 1.633123935319537e+16, 'ctg': inf}

    >>> trigonometry(0)
    {'rad': 0.0, 'sin': 0.0, 'cos': 1.0, 'tan': 0.0, 'ctg': inf}

    >>> trigonometry(np.pi)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'rad': 0.05483...,
     'sin': 0.05480...,
     'cos': 0.99849...,
     'tan': 0.05488...,
     'ctg': 18.2195...}
"""

import numpy as np


def trigonometry(angle_deg):
    return {
        'rad': ...,
        'sin': ...,
        'cos': ...,
        'tan': ...,
        'ctg': ...,
    }
