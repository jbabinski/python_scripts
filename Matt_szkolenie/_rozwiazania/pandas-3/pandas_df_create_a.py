"""
* Assignment: DataFrame Create
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Create `result: pd.DataFrame` for input data
    2. Run doctests - all must succeed

Polish:
    1. Stwórz `result: pd.DataFrame` dla danych wejściowych
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Use selection with `alt` key in your IDE

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
         Crew Role        Astronaut
    0   Prime  CDR   Neil Armstrong
    1   Prime  LMP      Buzz Aldrin
    2   Prime  CMP  Michael Collins
    3  Backup  CDR     James Lovell
    4  Backup  LMP   William Anders
    5  Backup  CMP       Fred Haise
"""

import pandas as pd


"""
"Prime", "CDR", "Neil Armstrong"
"Prime", "LMP", "Buzz Aldrin"
"Prime", "CMP", "Michael Collins"
"Backup", "CDR", "James Lovell"
"Backup", "LMP", "William Anders"
"Backup", "CMP", "Fred Haise"
"""

result = pd.DataFrame([
    {"Crew": "Prime", "Role": "CDR", "Astronaut": "Neil Armstrong"},
    {"Crew": "Prime", "Role": "LMP", "Astronaut": "Buzz Aldrin"},
    {"Crew": "Prime", "Role": "CMP", "Astronaut": "Michael Collins"},
    {"Crew": "Backup", "Role": "CDR", "Astronaut": "James Lovell"},
    {"Crew": "Backup", "Role": "LMP", "Astronaut": "William Anders"},
    {"Crew": "Backup", "Role": "CMP", "Astronaut": "Fred Haise"},
])
