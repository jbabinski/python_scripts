"""

* Assignment: Numpy Algebra Euclidean Ndim
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Given are two points `a: Sequence[int]` and `b: Sequence[int]`
    2. Coordinates are in cartesian system
    3. Points `a` and `b` are in n-dimensional space
    4. Points `a` and `b` must be in the same space
    5. Calculate distance between points using Euclidean algorithm
    6. Run doctests - all must succeed

Polish:
    1. Dane są dwa punkty `a: Sequence[int]` i `b: Sequence[int]`
    2. Koordynaty są w systemie kartezjańskim
    3. Punkty `a` i `b` są w n-wymiarowej przestrzeni
    4. Punkty `b` i `b` muszą być w tej samej przestrzeni
    5. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for n1,n2 in zip(a,b)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert euclidean_distance((0,0), (0,0)) is not Ellipsis, \
    'Assign result to function: `euclidean_distance`'

    >>> euclidean_distance((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
    ValueError: Points must be in the same dimensions

    >>> euclidean_distance((0,0,0), (0,0,0))
    0.0

    >>> euclidean_distance((0,0,0), (1,1,1))
    1.7320508075688772

    >>> euclidean_distance((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> euclidean_distance((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772
"""

from math import sqrt


# callable: Calculate distance between points using Euclidean algorithm
def euclidean_distance(a, b):
    pass
