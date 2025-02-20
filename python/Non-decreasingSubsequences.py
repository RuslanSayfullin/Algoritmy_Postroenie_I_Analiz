"""
Дан массив целых чисел nums. 
Верните все возможные различные неубывающие подпоследовательности данного массива, содержащие как минимум два элемента. 
Вы можете вернуть ответ в любом порядке.
"""

# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sequence = []
        self.backtrack(nums, 0, sequence, result)
        return list(result)

    def backtrack(self, nums, index, sequence, result):
        if index == len(nums):
            if len(sequence) >= 2:
                result.add(tuple(sequence))
            return
        if not sequence or sequence[-1] <= nums[index]:
            sequence.append(nums[index])
            self.backtrack(nums, index + 1, sequence, result)
            sequence.pop()
        self.backtrack(nums, index + 1, sequence, result)

if __name__ == "__main__":
    example = Solution()
    result = example.findSubsequences(nums = [4,6,7,7])
    print(result)