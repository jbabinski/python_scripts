# pandas

# pd.DataFrame -> list[pd.Series] + dodatkowe metody
# pd.Series -> np.array + dodatkowe metody
from io import StringIO

import pandas as pd


# Database -> SQL -> pd.DataFrame -> analiza

# Pandas:
# - "alternatywą" dla SQL
# - data exploration
# - R&D na danych

# Pandas:
# - numpy
# - cython
# - numba


# pandas -> 0 - 5GB do nawet 15 GB (trochę mniej niż połowa RAM)
# pandas + chunksize -> 50 GB
# dask -> 250 ~ 500 GB
# pyspark


# domyślnie operacje na Pandas nie podmieniają danych
# większość z nich ma parametr `inplace`
# jak się go ustawi na True, to podmienia dane
# jak jest na False (a tak jest domyślnie) to tylko pokaże co by zrobił

# %% read csv
import requests


DATA = 'http://python.astrotech.io/_static/martian-en.csv'

df = pd.read_csv(DATA,
                 nrows=10,
                 skiprows=2,
                 encoding='utf-8',
                 delimiter=';',
                 decimal=',',
                 parse_dates=['datetime', 'date', 'time'],
                 index_col=['datetime'],
                 names=['A', 'B', 'C', 'D'],)


#%% read string

