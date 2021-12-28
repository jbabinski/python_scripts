import numpy as np


# pd.DataFrame == list[pd.Series] + dodatki
# pd.Series == np.array + dodatki


# pandas -> 0 - 5GB do nawet 15 GB (trochę mniej niż połowa RAM)
# pandas + chunksize -> 50 GB
# dask -> 250 ~ 500 GB
# pyspark


# %% słownictwo

# ufunc, universal function

data = 1
np.sin(data)
# 0.8414709848078965

data = np.array([1, 2, 3])
np.sin(data)
# array([0.84147098, 0.90929743, 0.14112001])

# vectorized operations
data = np.array([1, 2, 3])
data * 2

# broadcasting
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[1, 2],
              [3, 4],
              [5, 6]])

a @ b  # matmul
# array([[22, 28],
#        [49, 64]])


# axis
# - w której osi prowadzimy operacje

# scalar - 0d
x = 1

# vector - 1d
x = [1, 2, 3]

# matrix - 2d
x = [[1, 2, 3],
     [4, 5, 6]]

# tensor - 3d
x = [[[1, 2, 3],
      [4, 5, 6]],

     [[1, 2, 3],
      [4, 5, 6]]]

# ndarray - nd
x = [[[[1, 2, 3],
       [4, 5, 6]],

      [[1, 2, 3],
       [4, 5, 6]]],

     [[[1, 2, 3],
       [4, 5, 6]],

      [[1, 2, 3],
       [4, 5, 6]]]]

a = np.array([1, 2, 3])
type(a)
# <class 'numpy.ndarray'>
n = 0, 1, 2, 3, 4, ...

# %% attributes

a = np.array([1, 2, 3])

a.data
# <memory at 0x122407d00>

a.itemsize  # ile pamięci (w bajtach) zajmuje jeden element array
8

len(a)
3
a.size
3

len(a) == a.size

a.ndim
1

# %% shape

# shape informuje nas o:
# - kolumny
# - wiersze
# - głębokość
# - czas
# - inne...

# niekoniecznie w tej kolejności
# kolejność zależy od liczby wymiarów naszego ndarray
# axis to będzie index w shape
a = np.array([1, 2, 3])
a.shape
(3,)  # kolumny
# a.shape[0] -> axis=0 -> kolumnach

b = np.array([[1, 2, 3],
              [4, 5, 6]])
b.shape
(2, 3)  # wiersze, kolumny
# a.shape[0] -> axis=0 -> wiersze
# a.shape[1] -> axis=1 -> kolumnach
# a.shape[-1] -> axis=-1 -> kolumnach


c = np.array([[[1, 2, 3],
               [4, 5, 6]],
              [[1, 2, 3],
               [4, 5, 6]]])
c.shape
(2, 2, 3)  # głębokość, wiersze, kolumny
# a.shape[0] -> axis=0 -> głębokość
# a.shape[1] -> axis=1 -> wiersze
# a.shape[2] -> axis=2 -> kolumny
# a.shape[-1] -> axis=-1 -> kolumny
# a.shape[-2] -> axis=-2 -> wiersze
# a.shape[-3] -> axis=-3 -> głębokość


c.sort(axis=2)

# shape, attrs
# type, itemsize
# getitem
# slice
# index
# axis, newaxis


# %% create

a = np.array([1, 2, 3])
b = np.arange(0, 10, 2)
c = np.linspace(0, 10, 100)
d = np.zeros(shape=(2, 3))
e = np.ones(shape=(2, 3))
f = np.empty(shape=(2, 3))  # śmieci z pamięci
g = np.zeros_like(b)
h = np.ones_like(b)
i = np.empty_like(b)
j = np.identity(4)

# %% reshape

# pozwala na zmianę kształtu
# tak by długość razy szerokość dawały .size

np.arange(0, 10).reshape(2, 5)
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])

np.arange(0, 10).reshape(5, 2)


# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])


# %%

# numba - kompilator dla obliczeń numerycznych
# cython - transpiler python do c

