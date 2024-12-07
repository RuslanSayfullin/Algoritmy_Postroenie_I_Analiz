# Дан корень N-арного дерева, верните значения его узлов в порядке предварительного (preorder) обхода.
# Сериализация ввода N-арного дерева представлена в их обходе уровнями. Каждая группа детей разделена значением null.

"""
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(reversed(node.children))
        
        return output

if __name__ == "__main__":
    example = Solution()
    result = example.preorder(root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14])
    print(result)