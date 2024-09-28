# Дан массив целых чисел nums и целое число k. 
# Верните true, если в массиве существуют два различных индекса i и j, такие что nums[i] == nums[j] и abs(i - j) <= k.

"""
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False

if __name__ == "__main__":
    example = Solution()
    result = example.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
    print(result)