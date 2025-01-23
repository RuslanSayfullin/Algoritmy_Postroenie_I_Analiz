"""
У вас есть набор целых чисел s, который изначально содержит все числа от 1 до n. 
К сожалению, из-за какой-то ошибки одно из чисел в s продублировалось в другое число в наборе, 
что привело к повторению одного числа и потере другого. 
Вам дан целочисленный массив nums, представляющий состояние данных в этом наборе после ошибки. 
Найдите число, которое встречается дважды, и число, которое отсутствует, и верните их в виде массива.
"""

# Input: nums = [1,2,2,4]
# Output: [2,3]

def findErrorNums(nums):
    n = len(nums)
    num_set = set()

    duplicate = -1
    for num in nums:
        if num in num_set:
            duplicate = num

        num_set.add(num)

    missing = (n * (n +1)) // 2 - sum(num_set)
    return [duplicate, missing]

if __name__ == "__main__":
    res = findErrorNums(nums = [1, 2, 2, 4])
    print(res)