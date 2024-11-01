# Вычислить а^b mod 1337, где a - положительное число, а b - чрезвычайно большое положительное целое число, заданное в виде массива.

"""
Input: a = 2, b = [3]
Output: 8
"""

from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def powmod(x, y, mod):
            result = 1
            x = x % mod
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % mod 
                y = y // 2
                x = (x * x) % mod 
            return result

        def superPowHelper(a, b, mod):
            if not b:
                return 1

            last_digit = b.pop()
            part1 = powmod(a, last_digit, mod)
            part2 = powmod(superPowHelper(a, b, mod), 10, mod)
            return (part1 * part2) % mod

        return superPowHelper(a, b, MOD)

if __name__ == "__main__":
    example = Solution()
    result = example.superPow(a = 2, b = [3])
    print(result)