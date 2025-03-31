"""
Дан массив nums из целых положительных чисел. 
Ваша задача - выбрать некоторое подмножество nums, умножить каждый элемент на целое число и сложить все эти числа.
Массив считается хорошим, если из него можно получить сумму, равную 1, при любом возможном подмножестве и множителе. 
Верните True, если массив хороший, иначе верните False.
"""

# Input: nums = [12,5,7,23]
# Output: true

import math
from functools import reduce

def isGoodArray(nums):
    return reduce(math.gcd, nums) == 1

if __name__ == "__main__":
    result = isGoodArray(nums = [12,5,7,23])
    print(result)