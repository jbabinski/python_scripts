"""
* Assignment: Pandas Read JSON OpenAPI
* Complexity: medium
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Import `requests` module
    2. Define `resp` with result of `requests.get()` for `DATA`
    3. Define `data` with conversion of `resp` from JSON to Python dict by calling `.json()` on `resp`
    4. Define `result: pd.DataFrame` from value for key `paths` in `data` dict
    5. Run doctests - all must succeed

Polish:
    1. Zaimportuj moduł `requests`
    2. Zdefiniuj `resp` z resultatem `requests.get()` dla `DATA`
    3. Zdefiniuj `data` z przekształceniem `resp` z JSON do Python dict wywołując `.json()` na `resp`
    4. Zdefiniuj `result: pd.DataFrame` dla wartości z klucza `paths` w słowniku `data`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.DataFrame(data)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> list(result.index)
    ['put', 'post', 'get', 'delete']
    >>> list(result.columns)  # doctest: +NORMALIZE_WHITESPACE
    ['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
     '/store/inventory', '/store/order', '/store/order/{orderId}',
     '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']
"""

import pandas as pd
import requests

DATA = 'https://python.astrotech.io/_static/openapi.json'


# requests.models.Response: result of `requests.get()` for `DATA`
resp = requests.get(DATA)

# dict: conversion of `resp` by calling `.json()` on `resp`
data = resp.json()

# pd.DataFrame: read DATA
result = pd.DataFrame(data['paths'])
