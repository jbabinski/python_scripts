import pandas as pd


pd.DataFrame([
    {'a': 1, 'b': None, 'c': 1},  # row 1
    {'a': 2, 'b': None, 'c': 1},  # row 2
])

pd.DataFrame({
    'A': ['a', 'b', 'c'],  # column 1
    'B': [1.0, 2.0, 3.0],  # column 2
    'C': [1, 2, 3],        # column 3
})


df.info()
df.info(memory_usage='deep')
df.convert_dtypes()


df.values
df.index
df.columns


# RangeIndex - dolny włącznie, górny rozłącznie
# Int64Index - dolny i górny włącznie
# Float64Index - dolny i górny włącznie
# ObjectIndex - dolny i górny włącznie
# DatetimeIndex - dolny i górny włącznie

# MultiIndex

df.query('Morning < 0 and Midnight < 0')
df.query('Noon > @mean')

# zwraca scala (wartość w komórce)
df.at[]
df.iat[]

# zwraca nam wiersze
df.loc[]
df.iloc[]

#%%

# IEEE 754
# standard zapisu float w systemach operacyjnych

"""
>>> 0.1 + 0.2  # doctest: +ELLIPSIS
0.3...
"""

# %% Slices


# int, list[int], slice(int, int, int)
# str, list[str], slice(str, str, int)
# list[bool]
# callable


import pandas as pd
import numpy as np
np.random.seed(0)

df = pd.DataFrame(
    columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
    index = pd.date_range('1999-12-30', periods=7),
    data = np.random.randn(7, 4))

df


df.loc[:, 'Morning']
df.loc[:, ['Morning','Noon']]
df.loc[:, 'Morning':'Evening']
df.loc[:, 'Morning':'Evening':2]

df.iloc[:, 0:3:2]

df.loc['2000-01-01']
df.loc[['2000-01-01','2000-01-05']]
df.loc['2000-01-01':'2000-01-05']
df.loc['2000-01-01':'2000-01-05':2]

df.iloc[0:6:2]

len(df)
7


df.loc[ [True, False, True, False, True, True, False] ]


df['Morning'] < 0
# 1999-12-30    False
# 1999-12-31    False
# 2000-01-01     True
# 2000-01-02    False
# 2000-01-03    False
# 2000-01-04     True
# 2000-01-05    False
# Freq: D, Name: Morning, dtype: bool


df[ df['Morning'] < 0 ]
#              Morning      Noon   Evening  Midnight
# 2000-01-01 -0.103219  0.410599  0.144044  1.454274
# 2000-01-04 -2.552990  0.653619  0.864436 -0.742165


df[ [False, False, True, False, False, True, False] ]
#              Morning      Noon   Evening  Midnight
# 2000-01-01 -0.103219  0.410599  0.144044  1.454274
# 2000-01-04 -2.552990  0.653619  0.864436 -0.742165



q1 = df['Morning'] < 0
q2 = df['Midnight'] > 0
q1 & q2
# 1999-12-30    False
# 1999-12-31    False
# 2000-01-01     True
# 2000-01-02    False
# 2000-01-03    False
# 2000-01-04    False
# 2000-01-05    False
# Freq: D, dtype: bool

df[ q1 & q2 ]
#              Morning      Noon   Evening  Midnight
# 2000-01-01 -0.103219  0.410599  0.144044  1.454274


#





# %%

# projekcja
# selekcja
# porządkowanie

"""
SELECT
    Morning,
    Noon,
    Evening,
    Midnight
FROM
    temperatures
WHERE
    Morning < 0 AND Midnight  > 0
ORDER BY
    Morning DESC 
"""

q1 = temperatures['Morning'] < 0
q2 = temperatures['Midnight'] > 0
temperatures[ q1 & q2 ]


temperatures[ \
    (temperatures['Morning'] < 0) \
  & (temperatures['Midnight'] > 0) \
]


#%%

# Pandas przed 1.0 (i do teraz)
np.nan


# Pandas od 1.0
pd.NA
pd.NaT

pd.read_csv()


df.dropna(how='any', axis='columns')

df.sort_values(ascending=False)
df.sort_values(by=['Morning', 'Evening'], ascending=False)


# Sortowanie wierszy (zmień kolejność wierszy)
df.sort_values(by=['Morning', 'Evening'], ascending=False, axis='rows')

# Sortowanie kolumn (zmień kolejność kolumn)
df.sort_values(by=['1999-12-31'], ascending=False, axis='columns')


# %%

df.describe()

df.count()
df.value_counts()
df.nunique()
df.sum()
df.cumsum()
df.prod()
df.cumprod()

