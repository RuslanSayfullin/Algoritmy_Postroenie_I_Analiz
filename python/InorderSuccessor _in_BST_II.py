"""
Дан узел в двоичном дереве поиска, верните его последующего (in-order successor) в этом дереве. Если у узла нет последующего, верните null.
"""

# Input: tree = [5,3,6,2,4,null,null,1], Node = 6
# Output: null

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def inorderSuccessor(self, x: 'Node') -> 'Node':
        if x.right:
            x = x.right
            while x.left:
                x = x.left
            return x

        while x.parent and x == x.parent.right:
            x = x.parent
        return x.parent
    
if __name__ == "__main__":
    example = Solution()
    result = example.inorderSuccessor(tree = [5,3,6,2,4,None,None,1], Node = 6)
    print(result)