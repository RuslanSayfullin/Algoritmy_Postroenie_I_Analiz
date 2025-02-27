"""
Совершенное число — это положительное целое число, которое равно сумме своих положительных делителей, исключая само число. 
Делитель целого числа x — это целое число, которое может делить x нацело.
Дано целое число n, верните true, если n является совершенным числом, в противном случае верните false.
"""

# Input: num = 28
# Output: true

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        sum_ = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_ += i
                if i * i != num:
                    sum_ += num // i
        return sum_ - num == num
    
if __name__ == "__main__":
    example = Solution()
    result = example.checkPerfectNumber(num = 28)
    print(result)