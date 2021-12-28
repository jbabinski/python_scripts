"""
* Assignment: Numpy Broadcasting Matmul
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. For given: `a: np.ndarray`, `b: np.ndarray` (see below)
    2. Multiply `a` and `b` using scalar multiplication
    3. Multiply `a` and `b` using matrix multiplication
    4. Multiply `b` and `a` using scalar multiplication
    5. Multiply `b` and `a` using matrix multiplication
    6. Discuss results
    7. Run doctests - all must succeed

Polish:
    1. Dla danych: `a: np.ndarray`, `b: np.ndarray` (patrz sekcja input)
    2. Przemnóż `a` i `b` używając mnożenia skalarnego
    3. Przemnóż `a` i `b` używając mnożenia macierzowego
    4. Przemnóż `b` i `a` używając mnożenia skalarnego
    5. Przemnóż `b` i `a` używając mnożenia macierzowego
    6. Omów wyniki
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mul_ab(a, b)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ValueError: operands could not be broadcast together with shapes (4,4) (4,2)

    >>> matmul_ab(a, b)
    array([[ 9,  2],
           [ 7,  3],
           [21,  8],
           [28,  8]])

    >>> mul_ba(b, a)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ValueError: operands could not be broadcast together with shapes (4,2) (4,4)

    >>> matmul_ba(b, a)
    Traceback (most recent call last):
    ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 4 is different from 2)
"""

import numpy as np


a = np.array([[1, 0, 1, 0],
              [0, 1, 1, 0],
              [3, 2, 1, 0],
              [4, 1, 2, 0]])

b = np.array([
    [4, 1],
    [2, 2],
    [5, 1],
    [2, 3]])


# callable: Multiply `a` and `b` using scalar multiplication
def mul_ab(a, b):
    return a * b

# callable: Multiply `a` and `b` using matrix multiplication
def matmul_ab(a, b):
    return a @ b

# callable: Multiply `b` and `a` using scalar multiplication
def mul_ba(b, a):
    return b * a

# callable: Multiply `b` and `a` using matrix multiplication
def matmul_ba(b, a):
    return b @ a
