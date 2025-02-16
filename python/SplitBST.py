"""
Дан корень бинарного дерева поиска (BST) и целое число target, разделите дерево на два поддерева, где первое поддерево содержит узлы, 
которые меньше или равны значению target, а второе поддерево содержит узлы, которые больше значения target. 
Верните массив из двух корней двух поддеревьев в порядке.
"""

# Input: root = [4,2,6,1,3,5,7], target = 2
# Output: [[2,1],[4,3,6,null,null,5,7]]

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def splitBST(self, root: TreeNode, target: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        
        if root.val > target:
            left = self.splitBST(root.left, target)
            root.left = left[1]
            return [left[0], root]
        else:
            right = self.splitBST(root.right, target)
            root.right = right[0]
            return [root, right[1]]
        
if __name__ == "__main__":
    example = Solution()
    result = example.splitBST(root = [4,2,6,1,3,5,7], target = 2)
    print(result)