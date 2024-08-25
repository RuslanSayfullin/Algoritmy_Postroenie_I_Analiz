#Вам дан диапазон [lower, upper] и отсортированный массив уникальных целых чисел nums, 
# где все элементы находятся в этом диапазоне.

"""
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
"""

from typing import List

class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        n = len(nums)
        missing_ranges = []
        if n == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])
        if upper > nums[n - 1]:
            missing_ranges.append([nums[n - 1] + 1, upper])

        return missing_ranges

if __name__ == "__main__":
    example = Solution()
    result = example.findMissingRanges( nums = [-1], lower = -1, upper = -1)
    print(result)