@numba.jit(numba.int32)
def factorial(n):
    """
    n! = n * (n-1)!, = 1 gdy n=0
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


# %%

# kopiowanie przez referencje
# kopiowanie przez kopiowanie (deep copy)

a.append(99)
a
# [1, 2, 3, 99]
b
# [1, 2, 3, 99]
c
# [1, 2, 3]


a = np.array([1, 2, 3])
b = a
c = a.copy()
a[0] = 99
a
array([99, 2, 3])
b
array([99, 2, 3])
c
array([1, 2, 3])

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
a
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
a.flatten()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a.ravel()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.flatten()
c = a.ravel()
a[0, 0] = 99
b
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
c
array([99, 2, 3, 4, 5, 6, 7, 8, 9])

# %% typy

# 1 bit = 0,1
# 2 bit = 00,01,10,11
# 3 bit = 000,001,010,011,100,110,111

# %% indeksacja

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

a[0]
array([1, 2, 3])
a[1]
array([4, 5, 6])
a[2]
array([7, 8, 9])
a[-1]
array([7, 8, 9])
a[-2]
array([4, 5, 6])
a[-3]
array([1, 2, 3])
a[-4]
IndexError: index - 4 is out
of
bounds
for axis 0 with size 3
a[3]
IndexError: index
3 is out
of
bounds
for axis 0 with size 3

a[0][0]
1
a[0][1]
2
a[0][2]
3

a[:]  # daj mi wszystkie wiersze
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

a[:, 0]  # kolumna pierwsza
array([1, 4, 7])
a[:, 1]
array([2, 5, 8])
a[:, 2]
array([3, 6, 9])

a[[0, 1, 2]]
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

a[[0, 2]]
array([[1, 2, 3],
       [7, 8, 9]])

# z wierszy 0 i 2 wybierz kolumnę pierwszą
a[[0, 2], 0]
array([1, 7])

a[[0, 2], 1]
array([2, 8])

a[[0, 2], 2]
array([3, 9])

# %% indeksy

# indeksy:
# - int
# - list[int]
# - slice
# - list[bool]

# przy indeksach bool
# zwraca wiersze, dla których jest true
a[[True, False, True]]
array([[1, 2, 3],
       [7, 8, 9]])

# możemy zastosować indeksy bool
# oraz selekcję kolumn po int
a[[True, False, True], 1]
array([2, 8])

a
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

a > 5
array([[False, False, False],
       [False, False, True],
       [True, True, True]])

a[a > 5]
# array([6, 7, 8, 9])

# & and
a[(a > 5) & (a % 2 == 0)]
# array([6, 8])

# | or
a[(a > 5) | (a % 2 == 0)]
# array([2, 4, 6, 7, 8, 9])

# ~ zaprzeczenie
a[(a > 5) & ~(a % 2 == 0)]
# array([7, 9])


a[(a > 5) & ~(a % 2 == 0)]
# array([7, 9])

query = (a > 5) & ~(a % 2 == 0)
a[query]
# array([7, 9])

q1 = (a > 5)
q2 = ~(a % 2 == 0)
a[q1 & q2]
# array([7, 9])


q1 = a > 5
q2 = a % 2 == 0
a[q1 & ~q2]
# array([7, 9])


# %% slice

# def slice(start=0, stop=len(data), step=1)
# data[::step]
# data[start:]
# data[:stop]
# data[start:stop]
# data[start::step]
# data[:stop:step]
# data[start:stop]
# data[start:stop:step]

a[1:2]
array([[4, 5, 6]])
a[1:3]
array([[4, 5, 6],
       [7, 8, 9]])
a[1:3, 2]
array([6, 9])
a[1:3, 0]
array([4, 7])
a[1:3, 1]
array([5, 8])
a[1:3, [0, 1]]
array([[4, 5],
       [7, 8]])
a[1:3, 0:2]
array([[4, 5],
       [7, 8]])

a[::2, ::-1]
array([[3, 2, 1],
       [9, 8, 7]])
a[1::2, ::-1]
array([[6, 5, 4]])
a[1::2, 3::-1]
array([[6, 5, 4]])
a[1::2, 2::-1]
array([[6, 5, 4]])
a[1::2, 1::-1]
array([[5, 4]])

# %% sort

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

x.sort()


# %% random

# - liczby pseudolosowe
#   (algorytm ich generowania jest trudny do kolizji,
#   ale nie niemożliwy - da się to zrobić teoretycznie)
# - generator liczb pseudolosowych
# - seed - ziarno losowości

# 6 6 0 4 8 7
np.random.seed(0)

# pseudolosowy int
np.random.randint(0,10)
np.random.randint(0,10, size=100)
np.random.randint(0,10, size=(10,10))

# pseudolosowy float
np.random.random()
np.random.random(size=100)
np.random.random(size=(10,10))

# continuous uniform
np.random.randn()

# normal (gaussian)
np.random.normal()
np.random.normal(loc=1, scale=0.1)
np.random.normal(loc=1, scale=0.1, size=100)
np.random.normal(loc=1, scale=0.1, size=(10,10))

# poisson
np.random.poisson(lam=4, size=100)
np.random.poisson(lam=4, size=(10,10))

#
np.random.choice()
np.random.shuffle()
np.random.random_sample()
