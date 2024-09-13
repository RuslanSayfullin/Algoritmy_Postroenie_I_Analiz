# Дан массив уникальных целых чисел preorder. Верните true, если это правильная последовательность обхода в порядке предварительного (preorder) обхода для бинарного дерева поиска.

"""
Input: preorder = [5,2,1,3,6]
Output: true
"""

from typing import List

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        minLimit = float('-inf')
        stack = []
        
        for num in preorder:
            while stack and stack[-1] < num:
                minLimit = stack.pop()
            
            if num <= minLimit:
                return False
            
            stack.append(num)
        
        return True


if __name__ == "__main__":
    example = Solution()
    result = example.verifyPreorder(preorder = [5,2,1,3,6])
    print(result)