"""
Дано корневое дерево двоичного поиска и нижняя и верхняя границы как low и high.
Обрежьте дерево так, чтобы все его элементы лежали в диапазоне [low, high]. 
Обрезка дерева не должна изменять относительную структуру элементов, 
которые останутся в дереве (то есть любой потомок узла должен оставаться потомком). Можно доказать, что существует единственный ответ.

Верните корень обрезанного дерева двоичного поиска. 
Обратите внимание, что корень может измениться в зависимости от заданных границ.
"""

# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]

class TreeNode:
    def __init__(self, val=0, lefn=None, rigth=None):
        self.val = val
        self.left = left
        self.rigth = rigth

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        # проверяем налаличие экземпляра дерева
        if not root:
            return None
        if root.val > high:
            # Если root.val > high, то обрезанное двоичное дерево должно находиться слева от узла.
            return self.trimBST(root.left, low, high)
        if root.val < low:
            # Если root.val < low, то обрезанное двоичное дерево должно находиться справа от узла.
            return self.trimBST(root.rigth, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

if __name__ == "__main__":
    example = Solution()
    result = example.trimBST(root = [1,0,2], low = 1, high = 2)
    print(result)
