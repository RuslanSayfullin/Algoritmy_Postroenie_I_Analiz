"""
Вам дано целое число n. 
Верните порядок самого большого крестообразного знака из 1, выровненного по осям, который содержится в сетке. 
Если такого знака нет, верните 0.
"""

# Input: N = 5, mines = [[4,2]]
# Output: 2

from typing import List 

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = set()
        for mine in mines:
            banned.add(mine[0] * N + mine[1])
            
        ans = 0
        for r in range(N):
            for c in range(N):
                k = 0
                while k <= r and r < N - k and k <= c and c < N - k and \
                      (r - k) * N + c not in banned and \
                      (r + k) * N + c not in banned and \
                      r * N + c - k not in banned and \
                      r * N + c + k not in banned:
                    k += 1
                ans = max(ans, k)
        return ans
    
if __name__ == "__main__":
    example = Solution()
    result = example.orderOfLargestPlusSign(N = 5, mines = [[4,2]])
    print(result)