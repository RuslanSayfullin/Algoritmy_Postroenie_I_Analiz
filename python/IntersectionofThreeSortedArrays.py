"""
Даны три целочисленных массива arr1, arr2 и arr3, отсортированных в строго возрастающем порядке. 
Верните отсортированный массив, содержащий только те целые числа, которые присутствуют во всех трех массивах.
"""

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]

from collections import Counter

class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        counter = Counter(arr1) + Counter(arr2) + Counter(arr3)
        return [num for num, freq in counter.items() if freq == 3]
    
if __name__ == "__main__":
    example = Solution()
    result = example.arraysIntersection(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8])
    print(result)