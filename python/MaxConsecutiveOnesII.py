"""
Дан бинарный массив nums, верните максимальное количество последовательных единиц в массиве, если можно перевернуть не более одного нуля.
"""

# Input: nums = [1,0,1,1,0]
# Output: 4

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longestSequence = 0
        for left in range(len(nums)):
            numZeroes = 0
            for right in range(left, len(nums)):
                if nums[right] == 0:
                    numZeroes += 1
                if numZeroes <= 1:
                    longestSequence = max(longestSequence, right - left + 1)
        return longestSequence
    
if __name__ == "__main__":
    example = Solution()
    result = example.findMaxConsecutiveOnes(nums = [1,0,1,1,0])
    print(result)