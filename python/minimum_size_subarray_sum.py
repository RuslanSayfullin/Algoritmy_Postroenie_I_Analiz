# Дан массив положительных целых чисел nums и положительное целое число target. Верните минимальную длину подмассива, сумма которого больше или равна target. Если такого подмассива нет, верните 0.

"""
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0


if __name__ == "__main__":
    example = Solution
    result = Solution.minSubArrayLen(example, target = 7, nums = [2,3,1,2,4,3])
    print(result)