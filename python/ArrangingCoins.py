"""
У вас есть n монет, и вы хотите построить лестницу из этих монет. 
Лестница состоит из k рядов, где i-й ряд содержит ровно i монет. Последний ряд лестницы может быть неполным.
Дано целое число n, верните количество полных рядов лестницы, которые вы сможете построить.
"""

# Input: n = 5
# Output: 2

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25)**0.5 - 0.5)
    
if __name__ == "__main__":
    example = Solution()
    result = example.arrangeCoins(n = 5)
    print(result)