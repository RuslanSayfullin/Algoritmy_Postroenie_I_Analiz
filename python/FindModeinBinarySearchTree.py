"""
ано корень бинарного дерева поиска (BST) с дубликатами. Необходимо вернуть все моды (т.е. самые часто встречающиеся элементы) в этом дереве.
Если в дереве более одной моды, верните их в любом порядке.
Предположим, что BST определяется следующим образом:
Левое поддерево узла содержит только узлы с ключами, меньшими или равными ключу этого узла.
Правое поддерево узла содержит только узлы с ключами, большими или равными ключу этого узла.
Оба поддерева также должны быть бинарными деревьями поиска.
"""

# Input: root = [1,None,2,2]
# Output: [2]

from typing  import List 

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        values = []
        self.dfs(root, values)
        
        max_streak = curr_streak = curr_num = 0
        ans = []
        
        for num in values:
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num
                
            if curr_streak > max_streak:
                ans = [num]
                max_streak = curr_streak
            elif curr_streak == max_streak:
                ans.append(num)
                
        return ans
    
    def dfs(self, node, values):
        if not node:
            return
        self.dfs(node.left, values)
        values.append(node.val)
        self.dfs(node.right, values)

if __name__ == "__main__":
    example = Solution()
    result = example.findMode(root = [1,None,2,2])
    print(result)