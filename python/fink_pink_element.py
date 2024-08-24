# Для массива целых чисел nums с индексацией с нуля найдите пиковый элемент и верните его индекс. 
# Если в массиве несколько пиков, верните индекс любого из пиков.
# Необходимо написать алгоритм, который работает за время O(log n).

"""
Пример:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""

from typing import List

class Solution:
    def finkPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], l: int, r: int) -> int:
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, l, mid)
        return self.search(nums, mid + 1, r)

if __name__ == "__main__":
    example = Solution()
    result = example.finkPeakElement(nums = [1,2,3,1])
    print(result)