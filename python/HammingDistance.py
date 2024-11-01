# Расстояние Хэмминга между двумя целыми числами — это количество позиций, в которых соответствующие биты различны.
# Даны два целых числа x и y, верните расстояние Хэмминга между ними.


"""
Input: x = 3, y = 1
Output: 1
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

if __name__ == "__main__":
    example = Solution()
    result = example.hammingDistance(x = 3, y = 1)
    print(result)