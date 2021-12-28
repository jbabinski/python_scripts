"""
* Assignment: Pandas Read PythonObj
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Non-functional requirements:
        a. Use `,` to separate mission fields
        b. Use `;` to separate missions
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z DATA jako result: pd.DataFrame
    2. Wymagania niefunkcjonalne:
        a. Użyj `,` do oddzielania pól mission
        b. Użyj `;` do oddzielenia missions
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(obj)`
    * Nested `for`
    * `str.join(';', sequence)`
    * `str.join(',', sequence)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` has invalid type, should be `pd.DataFrame`'

    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
      firstname  lastname                 missions
    0      Mark    Watney              2035,Ares 3
    1   Melissa     Lewis  2030,Ares 1;2035,Ares 3
    2      Rick  Martinez
"""

import pandas as pd


class Astronaut:
    def __init__(self, firstname, lastname, missions=None):
        self.firstname = firstname
        self.lastname = lastname
        self.missions = list(missions) if missions else []


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


DATA = [
    Astronaut('Mark', 'Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa', 'Lewis', missions=[
        Mission(2030, 'Ares 1'),
        Mission(2035, 'Ares 3')]),

    Astronaut('Rick', 'Martinez', missions=[]),
]


# list[dict]: convert DATA to list[dict], then flatten
data = ...

# pd.DataFrame: DATA as pd.DataFrame
result = ...
