"""
* Assignment: CSV Format WriteListDict
* Complexity: medium
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Define `result: str` with `DATA` converted to CSV format
    2. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: None
       c. Quoting: never
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z `DATA` przekonwertowaną do formatu CSV
    2. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: None
       c. Quoting: nigdy
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(obj)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    sepal_length,sepal_width,petal_length,petal_width,species
    5.1,3.5,1.4,0.2,setosa
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    <BLANKLINE>
"""

DATA = [{'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4,
         'petal_width': 0.2, 'species': 'setosa'},
        {'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1,
         'petal_width': 1.9, 'species': 'virginica'},
        {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4,
         'petal_width': 0.2, 'species': 'setosa'},
        {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1,
         'petal_width': 1.3, 'species': 'versicolor'},
        {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6,
         'petal_width': 1.8, 'species': 'virginica'},
        {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5,
         'petal_width': 1.5, 'species': 'versicolor'}]

# str: DATA converted to CSV format
result = ...
