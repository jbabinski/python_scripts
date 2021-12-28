"""
* Assignment: DataFrame Mapping Split
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Parse data in `date` column as `datetime` object
    3. Split column `date` with into two separate: date and time columns
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Sparsuj dane w kolumnie `date` jako obiekty `datetime`
    3. Podziel kolumnę z `date` na dwie osobne: datę i czas
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.Series.dt.date`
    * `pd.Series.dt.time`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
          id   period            datetime   network  item           type  duration        date      time
    0      0  1999-11 1999-10-15 06:58:00  T-Mobile  data           data      34.5  1999-10-15  06:58:00
    1      1  1999-11 1999-10-15 06:58:00    Orange  call         mobile      13.0  1999-10-15  06:58:00
    2      2  1999-11 1999-10-15 14:46:00      Play  call         mobile      23.0  1999-10-15  14:46:00
    3      3  1999-11 1999-10-15 14:48:00      Plus  call         mobile       4.0  1999-10-15  14:48:00
    4      4  1999-11 1999-10-15 17:27:00  T-Mobile  call         mobile       4.0  1999-10-15  17:27:00
    ..   ...      ...                 ...       ...   ...            ...       ...         ...       ...
    825  825  2000-03 2000-03-13 00:38:00      AT&T   sms  international       1.0  2000-03-13  00:38:00
    826  826  2000-03 2000-03-13 00:39:00    Orange   sms         mobile       1.0  2000-03-13  00:39:00
    827  827  2000-03 2000-03-13 06:58:00    Orange  data           data      34.5  2000-03-13  06:58:00
    828  828  2000-03 2000-03-14 00:13:00      AT&T   sms  international       1.0  2000-03-14  00:13:00
    829  829  2000-03 2000-03-14 00:16:00      AT&T   sms  international       1.0  2000-03-14  00:16:00
    <BLANKLINE>
    [830 rows x 9 columns]
"""

import pandas as pd


DATA = 'https://python.astrotech.io/_static/phones-pl.csv'

result = pd.read_csv(DATA, parse_dates=['datetime'])
result['date'] = result['datetime'].dt.date
result['time'] = result['datetime'].dt.time
