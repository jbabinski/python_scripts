"""
* Assignment: CSV Format WriteListTuple
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

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

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    SepalLength,SepalWidth,PetalLength,PetalWidth,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    4.7,3.2,1.3,0.2,setosa
    7.0,3.2,4.7,1.4,versicolor
    7.6,3.0,6.6,2.1,virginica
    4.9,3.0,1.4,0.2,setosa
    <BLANKLINE>
"""

DATA = [
    ('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa')]

# str: DATA converted to CSV format
result = ...
