"""
Дано n воздушных шаров, пронумерованных от 0 до n - 1. 
Каждый шарик окрашен в число, представленное массивом nums. Вам нужно лопнуть все шарики.
Если вы лопаете шарик i, вы получите nums[i - 1] * nums[i] * nums[i + 1] монет. Если i - 1 или i + 1 выходит за границы массива, 
то считайте, что там находится шарик с числом 1.
Верните максимальное количество монет, которое можно собрать, лопая шарики с умом.
"""

# Input: nums = [1,5]
# Output: 10

from typing import List
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left > right:
                return 0
            max_coins = 0
            for i in range(left, right + 1):
                coins = dp(left, i - 1) + dp(i + 1, right) + nums[left - 1] * nums[i] * nums[right + 1]
                max_coins = max(max_coins, coins)
            return max_coins
        
        return dp(1, n - 2)

if __name__ == "__main__":
    example = Solution()
    result = example.maxCoins(nums = [1,5])
    print(result)