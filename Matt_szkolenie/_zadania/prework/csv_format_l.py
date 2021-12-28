"""
* Assignment: CSV Format WriteObjects
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


class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


DATA = [Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
        Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
        Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
        Iris(6.4, 3.2, 4.5, 1.5, 'versicolor')]

# str: DATA converted to CSV format
result = ...
