# Дан отсортированный массив целых чисел nums и целое число n. Добавьте/дополните элементы в массив таким образом, чтобы любое число в диапазоне [1, n] включительно могло быть сформировано как сумма некоторых элементов массива.
# Верните минимальное количество дополнений, необходимых для этого.

"""
Input: nums = [1,3], n = 6
Output: 1
"""

from typing import List 

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, i, miss = 0, 0, 1
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches



if __name__ == "__main__":
    example = Solution()
    result = example.minPatches(nums = [1,3], n = 6)
    print(result)