"""
Дан целочисленный массив nums. Вернуть количество непустых подмассивов, в которых левый элемент не больше других элементов подмассива.
"""

# Input: nums = [1,4,2,5,3]
# Output: 11

from typing import List 

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        st = []
        
        for i in range(len(nums)):
            while st and nums[i] < nums[st[-1]]:
                ans += (i - st.pop())
            st.append(i)
        
        while st:
            ans += (len(nums) - st.pop())
        
        return ans
    
if __name__ == "__main__":
    example = Solution()
    result = example.validSubarrays(nums = [1,4,2,5,3])
    print(result)