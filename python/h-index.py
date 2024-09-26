"""
Дан массив целых чисел citations, где citations[i] — количество цитирований, которое исследователь получил за свою i-ю статью, и массив отсортирован в порядке возрастания. Верните h-индекс исследователя.
Согласно определению h-индекса на Википедии: h-индекс определяется как максимальное значение h, такое что данный исследователь опубликовал по крайней мере h статей, каждая из которых была процитирована как минимум h раз.
Вы должны написать алгоритм, который работает за логарифмическое время.
"""

"""
Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
"""

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return n - left

if __name__ == "__main__":
    example = Solution()
    result = example.hIndex(citations = [0,1,3,5,6])
    print(result)