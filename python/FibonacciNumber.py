"""
Числа Фибоначчи, обычно обозначаемые как F(n), образуют последовательность, называемую последовательностью Фибоначчи, 
так что каждое число является суммой двух предыдущих, начиная с 0 и 1. То есть,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), для n > 1.
Дано n, вычислите F(n).
"""

# Input: N = 28
# Output: 2

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        current, prev1, prev2 = 0, 1, 0
        for _ in range(2, N + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        return current
    
if __name__ == "__main__":
    example = Solution()
    result = example.fib(N = 28)
    print(result)