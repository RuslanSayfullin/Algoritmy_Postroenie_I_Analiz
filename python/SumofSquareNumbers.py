# Учитывая целое неотрицательное число c, решите, существуют ли два целых числа a и b такие, что a2 + b2 = c.

"""
Input: c = 5
Output: True
"""

import math

def judgeSquareSum(c: int) -> bool:
    a = 0
    b = int(math.sqrt(c))
    while a <= b:
        total = a * a + b * b
        if total == c:
            return True
        elif total < c:
            a += 1
        else:
            b -= 1
    return False

if __name__ == "__main__":
    result = judgeSquareSum(c = 5)
    print(result)