# Дан бинарный массив nums, верните максимальное количество последовательных единиц в массиве.

"""
Input: nums = [1,1,0,1,1,1]
Output: 3
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        return max(maxCount, count)

if __name__ == "__main__":
    example = Solution()
    result = example.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1])
    print(result)