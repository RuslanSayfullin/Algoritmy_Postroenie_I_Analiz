# Дан массив целых чисел nums. Верните true, если любое значение появляется в массиве хотя бы дважды, и верните false, если каждый элемент уникален.

"""
Input: nums = [1,2,3,4]
Output: false
"""

def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False



if __name__ == "__main__":
    result = containsDuplicate(nums = [1,2,3,4])
    print(result)