df.min()
df.max()
df.cummin()
df.cummax()

df.idxmax()
df.idxmin()

df.median()
df.mean()
df.std()
df.var()
df.mode()

df.std()
df.var()
df.cov()

df.rolling(window=3).median()
df.rolling(window=3).mean()

df.resample('W').median()
df.resample('5T').median()

df.sem()
df.skew()
df.kurt()
df.corr()

df.quantile(.25)
df.quantile(.33)
df.quantile([.25, .50, .75])



# - 'line' : line plot (default)
# - 'bar' : vertical bar plot
# - 'barh' : horizontal bar plot
# - 'hist' : histogram
# - 'box' : boxplot
# - 'kde' : Kernel Density Estimation plot
# - 'density' : same as 'kde'
# - 'area' : area plot
# - 'pie' : pie plot
# - 'scatter' : scatter plot (DataFrame only)
# - 'hexbin' : hexbin plot (DataFrame only)


# %% mapping

df['Midnight'].map(round)
df['Midnight'].apply(round, ndigits=2)
df['Midnight'].round(2)

df.apply(round, ndigits=2)

df.applymap(round)
df.applymap(round, ndigits=2)

x.strftime('%Y-%m-%d %H:%M:%S.%f %Z')
x.strftime('%Y-%m-%d %H:%M:%S.%f')

DATA = 'https://python.astrotech.io/_static/phones-pl.csv'

df = pd.read_csv(DATA, parse_dates=['datetime'])

df['datetime'].dt.strftime('%A %d, %m %Y')
df['datetime'].dt.strftime('%A %d, %B %Y')
df['datetime'].dt.date
df['datetime'].dt.time

df['time'] = df['datetime'].dt.time
df['date'] = df['datetime'].dt.date

df['period']
df['period'].str.split('-')
df['period'].str.split('-', expand=True)
df[ ['year','month'] ] = df['period'].str.split('-', expand=True)
MONTHS_PL = ['styczeń', 'luty', 'marzec', 'kwiecień',
             'maj', 'czerwiec', 'lipiec', 'sierpień',
             'wrzesień', 'październik', 'listopad', 'grudzień']
df['month']
'03' == 3
dict(enumerate(MONTHS_PL, start=1))
months = dict(enumerate(MONTHS_PL, start=1))
df['month'].astype(int)
df['month'].astype(int).replace(months)
df['months'] = df['month'].astype(int).replace(months)
df['month'] = df['month'].astype(int)
df.convert_dtypes()
df = df.convert_dtypes()
df
df.info()
df['year'] = df['year'].astype(int)


df.set_index('datetime', inplace=True)


# %% groupby

df.groupby('period')
df.groupby('period').count()
df.groupby('period')['item'].count()

df.groupby('period')['item'].count()
# period
# 1999-11    230
# 1999-12    157
# 2000-01    205
# 2000-02    137
# 2000-03    101
# Name: item, dtype: int64

df.groupby('period')['item'].value_counts()
# period   item
# 1999-11  call    107
#          sms      94
#          data     29
# 1999-12  call     79
#          sms      48
#          data     30
# 2000-01  call     88
#          sms      86
#          data     31
# 2000-02  call     67
#          sms      39
#          data     31
# 2000-03  call     47
#          data     29
#          sms      25
# Name: item, dtype: int64

df.loc['2000':'2000'].groupby('period')['item'].count()
# period
# 2000-01     88
# 2000-02    137
# 2000-03    101
# Name: item, dtype: int64


df.loc['2000-02-01':'2000-02-29'].groupby('period')['item'].count()
# period
# 2000-02    56
# 2000-03    62
# Name: item, dtype: int64

df.loc['2000-02-01':'2000-02-29'].groupby(['period','item'])['type'].count()
# period   item
# 2000-02  call    23
#          data    12
#          sms     21
# 2000-03  call    34
#          data    16
#          sms     12
# Name: type, dtype: int64


luty2000 = df.loc['2000-02-01':'2000-02-29']

luty2000.groupby(['period','item']).count()
#               id  network  type  duration  time  date  year  month  months
# period  item
# 2000-02 call  23       23    23        23    23    23    23     23      23
#         data  12       12    12        12    12    12    12     12      12
#         sms   21       21    21        21    21    21    21     21      21
# 2000-03 call  34       34    34        34    34    34    34     34      34
#         data  16       16    16        16    16    16    16     16      16
#         sms   12       12    12        12    12    12    12     12      12

