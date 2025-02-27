"""
Дано корень бинарного дерева, вернуть наиболее часто встречающуюся сумму поддерева. 
Если есть несколько таких значений, вернуть все значения с наибольшей частотой в любом порядке.
Сумма поддерева узла определяется как сумма всех значений узлов, образованных поддеревом, укорененным в этом узле (включая сам узел).
"""

# Input: root = [5,2,-3]
# Output: [2,-3,4]

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        from collections import defaultdict
        
        sumFreq = defaultdict(int)
        maxFreq = 0
        
        def subtreeSum(node):
            nonlocal maxFreq
            if not node:
                return 0
            leftSum = subtreeSum(node.left)
            rightSum = subtreeSum(node.right)
            currSum = node.val + leftSum + rightSum
            sumFreq[currSum] += 1
            maxFreq = max(maxFreq, sumFreq[currSum])
            return currSum
        
        subtreeSum(root)
        return [s for s in sumFreq if sumFreq[s] == maxFreq]
    
if __name__ == "__main__":
    example = Solution()
    result = example.findFrequentTreeSum(score = [5,4,3,2,1])
    print(result)