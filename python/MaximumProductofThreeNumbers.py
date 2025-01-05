# Задан неотрицательный, целочисленный массив nums, найдите три числа, произведение которых максимально, и верните максимальное произведение.

"""
Input: nums = [1,2,3,4]
Output: 24
"""

def maximumProduct(nums):
    # сортируем массив nums
    nums.sort()
    # Найдите два возможных максимальных произведения: 
    max1 = nums[-1] * nums[-2] * nums[-3]
    return max1

if __name__ == "__main__":
    res = maximumProduct(nums = [1,2,3,4])
    print(res)

