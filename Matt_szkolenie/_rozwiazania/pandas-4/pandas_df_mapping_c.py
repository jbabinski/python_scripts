"""
* Assignment: DataFrame Mapping Month
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Add column `year` and `month` by parsing `period` column
    3. Month name must be a string month name, not a number (i.e.: 'January', 'May')
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Dodaj kolumnę `year` i `month` poprzez sparsowanie kolumny `period`
    3. Nazwa miesiąca musi być ciągiem znaków, a nie liczbą (i.e. 'January', 'May')
    4. Uruchom doctesty - wszystkie muszą się powieść

:Example:
    * if `period` column is "2015-01"
    * `year`: 2015
    * `month`: January

Hints:
    * `Series.str.split(expand=True)`
    * `df[ ['A', 'B'] ] = ...`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
          period            datetime   network  item           type  duration  year     month
    id
    0    1999-11 1999-10-15 06:58:00  T-Mobile  data           data      34.5  1999  November
    1    1999-11 1999-10-15 06:58:00    Orange  call         mobile      13.0  1999  November
    2    1999-11 1999-10-15 14:46:00      Play  call         mobile      23.0  1999  November
    3    1999-11 1999-10-15 14:48:00      Plus  call         mobile       4.0  1999  November
    4    1999-11 1999-10-15 17:27:00  T-Mobile  call         mobile       4.0  1999  November
    ..       ...                 ...       ...   ...            ...       ...   ...       ...
    825  2000-03 2000-03-13 00:38:00      AT&T   sms  international       1.0  2000     March
    826  2000-03 2000-03-13 00:39:00    Orange   sms         mobile       1.0  2000     March
    827  2000-03 2000-03-13 06:58:00    Orange  data           data      34.5  2000     March
    828  2000-03 2000-03-14 00:13:00      AT&T   sms  international       1.0  2000     March
    829  2000-03 2000-03-14 00:16:00      AT&T   sms  international       1.0  2000     March
    <BLANKLINE>
    [830 rows x 8 columns]
"""

import pandas as pd


DATA = 'https://python.astrotech.io/_static/phones-pl.csv'
MONTHS_EN = ['January', 'February', 'March', 'April',
             'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']
MONTHS = dict(enumerate(MONTHS_EN, start=1))

result = ...
