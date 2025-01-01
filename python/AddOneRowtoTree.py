# Учитывая корень бинарного дерева и два целых числа val и depth, добавьте ряд узлов со значением val на заданную глубину depth.

"""
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root, val, depth):
    if depth == 1:
        return TreeNode(val, left=root)
    
    queue = [root]
    current_depth = 1
    
    while queue:
        if current_depth == depth - 1:
            for node in queue:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            break
        
        current_depth += 1
        next_queue = []
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    
    return root


if __name__ == "__main__":
    result = addOneRow(root = [4,2,6,3,1,5], val = 1, depth = 2)
    print(result)