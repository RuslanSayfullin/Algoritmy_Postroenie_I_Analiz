def has_duplicates(lst):
    print(len(lst) != len(set(lst)))

x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 5]

has_duplicates(x)
has_duplicates(y)
