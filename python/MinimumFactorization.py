"""
Если задано целое положительное число num, верните наименьшее целое положительное число x, 
умножение каждого разряда которого равно num. 
Если ответа нет или ответ не помещается в 32-битное знаковое целое число, возвращается 0.
"""

# Input: num = 48
# Output: 68

def smallestFactorization(num):
    if num == 1:
        return 1
    
    factors = []
    
    for i in range(9, 1, -1):
        while num % i == 0:
            factors.append(i)
            num //= i
    
    if num > 1:
        return 0
    
    result = 0
    for factor in reversed(factors):
        result = result * 10 + factor
        if result > 2**31 - 1:
            return 0
    
    return result

if __name__ == "__main__":
    result = smallestFactorization(num = 48)
    print(result)