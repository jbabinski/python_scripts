"""
* Assignment: CSV Format WriteListDict
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Convert `DATA` to CSV as `result: str`:
       a. do not add header
       a. firstname - first field
       c. lastname - second field
    2. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: None
       c. Quoting: None
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` do CSV jako `result: str`:
       a. nie dodawaj nagłówka
       b. imię - pierwsze pole
       c. nazwisko - drugie pole
    2. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: None
       c. Quoting: None
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)   # doctest: +NORMALIZE_WHITESPACE
    Jan,Twardowski
    Rick,Martinez
    Mark,Watney
    Ivan,Ivanovic
    Melissa,Lewis
    <BLANKLINE>
"""

DATA = [
    {'firstname': 'Jan', 'lastname': 'Twardowski'},
    {'firstname': 'Rick', 'lastname': 'Martinez'},
    {'firstname': 'Mark', 'lastname': 'Watney'},
    {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
    {'firstname': 'Melissa', 'lastname': 'Lewis'},
]

# str: multiline string with `firstname,lastname` pairs
result = ...
