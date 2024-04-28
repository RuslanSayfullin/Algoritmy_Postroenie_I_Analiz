name = ['A', 'B', 'C', 'D']
sides = [3, 4, 6, 5]
colors = ['red', 'green', 'yellow', 'blue']
shapes = zip(name, sides, colors)

print(set(shapes))

for i, (n, s, c) in enumerate(zip(name, sides, colors)):
    print(i, 'Shape- ', n, ': Side ', s)
