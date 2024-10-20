# Дан массив целых чисел nums, содержащий n + 1 целых чисел, где каждое число находится в диапазоне [1, n] включительно.
# В массиве есть только одно повторяющееся число, верните это повторяющееся число.
# Вы должны решить задачу, не изменяя массив nums и используя только постоянное дополнительное пространство.


"""
Input: nums = [1,3,4,2,2]
Output: 2
"""

class Solution:
    def findDuplicate(self, nums):
        duplicate = -1
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] *= -1
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return duplicate

if __name__ == "__main__":
    example = Solution()
    result = example.findDuplicate(nums = [1,3,4,2,2])
    print(result)