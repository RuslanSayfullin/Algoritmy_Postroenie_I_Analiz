# Дан бинарный массив nums. 
# Верните максимальную длину непрерывного подмассива с равным количеством 0 и 1.

"""
Input: nums = [0,1]
Output: 2
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}
        max_length = 0
        count = 0
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i
        
        return max_length

if __name__ == "__main__":
    example = Solution()
    result = example.findMaxLength(nums = [0,1])
    print(result)