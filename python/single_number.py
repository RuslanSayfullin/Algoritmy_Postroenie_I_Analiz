# Дан целочисленный массив nums, в котором ровно два элемента встречаются только один раз, а все остальные элементы встречаются ровно дважды. Найдите два элемента, которые встречаются только один раз. Вы можете вернуть ответ в любом порядке.
# Вы должны написать алгоритм, который работает за линейное время и использует только постоянное дополнительное пространство.

"""
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        diff = xor & - xor
        res = [0, 0]
        for num in nums:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res

if __name__ == "__main__":
    example = Solution()
    result = example.singleNumber(nums = [1,2,1,3,2,5])
    print(result)