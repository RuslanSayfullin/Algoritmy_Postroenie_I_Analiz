# Дан корень двоичного дерева, верните самое левое значение в последней строке дерева.

"""
Input: root = [2,1,3]
Output: 1
"""

from typing import Optional

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = -1
        self.bottomLeftValue = 0
        self.dfs(root, 0)
        return self.bottomLeftValue

    def dfs(self, current: TreeNode, depth: int):
        if not current:
            return
        
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.bottomLeftValue = current.val

        self.dfs(current.left, depth + 1)
        self.dfs(current.right, depth + 1)
        return

if __name__ == "__main__":
    example = Solution()
    result = example.findBottomLeftValue(root = [2,1,3])
    print(result)