"""
Дан неотсортированный массив целых чисел nums, верните длину самой длинной непрерывной возрастающей подпоследовательности (т.е. подмассива). 
Подпоследовательность должна быть строго возрастающей.
Непрерывная возрастающая подпоследовательность определяется двумя индексами l и r (l < r) так, что она имеет вид [nums[l], nums[l + 1], ..., 
nums[r - 1], nums[r]] и для каждого l <= i < r выполняется nums[i] < nums[i + 1].
"""

# nums = [1,3,5,4,7]
# 3

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        anchor = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans

if __name__ == "__main__":
    example = Solution()
    res = example.findLengthOfLCIS(nums = [1,3,5,4,7])
    print(res)