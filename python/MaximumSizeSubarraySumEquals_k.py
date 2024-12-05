# Дан целочисленный массив nums и целое число k. Верните максимальную длину подмассива, сумма которого равна k. Если такого подмассива не существует, верните 0.


"""
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
"""

from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        longestSubarray = 0
        indices = {}
        
        for i, num in enumerate(nums):
            prefixSum += num
            
            if prefixSum == k:
                longestSubarray = i + 1
            if prefixSum - k in indices:
                longestSubarray = max(longestSubarray, i - indices[prefixSum - k])
            if prefixSum not in indices:
                indices[prefixSum] = i
        
        return longestSubarray

if __name__ == "__main__":
    example = Solution()
    result = example.maxSubArrayLen(nums = [1,-1,5,-2,3], k = 3)
    print(result)