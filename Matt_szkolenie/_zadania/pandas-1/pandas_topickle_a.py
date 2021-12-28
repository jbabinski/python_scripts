"""
* Assignment: DataFrame Export Pickle
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

    >>> assert type(result) is pd.DataFrame

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 20)

    >>> pd.read_pickle(FILE)
    135                                    LM lunar landing.
    136                   LM powered descent  engine cutoff.
    137    Decision made to  proceed with EVA prior to fi...
    138                        Preparation for EVA  started.
    139                           EVA started (hatch  open).
    140                 CDR completely outside  LM on porch.
    141    Modular equipment  stowage assembly deployed (...
    142                    First clear TV picture  received.
    143    CDR at foot of ladder  (starts to report, then...
    144    CDR at foot of ladder  and described surface a...
    145    1st step  taken lunar surface (CDR). “That’s o...
    Name: Event, dtype: object

    >>> remove(FILE)
"""

import pandas as pd

DATA = 'https://python.astrotech.io/_static/apollo11.html'
FILE = r'_temporary.pkl'

# pd.DataFrame: dump DATA to FILE in Pickle format
result = ...