luty2000.groupby(['period','item']).first()
#                id   network      type  duration      time        date  year  month  months
# period  item
# 2000-02 call  674  landline  landline     103.0  13:33:00  2000-02-01  2000      2    luty
#         data  673      Plus      data      34.5  06:58:00  2000-02-01  2000      2    luty
#         sms   678      Plus    mobile       1.0  17:35:00  2000-02-02  2000      2    luty
# 2000-03 call  729  landline  landline      69.0  20:15:00  2000-02-12  2000      3  marzec
#         data  731    Orange      data      34.5  06:58:00  2000-02-13  2000      3  marzec
#         sms   747    Orange    mobile       1.0  18:46:00  2000-02-19  2000      3  marzec


luty2000.groupby(['period','item']).last()
#                id   network    type  duration      time        date  year  month  months
# period  item
# 2000-02 call  720  T-Mobile  mobile      89.0  17:54:00  2000-02-09  2000      2    luty
#         data  728    Orange    data      34.5  06:58:00  2000-02-12  2000      2    luty
#         sms   726    Orange  mobile       1.0  21:40:00  2000-02-10  2000      2    luty
# 2000-03 call  788  T-Mobile  mobile     357.0  21:25:00  2000-02-28  2000      3  marzec
#         data  779  T-Mobile    data      34.5  06:58:00  2000-02-28  2000      3  marzec
#         sms   790  T-Mobile  mobile       1.0  22:39:00  2000-02-28  2000      3  marzec


df.groupby(['period', 'item']).size()
period   item
1999-11  call    107
         data     29
         sms      94
1999-12  call     79
         data     30
         sms      48
2000-01  call     88
         data     31
         sms      86
2000-02  call     67
         data     31
         sms      39
2000-03  call     47
         data     29
         sms      25
dtype: int64
df.groupby(['period', 'item'], as_index=False).size()
     period  item  size
0   1999-11  call   107
1   1999-11  data    29
2   1999-11   sms    94
3   1999-12  call    79
4   1999-12  data    30
5   1999-12   sms    48
6   2000-01  call    88
7   2000-01  data    31
8   2000-01   sms    86
9   2000-02  call    67
10  2000-02  data    31
11  2000-02   sms    39
12  2000-03  call    47
13  2000-03  data    29
14  2000-03   sms    25

# %% aggregate

df.groupby(['period', 'item']).agg(
    duration_max=('duration', 'max'),
    duration_min=('duration', 'min'),
    duration_mean=('duration', 'mean'),
    duration_median=('duration', 'median'),
    duration_std=('duration', 'std'),
    duration_sum=('duration', 'sum'),
    days=('date', lambda x: (max(x) - min(x)).days),
)

df.describe()
#                id      duration         year       month
# count  830.000000    830.000000   830.000000  830.000000
# mean   414.500000    117.816867  1999.533735    6.260241
# std    239.744656    444.127149     0.499161    4.858900
# min      0.000000      1.000000  1999.000000    1.000000
# 25%    207.250000      1.000000  1999.000000    2.000000
# 50%    414.500000     24.500000  2000.000000    3.000000
# 75%    621.750000     55.000000  2000.000000   11.000000
# max    829.000000  10528.000000  2000.000000   12.000000



pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 50)

