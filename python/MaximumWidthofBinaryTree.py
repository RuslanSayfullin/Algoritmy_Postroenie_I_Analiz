"""
Дан корень бинарного дерева, верните максимальную ширину данного дерева.
Максимальная ширина дерева - это максимальная ширина среди всех уровней.
"""

# Input: root = [1,3,2,5,3,null,9]
# Output: 4

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, rigth=None):
        self.val = val
        self.left = left
        self.rigth = rigth

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([root, 0])

        while queue:
            level_length = len(queue)
            _, first_pos = queue[0]
            for i in range(level_length):
                node, pos = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.rigth:
                    queue.append((node.rigth, 2 * pos + 1))

            max_width = max(max_width, pos - first_pos + 1)

        return max_width
    
    
if __name__ == "__main__":
    example = Solution()
    result = example.widthOfBinaryTree(root = [1,3,2,5,3,None,9])
    print(result)
