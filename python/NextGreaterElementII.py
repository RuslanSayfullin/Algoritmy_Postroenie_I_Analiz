"""
Дан циклический массив целых чисел nums (т.е. следующий элемент после nums[nums.length - 1] это nums[0]), верните следующее большее число для каждого элемента в nums.
Следующее большее число для числа x — это первое большее число, следующее за ним в порядке обхода массива, что означает, что вы можете искать циклически, 
чтобы найти следующее большее число. Если оно не существует, верните -1 для этого числа.
"""

# Input: nums = [1,2,1]
# Output: [2,-1,2]

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        for i in range(n):
            for j in range(1, n):
                if nums[(i + j) % n] > nums[i]:
                    res[i] = nums[(i + j) % n]
                    break
        
        return res
    
if __name__ == "__main__":
    example = Solution()
    result = example.nextGreaterElements(nums = [1,2,1])
    print(result)