"""
Дана строка s, переставьте символы строки s так, чтобы любые два соседних символа не были одинаковыми.
Верните любую возможную перестановку строки s или верните "", если это невозможно.
"""

# Input: s = "aab"
# Output: "aba"

import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        charCounts = [0] * 26
        for c in s:
            charCounts[ord(c) - ord('a')] += 1
        
        pq = []
        for i in range(26):
            if charCounts[i] > 0:
                heapq.heappush(pq, (-charCounts[i], chr(i + ord('a'))))
        
        result = []
        while pq:
            first = heapq.heappop(pq)
            if not result or first[1] != result[-1]:
                result.append(first[1])
                if -first[0] > 1:
                    heapq.heappush(pq, (first[0] + 1, first[1]))
            else:
                if not pq:
                    return ""
                second = heapq.heappop(pq)
                result.append(second[1])
                if -second[0] > 1:
                    heapq.heappush(pq, (second[0] + 1, second[1]))
                heapq.heappush(pq, first)
        
        return "".join(result)
    

if __name__ == "__main__":
    example = Solution()
    result = example.reorganizeString(s = "aab")
    print(result)