"""
Вам дан целочисленный массив nums без дубликатов. 
Из nums можно рекурсивно построить максимальное двоичное дерево, 
используя следующий алгоритм: создайте корневой узел, значение которого равно максимальному значению в nums. 
Рекурсивно постройте левое поддерево по префиксу подмассива слева от максимального значения. 
Рекурсивно постройте правое поддерево по суффиксу подмассива справа от максимального значения. 
Верните максимальное двоичное дерево, построенное из nums.
"""

# Input: root = [5,3,6,2,4,None,7], k = 9
# Output: true

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    def find(node, k, seen):
        if not node:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return find(node.left, k, seen) or find(node.right, k, seen)
    
    return find(root, k, set())


if __name__ == "__main__":
    result = findTarget(root = [5,3,6,2,4,None,7], k = 9)
    print(result)