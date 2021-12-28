"""
* Assignment: DataFrame Sample
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Ustaw wszystkie wiersze w losowej kolejności
    3. Zresetuj index nie pozostawiając kopii zapasowej starego
    4. Zdefiniuj `result` z ostatnimi 10 wierszami
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
                           Name        Country Gender                                            Flights  Total Flights Total Flight Time (ddd:hh:mm)
    557  Thomas Marshburn, M.D.  United States    Man               STS-127 (2009), Soyuz TMA-07M (2012)              2                     161:07:03
    558           Michael Baker  United States    Man  STS-43 (1991), STS-52 (1992), STS-68 (1994), S...              4                     040:03:04
    559            Rick Husband  United States    Man                      STS-96 (1999), STS-107 (2003)              2                     025:13:33
    560     Svetlana Savitskaya   Soviet Union  Woman                Soyuz T-7 (1982), Soyuz T-12 (1984)              2                     019:17:07
    561   Charles "Pete" Conrad  United States    Man  Gemini 5 (1965), Gemini 11 (1966), Apollo 12 (...              4                     049:03:38
    562     Lawrence J. DeLucas  United States    Man                                      STS-50 (1992)              1                     013:19:30
    563      Aleksandr Laveykin   Soviet Union    Man                                  Soyuz TM-2 (1987)              1                     174:03:25
    564           Owen Garriott  United States    Man                      Skylab 3 (1973), STS-9 (1983)              2                     069:17:56
    565             Ivan Vagner         Russia    Man                                 Soyuz MS-16 (2020)              1                     145:04:14
    566        Yuri Malenchenko         Russia    Man  Soyuz TM-19 (1994), STS-106 (2000), Soyuz TMA-...              6                     826:09:22
"""

import pandas as pd
import numpy as np
np.random.seed(0)


DATA = 'https://python.astrotech.io/_static/astro-database.csv'

result = pd.read_csv(DATA).sample(frac=1.0).reset_index(drop=True).tail(10)
