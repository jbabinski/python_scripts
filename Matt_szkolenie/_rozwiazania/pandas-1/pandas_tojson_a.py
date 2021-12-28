"""
* Assignment: DataFrame Export JSON
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. While reading use `header=0` parameter
    3. Select 146 head rows, and last 11 from it
    4. Export data from column `Event` to file the `FILE`
    5. Data has to be in JSON format
    6. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `result: pd.DataFrame`
    2. Przy wczytywaniu użyj parametru `header=0`
    3. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    4. Wyeksportuj dane z kolumny `Event` do pliku `FILE`
    5. Dane mają być w formacie JSON
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> import json

    >>> result = open(FILE).read()

    >>> json.loads(result)  # doctest: +NORMALIZE_WHITESPACE
    {'135': 'LM lunar landing.',
     '136': 'LM powered descent  engine cutoff.',
     '137': 'Decision made to  proceed with EVA prior to first rest period.',
     '138': 'Preparation for EVA  started.',
     '139': 'EVA started (hatch  open).',
     '140': 'CDR completely outside  LM on porch.',
     '141': 'Modular equipment  stowage assembly deployed (CDR).',
     '142': 'First clear TV picture  received.',
     '143': 'CDR at foot of ladder  (starts to report, then pauses to listen).',
     '144': 'CDR at foot of ladder  and described surface as “almost like a powder.”',
     '145': '1st step  taken lunar surface (CDR). “That’s one small step for a man…one giant leap  for mankind.”'}

    >>> remove(FILE)
"""

import pandas as pd

DATA = 'https://python.astrotech.io/_static/apollo11.html'
FILE = r'_temporary.json'

# pd.DataFrame: dump DATA to FILE in JSON format
result = ...
