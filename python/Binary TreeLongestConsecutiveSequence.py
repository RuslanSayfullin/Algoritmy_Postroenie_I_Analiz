# Дан корень бинарного дерева, верните длину самого длинного пути последовательных значений.
# Путь последовательных значений — это путь, где значения увеличиваются на единицу вдоль пути.

"""
Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
"""

from typing import Optional

class Solution:
    def __init__(self):
        self.maxLength = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, None, 0)
        return self.maxLength

    def dfs(self, node: Optional[TreeNode], parent: Optional[TreeNode], length: int) -> None:
        if not node:
            return
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        self.maxLength = max(self.maxLength, length)
        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)

if __name__ == "__main__":
    example = Solution()
    result = example.longestConsecutive(root = [1,null,3,2,4,null,null,null,5])
    print(result)