DATA = 'https://python.astrotech.io/_static/iris.csv'
data = requests.get(DATA).text
data
'sepal_length,sepal_width,petal_length,petal_width,species\n5.4,3.9,1.3,0.4,setosa\n5.9,3.0,5.1,1.8,virginica\n6.0,3.4,4.5,1.6,versicolor\n7.3,2.9,6.3,1.8,virginica\n5.6,2.5,3.9,1.1,versicolor\n5.4,3.9,1.3,0.4,setosa\n5.5,2.6,4.4,1.2,versicolor\n5.7,2.9,4.2,1.3,versicolor\n4.9,3.1,1.5,0.1,setosa\n6.7,2.5,5.8,1.8,virginica\n6.5,3.0,5.2,2.0,virginica\n5.1,3.3,1.7,0.5,setosa\n4.6,3.4,1.4,0.3,setosa\n7.4,2.8,6.1,1.9,virginica\n7.7,3.8,6.7,2.2,virginica\n6.6,3.0,4.4,1.4,versicolor\n7.2,3.2,6.0,1.8,virginica\n5.8,2.7,5.1,1.9,virginica\n6.5,3.0,5.5,1.8,virginica\n6.1,2.9,4.7,1.4,versicolor\n5.2,3.5,1.5,0.2,setosa\n5.9,3.2,4.8,1.8,versicolor\n6.1,3.0,4.6,1.4,versicolor\n5.2,4.1,1.5,0.1,setosa\n5.1,3.8,1.9,0.4,setosa\n4.8,3.4,1.6,0.2,setosa\n6.0,2.2,5.0,1.5,virginica\n6.4,3.2,5.3,2.3,virginica\n4.9,3.0,1.4,0.2,setosa\n6.3,2.9,5.6,1.8,virginica\n6.0,3.0,4.8,1.8,virginica\n4.3,3.0,1.1,0.1,setosa\n6.9,3.1,4.9,1.5,versicolor\n6.3,2.3,4.4,1.3,versicolor\n6.4,3.1,5.5,1.8,virginica\n6.5,3.2,5.1,2.0,virginica\n5.0,3.3,1.4,0.2,setosa\n5.5,2.4,3.7,1.0,versicolor\n6.1,3.0,4.9,1.8,virginica\n6.4,3.2,4.5,1.5,versicolor\n5.5,2.4,3.8,1.1,versicolor\n6.2,2.9,4.3,1.3,versicolor\n6.2,2.8,4.8,1.8,virginica\n5.7,2.5,5.0,2.0,virginica\n5.4,3.4,1.5,0.4,setosa\n5.6,3.0,4.1,1.3,versicolor\n6.0,2.7,5.1,1.6,versicolor\n5.2,2.7,3.9,1.4,versicolor\n6.7,3.1,4.7,1.5,versicolor\n5.5,2.5,4.0,1.3,versicolor\n6.7,3.3,5.7,2.5,virginica\n5.1,3.7,1.5,0.4,setosa\n7.7,3.0,6.1,2.3,virginica\n6.6,2.9,4.6,1.3,versicolor\n4.8,3.4,1.9,0.2,setosa\n4.8,3.0,1.4,0.1,setosa\n4.4,3.2,1.3,0.2,setosa\n5.1,3.8,1.5,0.3,setosa\n5.4,3.0,4.5,1.5,versicolor\n4.6,3.2,1.4,0.2,setosa\n5.6,3.0,4.5,1.5,versicolor\n5.5,3.5,1.3,0.2,setosa\n6.5,2.8,4.6,1.5,versicolor\n5.6,2.8,4.9,2.0,virginica\n5.0,3.5,1.6,0.6,setosa\n5.7,4.4,1.5,0.4,setosa\n5.4,3.4,1.7,0.2,setosa\n4.8,3.1,1.6,0.2,setosa\n5.0,3.6,1.4,0.2,setosa\n5.1,3.5,1.4,0.3,setosa\n5.7,2.8,4.1,1.3,versicolor\n4.9,3.1,1.5,0.2,setosa\n6.4,2.7,5.3,1.9,virginica\n5.0,3.5,1.3,0.3,setosa\n4.6,3.6,1.0,0.2,setosa\n5.7,2.8,4.5,1.3,versicolor\n6.3,2.5,4.9,1.5,versicolor\n7.7,2.8,6.7,2.0,virginica\n7.2,3.6,6.1,2.5,virginica\n6.4,2.9,4.3,1.3,versicolor\n4.9,3.6,1.4,0.1,setosa\n7.2,3.0,5.8,1.6,virginica\n7.0,3.2,4.7,1.4,versicolor\n5.1,3.5,1.4,0.2,setosa\n5.8,2.7,3.9,1.2,versicolor\n4.7,3.2,1.6,0.2,setosa\n6.9,3.1,5.4,2.1,virginica\n5.7,2.6,3.5,1.0,versicolor\n5.7,3.8,1.7,0.3,setosa\n5.8,2.7,5.1,1.9,virginica\n4.4,2.9,1.4,0.2,setosa\n6.4,2.8,5.6,2.2,virginica\n6.1,2.8,4.7,1.2,versicolor\n5.4,3.7,1.5,0.2,setosa\n6.4,2.8,5.6,2.1,virginica\n6.7,3.0,5.0,1.7,versicolor\n4.9,2.4,3.3,1.0,versicolor\n4.5,2.3,1.3,0.3,setosa\n5.0,3.0,1.6,0.2,setosa\n5.1,2.5,3.0,1.1,versicolor\n6.3,3.4,5.6,2.4,virginica\n6.5,3.0,5.8,2.2,virginica\n6.7,3.0,5.2,2.3,virginica\n6.2,2.2,4.5,1.5,versicolor\n5.3,3.7,1.5,0.2,setosa\n6.1,2.8,4.0,1.3,versicolor\n5.0,2.3,3.3,1.0,versicolor\n6.8,2.8,4.8,1.4,versicolor\n7.1,3.0,5.9,2.1,virginica\n6.3,2.7,4.9,1.8,virginica\n5.1,3.8,1.6,0.2,setosa\n7.6,3.0,6.6,2.1,virginica\n6.9,3.1,5.1,2.3,virginica\n5.0,3.4,1.6,0.4,setosa\n6.7,3.3,5.7,2.1,virginica\n5.8,2.6,4.0,1.2,versicolor\n7.7,2.6,6.9,2.3,virginica\n5.8,4.0,1.2,0.2,setosa\n5.2,3.4,1.4,0.2,setosa\n5.7,3.0,4.2,1.2,versicolor\n4.6,3.1,1.5,0.2,setosa\n7.9,3.8,6.4,2.0,virginica\n4.8,3.0,1.4,0.3,setosa\n6.7,3.1,5.6,2.4,virginica\n5.5,2.3,4.0,1.3,versicolor\n6.2,3.4,5.4,2.3,virginica\n6.3,2.5,5.0,1.9,virginica\n6.3,3.3,6.0,2.5,virginica\n6.7,3.1,4.4,1.4,versicolor\n4.4,3.0,1.3,0.2,setosa\n6.1,2.6,5.6,1.4,virginica\n5.8,2.7,4.1,1.0,versicolor\n5.4,3.9,1.7,0.4,setosa\n5.0,3.2,1.2,0.2,setosa\n5.8,2.8,5.1,2.4,virginica\n4.7,3.2,1.3,0.2,setosa\n6.9,3.2,5.7,2.3,virginica\n5.0,2.0,3.5,1.0,versicolor\n5.6,2.7,4.2,1.3,versicolor\n6.0,2.2,4.0,1.0,versicolor\n5.1,3.4,1.5,0.2,setosa\n6.0,2.9,4.5,1.5,versicolor\n5.6,2.9,3.6,1.3,versicolor\n6.8,3.0,5.5,2.1,virginica\n5.5,4.2,1.4,0.2,setosa\n6.3,3.3,4.7,1.6,versicolor\n5.9,3.0,4.2,1.5,versicolor\n5.0,3.4,1.5,0.2,setosa\n4.9,2.5,4.5,1.7,virginica\n6.3,2.8,5.1,1.5,virginica\n6.8,3.2,5.9,2.3,virginica\n'
pd.read_csv(data)
# SError: [Errno 63] File name too long: 'sepal_length,...5.9,2.3,virginica\n'
data = StringIO(data)
pd.read_csv(data)


# %% read html

DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'
result = pd.read_html(DATA)
