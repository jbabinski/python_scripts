"""
* Assignment: OOP Relations Nested
* Complexity: medium
* Lines of code: 6 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Note, that enumeration starts with one
    3. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list
    >>> assert len(result) > 0
    >>> assert all(type(x) is dict for x in result)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'firstname': 'Mark',
      'lastname': 'Watney',
      'mission1_year': '2035',
      'mission1_name': 'Ares3'},
     {'firstname': 'Melissa',
      'lastname': 'Lewis',
      'mission1_year': '2030',
      'mission1_name': 'Ares1',
      'mission2_year': '2035',
      'mission2_name': 'Ares3'},
     {'firstname': 'Rick',
      'lastname': 'Martinez'}]
"""

import csv

FILE = r'_temporary.csv'

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "missions": [
        {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "missions": [
         {"year": "2030", "name": "Ares1"},
         {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Rick", "lastname": "Martinez", "missions": []}
]

# list[dict]: flatten data, each mission field prefixed with mission and number
result = ...
