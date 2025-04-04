"""
Дан целочисленный массив arr, посчитайте, сколько элементов x в нем есть таких, что x + 1 также находится в arr. 
Если в arr есть дубликаты, считайте их отдельно.
"""

# Input: arr = [1,2,3]
# Output: 2

from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        def integerInArray(arr, target):
            for x in arr:
                if x == target:
                    return True
            return False
        
        count = 0
        for x in arr:
            if integerInArray(arr, x + 1):
                count += 1
        return count
    
if __name__ == "__main__":
    example = Solution()
    result = example.countElements(arr = [1,2,3])
    print(result)