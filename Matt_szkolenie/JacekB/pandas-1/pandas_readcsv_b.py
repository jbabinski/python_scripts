"""
* Assignment: Pandas Read CSV Replace
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Read data from `DATA` to `result: pd.DataFrame`
    2. Use provided column names in `COLUMNS`
    3. Read labels from the first row
    4. Replace data in `label` column with values extracted above
    5. Define `result: pd.DataFrame` with 25 first rows
    6. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` do `result: pd.DataFrame`
    2. Użyj podanych w `COLUMNS` nazw kolumn
    3. Wczytaj nazwy labeli z pierwszego wiersza
    4. Podmień dane w kolumnie `label` na wartości wyciągnięte powyżej
    5. Zdefiniuj `result: pd.DataFrame` z 25 pierwszymi wierszami
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `class_labels = pd.read_csv(DATA, nrows=0).columns[2:]`
    * `label_encoder = dict(enumerate(class_labels))`
    * `df['label'].replace({'from': 'to'}, inplace=True)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) == 25
    True

    >>> result.loc[[0,1,2,3,4,5], ['mean radius', 'mean texture', 'label']]
       mean radius  mean texture      label
    0        17.99         10.38  malignant
    1        20.57         17.77  malignant
    2        19.69         21.25  malignant
    3        11.42         20.38  malignant
    4        20.29         14.34  malignant
    5        12.45         15.70  malignant

    >>> result['label'].value_counts()
    malignant    22
    benign        3
    Name: label, dtype: int64
"""

import pandas as pd

DATA = 'https://python.astrotech.io/_static/breast-cancer.csv'

COLUMNS = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
           'mean smoothness', 'mean compactness', 'mean concavity',
           'mean concave points', 'mean symmetry', 'mean fractal dimension',
           'radius error', 'texture error', 'perimeter error', 'area error',
           'smoothness error', 'compactness error', 'concavity error',
           'concave points error', 'symmetry error',
           'fractal dimension error', 'worst radius', 'worst texture',
           'worst perimeter', 'worst area', 'worst smoothness',
           'worst compactness', 'worst concavity', 'worst concave points',
           'worst symmetry', 'worst fractal dimension', 'label']

# pd.DataFrame: read DATA, substitute column names, and labels, select 25 rows
class_labels = pd.read_csv(DATA, nrows=0).columns[2:]
label_encoder = dict(enumerate(class_labels))

result = (pd.read_csv(DATA,
                      names=COLUMNS,
                      skiprows=1,
                      nrows=25)
          .replace(label_encoder))
