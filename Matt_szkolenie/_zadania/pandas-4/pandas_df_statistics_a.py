"""
* Assignment: DataFrame Statistics
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz `df: pd.DataFrame` z 50 wierszami:
        a. kolumna `mileage` - losowe `int` [0, 200_000)
        b. kolumna `consumption` - losowe `int` [0, 20)
    3. Dodaj kolumnę `status` o wartościach:
        a. `old` jeżeli `mileage` powyżej 100_000 km
        b. `young` jeżeli `mileage` od 10_000 km do 50_000 km
        c. `new` jeżeli `mileage` od 0 do 10_000 km
    4. Używając `pd.cut` dodaj kolumnę `type`:
        a. jeżeli `consumption` [0, 1] `type` to `electric`
        b. jeżeli `consumption` [2, 10] `type` to `car`
        c. jeżeli `consumption` 11 i więcej, `type` to `truck`
    5. Przeanalizuj dane statystycznie:
        a. Zapisz podstawowe statystyki opisowe (`DataFrame.describe()`) do `result: pd.DataFrame`
        b. Sprawdź liczność grup (`DataFrame.count()`, `Series.value_counts()`)
    6. Uruchom doctesty - wszystkie muszą się powieść

Extra Task:
    1. (wymaga wiedzy z przyszłych rozdziałów)
    2. Narysuj histogram dla `consumption`
    3. Pogrupuj dane po `type` i `status` a następnie wypisz statystyki opisowe
    4. Pogrupuj dane po `type` i `status`, wypisz statystyki opisowe a następnie je transponuj

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
                mileage  consumption
    count      50.00000    50.000000
    mean   110421.02000     9.320000
    std     53170.24328     6.244802
    min      7877.00000     0.000000
    25%     71239.75000     4.000000
    50%    115186.00000     9.000000
    75%    154889.00000    14.750000
    max    199827.00000    20.000000
"""

import pandas as pd
import numpy as np
np.random.seed(0)


df = pd.DataFrame({
    'mileage': np.random.randint(0, 200_000, size=50),
    'consumption': np.random.randint(0, 21, size=50),
})

result = ...
