"""
* Assignment: Numpy Loadtext
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Load text from `URL`
    2. From the first line select Iris species names and save as str to `species: np.ndarray`
    3. For other lines:
        a. Read columns with data and save as float to `features: np.ndarray`
        b. Read last column with species numbers and save as `int` to `labels: np.ndarray`
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj tekst z `URL`
    2. Z pierwszej linii wybierz nazwy gatunków Irysów i zapisz rezultat jako str do `species: np.ndarray`
    3. W pozostałych linii:
        a Wczytaj kolumny z danymi i zapisz jako float do `features: np.ndarray`
        b Wczytaj ostatnią kolumnę z numerami gatunków i zapisz jako `int` do `labels: np.ndarray`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert species is not Ellipsis, \
    'Assign result to variable: `species`'
    >>> assert type(species) is np.ndarray, \
    'Variable `species` has invalid type, expected: np.ndarray'

    >>> assert features is not Ellipsis, \
    'Assign result to variable: `features`'
    >>> assert type(features) is np.ndarray, \
    'Variable `features` has invalid type, expected: np.ndarray'

    >>> assert labels is not Ellipsis, \
    'Assign result to variable: `labels`'
    >>> assert type(labels) is np.ndarray, \
    'Variable `labels` has invalid type, expected: np.ndarray'

    >>> species
    array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

    >>> len(features)
    151

    >>> features[:3]
    array([[5.4, 3.9, 1.3, 0.4],
           [5.9, 3. , 5.1, 1.8],
           [6. , 3.4, 4.5, 1.6]])

    >>> features[-3:]
    array([[4.9, 2.5, 4.5, 1.7],
           [6.3, 2.8, 5.1, 1.5],
           [6.8, 3.2, 5.9, 2.3]])

    >>> labels
    array([0, 2, 1, 2, 1, 0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 0, 1,
           1, 0, 0, 0, 2, 2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 2,
           0, 1, 1, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 0,
           0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 1, 2, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1,
           0, 2, 0, 2, 1, 0, 2, 1, 1, 0, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 2, 2,
           0, 2, 2, 0, 2, 1, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 1,
           0, 0, 2, 0, 2, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1, 0, 2, 2, 2])
"""

import numpy as np


DATA = 'https://python.astrotech.io/_static/iris-dirty.csv'

species = ...
features = ...
labels = ...
