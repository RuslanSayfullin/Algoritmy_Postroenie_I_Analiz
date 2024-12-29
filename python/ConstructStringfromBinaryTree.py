# создать строковое представление дерева, следуя определенным правилам форматирования

"""
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
"""

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(t):
            if not t:
                return ""
            res = str(t.val)
            if not t.left and not t.right:
                return res
            res += f"({dfs(t.left)})"
            if t.right:
                res += f"({dfs(t.right)})"
            return res
        return dfs(t)


if __name__ == "__main__":
    example = Solution()
    result = example.tree2str(root = [1,2,3,4])
    print(result)