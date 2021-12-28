import string

import numpy as np
import pandas as pd


s = pd.Series([1, 2, 3])
s = pd.Series(['a', 'b', 'c'])
s = pd.Series(['a', 1, 1.5])
s = pd.Series(np.arange(0, 10, 2))
s = pd.Series(['A', 'B', 'C', 'D', 'E'])
s = pd.Series(list(string.ascii_uppercase)[:5])

pd.Series(range(0, 5))
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# dtype: int64

pd.Series(np.arange(0, 5))
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# dtype: int64

data = pd.date_range(start='1999-12-27', end='2000-01-05')
# pd.Series(data)
# 0   1999-12-27
# 1   1999-12-28
# 2   1999-12-29
# 3   1999-12-30
# 4   1999-12-31
# 5   2000-01-01
# 6   2000-01-02
# 7   2000-01-03
# 8   2000-01-04
# 9   2000-01-05
# dtype: datetime64[ns]

data = np.arange(0, 10)

s = pd.Series(data=data,
              index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

s.index
# Index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], dtype='object')


# RangeIndex()  # dolny jest włącznie i górny jest rozłącznie
# Int64Index()          # dolny i górny jest włącznie
# Float64Index()        # dolny i górny jest włącznie
# Index()               # dolny i górny jest włącznie
# DatetimeIndex()       # dolny i górny jest włącznie


s = pd.Series(index=pd.date_range(start='1999-12-27', end='2000-01-05'),
              data=np.arange(10))

index = pd.date_range(start='1999-12-27', end='2000-01-05')
index
DatetimeIndex(['1999-12-27', '1999-12-28', '1999-12-29', '1999-12-30',
               '1999-12-31', '2000-01-01', '2000-01-02', '2000-01-03',
               '2000-01-04', '2000-01-05'],
              dtype='datetime64[ns]', freq='D')
len(index)
10
data = np.arange(len(index))
pd.Series(index=index, data=data)
1999 - 12 - 27
0
1999 - 12 - 28
1
1999 - 12 - 29
2
1999 - 12 - 30
3
1999 - 12 - 31
4
2000 - 01 - 01
5
2000 - 01 - 02
6
2000 - 01 - 03
7
2000 - 01 - 04
8
2000 - 01 - 05
9
Freq: D, dtype: int64
s = pd.Series(index=index, data=data)
s.index
DatetimeIndex(['1999-12-27', '1999-12-28', '1999-12-29', '1999-12-30',
               '1999-12-31', '2000-01-01', '2000-01-02', '2000-01-03',
               '2000-01-04', '2000-01-05'],
              dtype='datetime64[ns]', freq='D')
s
1999 - 12 - 27
0
1999 - 12 - 28
1
1999 - 12 - 29
2
1999 - 12 - 30
3
1999 - 12 - 31
4
2000 - 01 - 01
5
2000 - 01 - 02
6
2000 - 01 - 03
7
2000 - 01 - 04
8
2000 - 01 - 05
9
Freq: D, dtype: int64

s['1999']
1999 - 12 - 27
0
1999 - 12 - 28
1
1999 - 12 - 29
2
1999 - 12 - 30
3
1999 - 12 - 31
4
Freq: D, dtype: int64

s['1999-12']
1999 - 12 - 27
0
1999 - 12 - 28
1
1999 - 12 - 29
2
1999 - 12 - 30
3
1999 - 12 - 31
4
Freq: D, dtype: int64

s['1999':'1999']
1999 - 12 - 27
0
1999 - 12 - 28
1
1999 - 12 - 29
2
1999 - 12 - 30
3
1999 - 12 - 31
4
Freq: D, dtype: int64

s['1999':'1999-12-29']
1999 - 12 - 27
0
1999 - 12 - 28
1
1999 - 12 - 29
2
Freq: D, dtype: int64

s['1999-12':'1999-12-29']
1999 - 12 - 27
0
1999 - 12 - 28
1
1999 - 12 - 29
2
Freq: D, dtype: int64

s['1999-12-28':'1999-12-29']
1999 - 12 - 28
1
1999 - 12 - 29
2
Freq: D, dtype: int64


# .drop(0)
# .drop([1,2,3])
# .reset_index(drop=True)
# .replace({0:'setosa', 1:'virginica'})
# .sample(n=5, replace=False)
# .sample(frac=0.50, replace=True)
# .head(n=5)
# .tail(n=5)
# .first('W')
# .last('W')
# .nunique()
# .unique()
# .drop_duplicates()
# .mean()
# .median()
# .sum()
# .prod()
# .plot()
# .fillna()
# .ffill()
# .bfill()
# .dropna()
# .interpolate()


# %% Mapping

# .map()  # nie można ustawiać parametrów; ale może brać jeszcze dict
# .apply()  # można podawać dodatkowe parametry do funkcji

# .map() - działa tylko na Series
# .apply() - działa na Series i DataFrame
# .applymap() - działa tylko na DataFrame


# argumentem jest
# - funkcja
# - dict (musi być pokrycie wszystkich wartości inaczej będzie NaN)

def my_function(x):
    return x ** 2


s.map(my_function)
s.map({0: 'setosa', 1: 'virginica'})
s.map(lambda x: x ** 2)

PLEN = {'ą': 'a', 'ć': 'c', 'ę': 'e',
        'ł': 'l', 'ń': 'n', 'ó': 'o',
        'ś': 's', 'ż': 'z', 'ź': 'z'}

data = list('zażółć gęślą jaźń')
s = pd.Series(data).map(lambda x: PLEN.get(x,x))


def remove_accent_chars(letter):
    return PLEN.get(letter, letter)

s.map(remove_accent_chars)
