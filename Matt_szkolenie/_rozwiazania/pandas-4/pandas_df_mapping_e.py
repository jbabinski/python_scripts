"""
* Assignment: Pandas Read JSON OpenAPI
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Use `requests` library
    3. Transpose data
    4. If cell is a `dict`, then extract value for `summary`
    5. If cell is empty, leave `pd.NA`
    6. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Użyj biblioteki `requests`
    3. Transponuj dane
    4. Jeżeli komórka jest `dict`, to wyciągnij wartość dla `summary`
    5. Jeżeli komórka jest pusta, pozostaw `pd.NA`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> len(result) > 0
    True
    >>> list(result.columns)
    ['put', 'post', 'get', 'delete']
    >>> list(result.index)  # doctest: +NORMALIZE_WHITESPACE
    ['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
     '/store/inventory', '/store/order', '/store/order/{orderId}',
     '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']
"""

import pandas as pd
import requests


DATA = 'https://python.astrotech.io/_static/openapi.json'

data = requests.get(DATA).json()
df = pd.DataFrame(data['paths'])
result = df.applymap(lambda x: x.get('summary') if type(x) is dict else '')
