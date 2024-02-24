from itertools import groupby

data = ['a', 'b', 'c', 'a', 'b']

for key, value in groupby(data):
    print(key, list(value))
