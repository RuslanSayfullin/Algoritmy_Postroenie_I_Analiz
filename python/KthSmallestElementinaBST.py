# Дан корень бинарного дерева поиска и целое число k. Верните k-ое по величине значение (нумерация с 1) среди всех значений узлов в дереве.

"""
Input: root = [3,1,4,null,2], k = 1
Output: 1
"""


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right



if __name__ == "__main__":
    example = Solution()
    result = example. thSmallest(root = [3,1,4,null,2], k = 1)
    print(result)