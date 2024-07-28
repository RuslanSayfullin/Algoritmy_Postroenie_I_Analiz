from collections import deque

x = deque([1, 2, 3])
print(x)
x.append(4)
print(x)
x.appendleft(0)
print(x)
x.pop()
print(x)
x.popleft()
print(x)
