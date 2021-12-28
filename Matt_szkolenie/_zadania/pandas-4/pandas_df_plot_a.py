"""
* Assignment: DataFrame Plot
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Select `Luminance` stylesheet
    3. Parse column with dates
    4. Select desired date and location, then resample by hour
    5. Display chart (line) with activity hours in "Sleeping Quarters upper" location
    6. Active is when `Luminance` is not zero
    7. Easy: for day 2019-09-28
    8. Advanced: for each day, as subplots
    9. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Wybierz arkusz `Luminance`
    3. Sparsuj kolumny z datami
    4. Wybierz pożądaną datę i lokację, następnie próbkuj co godzinę
    5. Aktywność jest gdy `Luminance` jest różna od zera
    6. Wyświetl wykres (line) z godzinami aktywności w dla lokacji "Sleeping Quarters upper"
    7. Łatwe: dla dnia 2019-09-28
    8. Zaawansowane: dla wszystkich dni, jako subplot
    9. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.Series.apply(np.sign)` :ref:`Numpy signum`
    * `pd.Series.resample('H').sum()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    datetime
    2019-09-28 00:00:00+00:00    1
    2019-09-28 01:00:00+00:00    1
    2019-09-28 02:00:00+00:00    1
    2019-09-28 03:00:00+00:00    1
    2019-09-28 04:00:00+00:00    0
                                ..
    2019-09-28 19:00:00+00:00    1
    2019-09-28 20:00:00+00:00    1
    2019-09-28 21:00:00+00:00    1
    2019-09-28 22:00:00+00:00    1
    2019-09-28 23:00:00+00:00    1
    Freq: H, Name: value, Length: 24, dtype: int64
"""

import numpy as np
import pandas as pd


DATA = 'https://python.astrotech.io/_static/sensors-optima.xlsx'
WHERE = 'Sleeping Quarters upper'
WHEN = '2019-09-28'

result = ...
