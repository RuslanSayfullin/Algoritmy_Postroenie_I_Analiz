# Дано целое число num. Повторно складывайте все его цифры,
# пока результат не станет однозначным, и верните его.

"""
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num //= 10
            if num == 0 and digital_root > 9:
                num= digital_root
                digital_root = 0
        return digital_root


if __name__ == "__main__":
    example = Solution()
    result = example.addDigits(num = 38)
    print(result)
