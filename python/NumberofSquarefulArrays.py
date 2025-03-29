"""
Массив является квадратным, если сумма каждой пары соседних элементов является совершенным квадратом. 
Если задан целочисленный массив nums, верните количество перестановок nums, которые являются квадратными. 
Две перестановки perm1 и perm2 различны, если существует некоторый индекс i такой, что perm1[i] != perm2[i].
"""

# Input: nums = [1,17,8]
# Output: 2

from typing import List
from itertools import permutations
import math

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def isPerfectSquare(x):
            return int(math.isqrt(x)) ** 2 == x
        
        def isSquareful(perm):
            for i in range(len(perm) - 1):
                if not isPerfectSquare(perm[i] + perm[i + 1]):
                    return False
            return True
        
        perms = set(permutations(nums))
        count = sum(1 for perm in perms if isSquareful(perm))
        return count

if __name__ == "__main__":
    example = Solution()
    result = example.numSquarefulPerms(nums = [1,17,8])
    print(result)