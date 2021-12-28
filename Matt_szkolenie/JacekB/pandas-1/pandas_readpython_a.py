"""
* Assignment: Pandas Read PythonDict
* Complexity: medium
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Note, that enumeration starts with one
    3. Convert data to `result: pd.DataFrame`
    4. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Przekonwertuj dane do `result: pd.DataFrame`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` has invalid type, should be `pd.DataFrame`'

    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
      firstname  lastname mission1_year mission1_name mission2_year mission2_name
    0      Mark    Watney          2035         Ares3           NaN           NaN
    1   Melissa     Lewis          2030         Ares1          2035         Ares3
    2      Rick  Martinez           NaN           NaN           NaN           NaN
"""
import pandas as pd


DATA = [
    {"firstname": "Mark", "lastname": "Watney", "missions": [
        {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "missions": [
         {"year": "2030", "name": "Ares1"},
         {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Rick", "lastname": "Martinez", "missions": []}
]


# list[dict]: flatten data, each mission field prefixed with mission and number
data = []

for x in DATA:
    dct = {}
    dct.update({i: x.get(i) for i in x.keys() if i != 'missions'})
    for cnt, mis in enumerate(x.get('missions'), start=1):        # tutaj mozna jeszcze for po keys, zeby nie wpisywac
        dct.update({f"mission{cnt}_year": str(mis.get('year'))})  # na sztywno year/name
        dct.update({f"mission{cnt}_name": str(mis.get('name'))})
    data.append(dct)

# pd.DataFrame: data as pd.DataFrame
result = pd.DataFrame(data)
