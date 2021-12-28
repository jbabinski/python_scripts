"""
* Assignment: DataFrame NaN
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Pomiń pierwszą linię z metadanymi
    3. Zmień nazwy kolumn na:
        a. Sepal length
        b. Sepal width
        c. Petal length
        d. Petal width
        e. Species
    4. Podmień wartości w kolumnie species
        a. 0 -> 'setosa',
        b. 1 -> 'versicolor',
        c. 2 -> 'virginica'
    5. Wybierz wartości w kolumnie 'Petal length' mniejsze od 4
    6. Wybrane wartości ustaw na `NaN`
    7. Interpoluj liniowo wszystkie wartości `NaN`
    8. Usuń wiersze z pozostałymi wartościami `NaN`
    9. Zdefiniuj `result` jako dwa pierwsze wiersze
    10. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
       Sepal length  Sepal width  Petal length  Petal width     Species
    1           5.9          3.0           5.1          1.8   virginica
    2           6.0          3.4           4.5          1.6  versicolor
"""

import pandas as pd
import numpy as np

DATA = 'https://python.astrotech.io/_static/iris-dirty.csv'
COLUMNS = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']

species = ['setosa', 'versicolor', 'virginica']

label_encoder = dict(enumerate(species))

data = pd.read_csv(DATA,
                   names=COLUMNS,
                   skiprows=1)

data['Species'] = data['Species'].replace(label_encoder)
data.loc[data['Petal length'].astype('float') < 4.0, 'Petal length'] = np.nan

result = (data.interpolate(method='linear')
          .dropna()
          .head(2))
