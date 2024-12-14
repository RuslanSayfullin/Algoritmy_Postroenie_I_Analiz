# Если задан целочисленный массив nums, верните третье максимальное число в этом массиве.
# Если третьего максимального числа не существует, верните максимальное число.

"""
Input: nums = [3,2,1]
Output: 1
"""

def thirdMax(nums):
    first = second = third = None
    
    for num in nums:
        if num in (first, second, third):
            continue
        if first is None or num > first:
            third = second
            second = first
            first = num
        elif second is None or num > second:
            third = second
            second = num
        elif third is None or num > third:
            third = num
    
    return third if third is not None else first

if __name__ == "__main__":
    result = thirdMax(nums = [3,2,1])
    print(result)