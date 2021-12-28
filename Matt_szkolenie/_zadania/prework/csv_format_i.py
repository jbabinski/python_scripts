"""
* Assignment: CSV Format WriteSchemaless
* Complexity: medium
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Define `header: str` with sorted list of unique keys from `DATA`
    2. `header` must be automatically generated from `DATA`
    3. Iterate over `DATA` and extract values for each header column
    4. Define `result: str` with header and matching values
    5. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: `"`
       c. Quoting: always
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `header: str` z posortowaną listą unikalnych kluczy z `DATA`
    2. `header` musi być generowany automatycznie z `DATA`
    3. Iteruj po `DATA` i wyciągnij wartości dla każdej kolumny z nagłówka
    4. Zdefiniuj `result: str` z nagłówkiem i pasującymi wartościami
    5. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: `"`
       c. Quoting: zawsze
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "Petal length","Petal width","Sepal length","Sepal width","Species"
    "","","5.1","3.5","setosa"
    "4.1","1.3","","","versicolor"
    "","1.8","6.3","","virginica"
    "","0.2","5.0","","setosa"
    "4.1","","","2.8","versicolor"
    "","1.8","","2.9","virginica"
    <BLANKLINE>
"""

DATA = [
    {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
    {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
    {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
    {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
    {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
    {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
]

# str: header has unique keys from DATA, row values match header columns
result = ...
