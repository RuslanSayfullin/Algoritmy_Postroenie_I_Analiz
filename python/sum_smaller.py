# Дан массив из n целых чисел nums и целое число target. Найдите количество троек индексов i, j, k, удовлетворяющих условию 0 <= i < j < k < n и nums[i] + nums[j] + nums[k] < target.

"""
Input: nums = [-2,0,1,3], target = 2
Output: 2
"""

from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum_count = 0
        for i in range(len(nums) - 2):
            sum_count += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return sum_count

    def twoSumSmaller(self, nums: List[int], startIndex: int, target: int) -> int:
        sum_count = 0
        for i in range(startIndex, len(nums) - 1):
            j = self.binarySearch(nums, i, target - nums[i])
            sum_count += j - i
        return sum_count

    def binarySearch(self, nums: List[int], startIndex: int, target: int) -> int:
        left, right = startIndex, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    example = Solution()
    result = example.threeSumSmaller(nums = [-2,0,1,3], target = 2)
    print(result)