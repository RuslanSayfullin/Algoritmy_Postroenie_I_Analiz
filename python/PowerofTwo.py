# Дано целое число n, верните true, если оно является степенью двойки. В противном случае верните false.
# Целое число n является степенью двойки, если существует целое число x, такое что n == 2^x.

"""
Input: n = 1
Output: true
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return (n & -n) == n

if __name__ == "__main__":
    example = Solution()
    result = example.isPowerOfTwo(n = 1)
    print(result)