df.groupby(['period', 'item']).describe()
#                  id                                                             duration              ...    year          month
#               count        mean        std    min     25%    50%     75%    max    count        mean  ...     75%     max  count  mean  std   min   25%   50%   75%   max
# period  item                                                                                          ...
# 1999-11 call  107.0  102.467290  61.870729    1.0   47.50  104.0  148.50  224.0    107.0  238.757009  ...  1999.0  1999.0  107.0  11.0  0.0  11.0  11.0  11.0  11.0  11.0
#         data   29.0  100.758621  60.899598    0.0   56.00   95.0  151.00  208.0     29.0   34.500000  ...  1999.0  1999.0   29.0  11.0  0.0  11.0  11.0  11.0  11.0  11.0
#         sms    94.0  132.457447  69.828001   11.0   70.25  146.5  194.75  230.0     94.0    1.000000  ...  1999.0  1999.0   94.0  11.0  0.0  11.0  11.0  11.0  11.0  11.0
# 1999-12 call   79.0  312.974684  44.250735  232.0  276.50  303.0  352.50  388.0     79.0  171.658228  ...  1999.0  1999.0   79.0  12.0  0.0  12.0  12.0  12.0  12.0  12.0
#         data   30.0  307.533333  52.454731  228.0  256.25  322.5  349.75  378.0     30.0   34.500000  ...  1999.0  1999.0   30.0  12.0  0.0  12.0  12.0  12.0  12.0  12.0
#         sms    48.0  300.229167  42.933516  233.0  256.00  309.0  333.25  371.0     48.0    1.000000  ...  1999.0  1999.0   48.0  12.0  0.0  12.0  12.0  12.0  12.0  12.0
# 2000-01 call   88.0  489.931818  61.574699  392.0  432.50  502.5  543.25  589.0     88.0  193.977273  ...  2000.0  2000.0   88.0   1.0  0.0   1.0   1.0   1.0   1.0   1.0
#         data   31.0  472.548387  59.105464  381.0  423.00  473.0  514.00  571.0     31.0   34.500000  ...  2000.0  2000.0   31.0   1.0  0.0   1.0   1.0   1.0   1.0   1.0
#         sms    86.0  494.139535  57.235563  390.0  449.75  488.5  544.50  593.0     86.0    1.000000  ...  2000.0  2000.0   86.0   1.0  0.0   1.0   1.0   1.0   1.0   1.0
# 2000-02 call   67.0  656.641791  36.028062  595.0  629.50  656.0  686.50  720.0     67.0  215.164179  ...  2000.0  2000.0   67.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
#         data   31.0  656.774194  43.210114  577.0  623.00  655.0  687.00  728.0     31.0   34.500000  ...  2000.0  2000.0   31.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
#         sms    39.0  667.769231  43.650804  596.0  623.50  679.0  705.50  726.0     39.0    1.000000  ...  2000.0  2000.0   39.0   2.0  0.0   2.0   2.0   2.0   2.0   2.0
# 2000-03 call   47.0  773.659574  25.740576  729.0  754.00  777.0  795.50  816.0     47.0  462.276596  ...  2000.0  2000.0   47.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
#         data   29.0  779.896552  34.445967  731.0  751.00  775.0  818.00  827.0     29.0   34.500000  ...  2000.0  2000.0   29.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0
#         sms    25.0  788.000000  27.958302  747.0  765.00  794.0  813.00  829.0     25.0    1.000000  ...  2000.0  2000.0   25.0   3.0  0.0   3.0   3.0   3.0   3.0   3.0


x = df.groupby(['period', 'item']).describe()
type(x)
# <class 'pandas.core.frame.DataFrame'>



x.columns
# MultiIndex([(      'id', 'count'),
#             (      'id',  'mean'),
#             (      'id',   'std'),
#             (      'id',   'min'),
#             (      'id',   '25%'),
#             (      'id',   '50%'),
#             (      'id',   '75%'),
#             (      'id',   'max'),
#             ('duration', 'count'),
#             ('duration',  'mean'),
#             ('duration',   'std'),
#             ('duration',   'min'),
#             ('duration',   '25%'),
#             ('duration',   '50%'),
#             ('duration',   '75%'),
#             ('duration',   'max'),
#             (    'year', 'count'),
#             (    'year',  'mean'),
#             (    'year',   'std'),
#             (    'year',   'min'),
#             (    'year',   '25%'),
#             (    'year',   '50%'),
#             (    'year',   '75%'),
#             (    'year',   'max'),
#             (   'month', 'count'),
#             (   'month',  'mean'),
#             (   'month',   'std'),
#             (   'month',   'min'),
#             (   'month',   '25%'),
#             (   'month',   '50%'),
#             (   'month',   '75%'),
#             (   'month',   'max')],
#            )


x.index
# MultiIndex([('1999-11', 'call'),
#             ('1999-11', 'data'),
#             ('1999-11',  'sms'),
#             ('1999-12', 'call'),
#             ('1999-12', 'data'),
#             ('1999-12',  'sms'),
#             ('2000-01', 'call'),
#             ('2000-01', 'data'),
#             ('2000-01',  'sms'),
#             ('2000-02', 'call'),
#             ('2000-02', 'data'),
#             ('2000-02',  'sms'),
#             ('2000-03', 'call'),
#             ('2000-03', 'data'),
#             ('2000-03',  'sms')],
#            names=['period', 'item'])


['_'.join(x) for x in x.columns.ravel()]
# ['id_count', 'id_mean', 'id_std', 'id_min', 'id_25%', 'id_50%', 'id_75%', 'id_max', 'duration_count', 'duration_mean', 'duration_std', 'duration_min', 'duration_25%', 'duration_50%', 'duration_75%', 'duration_max', 'year_count', 'year_mean', 'year_std', 'year_min', 'year_25%', 'year_50%', 'year_75%', 'year_max', 'month_count', 'month_mean', 'month_std', 'month_min', 'month_25%', 'month_50%', 'month_75%', 'month_max']


x.columns.droplevel(0)
