"""
У вас есть k списков отсортированных целых чисел в неубывающем порядке. 
Найдите наименьший диапазон, в который входит хотя бы одно число из каждого из k списков. 
Мы определяем, что диапазон [a, b] меньше диапазона [c, d], если b - a < d - c или a < c, если b - a == d - c.
"""

# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]

from heapq import heappop, heappush

def smallestRange(nums):
    # массив для хранения текущих индексов каждого списка
    min_heap = []
    max_value = float('-inf')
    
    for i in range(len(nums)):
        heappush(min_heap, (nums[i][0], i, 0))
        max_value = max(max_value, nums[i][0])
    
    range_start, range_end = float('-inf'), float('inf')
    
    while len(min_heap) == len(nums):
        min_value, row, col = heappop(min_heap)
        
        if max_value - min_value < range_end - range_start:
            range_start, range_end = min_value, max_value
        
        if col + 1 < len(nums[row]):
            heappush(min_heap, (nums[row][col + 1], row, col + 1))
            max_value = max(max_value, nums[row][col + 1])
    
    return [range_start, range_end]

if __name__ == "__main__":
    result = smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
    print(result)
