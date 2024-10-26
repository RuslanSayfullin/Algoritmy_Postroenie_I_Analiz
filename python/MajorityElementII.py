# Дан массив целых чисел размера n, найдите все элементы, которые встречаются более ⌊ n/3 ⌋ раз.

"""
Input: nums = [3,2,3]
Output: [3]
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        
        for n in nums:
            if candidate1 is not None and candidate1 == n:
                count1 += 1
            elif candidate2 is not None and candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for n in nums:
            if candidate1 == n:
                count1 += 1
            if candidate2 == n:
                count2 += 1
        
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        return result

if __name__ == "__main__":
    example = Solution()
    result = example.majorityElement(nums = [3,2,3])
    print(result)