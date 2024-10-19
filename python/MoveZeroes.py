# Дан целочисленный массив nums. Переместите все нули в конец массива, сохраняя относительный порядок ненулевых элементов.
# Обратите внимание, что вы должны сделать это на месте, не создавая копию массива.

"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]"""


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[lastNonZeroFoundAt], nums[cur] = nums[cur], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
        
        return nums


if __name__ == "__main__":
    example = Solution()
    result = example.moveZeroes(nums = [0,1,0,3,12])
    print(result)