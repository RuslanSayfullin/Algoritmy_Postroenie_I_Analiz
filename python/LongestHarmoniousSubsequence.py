# Мы определяем гармоничный массив как массив, в котором разница между его максимальным и минимальным значением составляет ровно 1.
# Дан целочисленный массив nums, верните длину его самой длинной гармоничной подпоследовательности среди всех возможных подпоследовательностей.
# Подпоследовательность массива - это последовательность, которую можно получить из массива, удалив некоторые или никакие элементы, не изменяя порядок оставшихся элементов.

"""
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
"""

from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        res = 0
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])
            if num - 1 in count:
                res = max(res, count[num] + count[num - 1])
        
        return res

if __name__ == "__main__":
    example = Solution()
    result = example.findLHS(nums = [1,3,2,2,5,2,3,7])
    print(result)