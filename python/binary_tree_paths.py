# Дано корневое дерево, верните все пути от корня до листа в любом порядке.
# Лист — это узел без детей.

"""
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""

from typing import List

class Solution:
    def construct_paths(self, root: TreeNode, path: str, paths: List[str]):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += "->"
                self.construct_paths(root.left, path, paths)
                self.construct_paths(root.right, path, paths)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.construct_paths(root, "", paths)
        return paths

if __name__ == "__main__":
    example = Solution()
    result = example.binaryTreePaths(root = [1,2,3,null,5])
    print(result)       