# Дан массив целых чисел nums. Найдите подмассив, 
# который имеет наибольший произведение, и верните это произведение.

"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(len(nums)):
                accu *= nums[j]
                result = max(result, accu)
            
        return result

if __name__ == "__main__":
    example = Solution
    result = Solution.maxProduct(example, nums = [2,3,-2,4])
    print(result)