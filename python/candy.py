"""
В очереди стоят n детей. Каждому ребенку присвоено значение рейтинга, указанное в массиве целых чисел ratings.
Вы раздаете конфеты этим детям с соблюдением следующих требований:
Каждый ребенок должен получить как минимум одну конфету.
Дети с более высоким рейтингом должны получать больше конфет, чем их соседи.
Верните минимальное количество конфет, которое вам нужно иметь, чтобы распределить их среди детей.
"""

# Input: ratings = [1,0,2]
# Output: 5

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        sum = 0
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
        for i in range(n):
            sum += max(left2right[i], right2left[i])
        return sum
    
if __name__ == "__main__":
    example = Solution()
    result = example.candy(ratings = [1,0,2])
    print(result)