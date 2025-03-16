"""
Перед вами замок с 4 круглыми колесами. Каждое колесо имеет 10 слотов: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
Колеса могут свободно вращаться и оборачиваться: например, мы можем повернуть "9" так, чтобы получился "0", или "0" так, чтобы получился "9". 
Каждый ход состоит из поворота одного колеса на один слот. Изначально замок начинается с '0000', строки, представляющей состояние 4 колес. 
Вам дан список тупиков, то есть если замок отобразит любой из этих кодов, колеса замка перестанут вращаться, и вы не сможете его открыть. 
Учитывая цель, представляющую значение колес, которое позволит отпереть замок, верните минимальное общее количество оборотов, 
необходимое для открытия замка, или -1, если это невозможно.
"""

# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6

from collections import deque

def openLock(deadends, target):
    def neighbors(node):
        for i in range(4):
            x = int(node[i])
            for d in (-1, 1):
                y = (x + d) % 10
                yield node[:i] + str(y) + node[i+1:]

    dead = set(deadends)
    queue = deque([('0000', 0)])
    visited = {'0000'}
    
    while queue:
        node, steps = queue.popleft()
        if node == target:
            return steps
        if node in dead:
            continue
        for neighbor in neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    
    return -1

if __name__ == "__main__":
    example = openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202")
    print(example)