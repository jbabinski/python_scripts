"""
* Assignment: CSV Format ReadSwitch
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Convert `DATA` to `result: list[tuple[str]]`
    2. Substitute last element (class label) with value from `LABEL_ENCODER`
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: list[tuple[str]]`
    2. Podmień ostatni element (etykietę klasową) z wartością z `LABEL_ENCODER`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.splitlines()`
    * `str.strip()`
    * `str.split()`
    * `dict.get()`
    * `list() + list()`
    * `list.append()`
    * `tuple()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result), \
    'All rows in `result` should be tuple'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     ('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]
"""

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,0
5.1,3.5,1.4,0.2,1
5.7,2.8,4.1,1.3,2"""

LABEL_ENCODER = {
    '0': 'virginica',
    '1': 'setosa',
    '2': 'versicolor'}

# list[tuple]: data from file (note the list[tuple] format!)
result = ...
