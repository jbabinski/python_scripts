DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

# list[tuple]: data from file (note the list[tuple] format!)
result = []
for line in DATA.splitlines():
    line = line.strip().split(',')
    result.append(tuple(line))


result = [tuple(row)
          for line in DATA.splitlines()
          if (row := line.strip().split(','))]
# Assignment expression od Python 3.8



result = [tuple(x.strip().split(','))
          for x in DATA.splitlines()]


#%%


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
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
]

all(observation > 1.0
    for row in DATA[1:]
    for observation in row
    if type(observation) in (int,float))

# złożoność kognitywna
# idiomatyczny kod
# 80% - czytamy kod
# 20% - pisze kod


all(x > 1.0 for *X,y in DATA[1:] for x in X if type(x) in (int,float))
