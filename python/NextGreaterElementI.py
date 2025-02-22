"""
Следующий больший элемент для некоторого элемента x в массиве — это первый больший элемент, который находится справа от x в том же массиве.
Вам даны два различных целочисленных массива с индексами, начинающимися с 0: nums1 и nums2, где nums1 является подмножеством nums2.
Для каждого 0 <= i < nums1.length найдите индекс j, такой что nums1[i] == nums2[j], и определите следующий больший элемент для nums2[j] в nums2. 
Если следующего большего элемента нет, то ответ для этого запроса — -1.
Верните массив ans длиной nums1.length, где ans[i] — это следующий больший элемент, как описано выше.
"""

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    found = True
                if found and nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        
        return res
    
if __name__ == "__main__":
    example = Solution()
    result = example.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
    print(result)