# Хэммингово расстояние между двумя целыми числами — это количество позиций, в которых соответствующие биты отличаются.
# Дан целочисленный массив nums, верните сумму Хэмминговых расстояний между всеми парами чисел в nums.

"""
Input: nums = [4,14,2]
Output: 6
"""

class Solution:
    def totalHammingDistance(self, nums):
        ans = 0
        
        if not nums:
            return ans
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                ans += bin(nums[i] ^ nums[j]).count('1')
        
        return ans


if __name__ == "__main__":
    example = Solution()
    result = example.totalHammingDistance(nums = [4,14,2])
    print(result)