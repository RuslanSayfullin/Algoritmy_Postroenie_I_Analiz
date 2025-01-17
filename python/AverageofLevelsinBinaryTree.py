"""
Учитывая корень бинарного дерева, верните среднее значение узлов на каждом уровне в виде массива. 
Принимаются ответы в пределах 10-5 от фактического ответа.
"""

# Input: root = [3,9,20, None, None,15,7]
# Output: [3.00000,14.50000,11.00000]

from collections import deque

def averageOfLevels(root):
    result = []
    queue = deque([root])
    
    while queue:
        level_sum, level_count = 0, len(queue)
        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_count)
    
    return result

if __name__ == "__main__":
    result = averageOfLevels(root = [3,9,20, None, None,15,7])
    print(result)