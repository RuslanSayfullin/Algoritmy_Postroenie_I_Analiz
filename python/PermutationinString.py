# Даны две строки s1 и s2. Верните true, если s2 содержит перестановку s1, или false в противном случае.
# Другими словами, верните true, если одна из перестановок s1 является подстрокой s2.

"""
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

from collections import Counter

class Solution():
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Создать массивы для подсчета символов в строках s1 и s2.
        s1Count = Counter(s1)
        s2Count = Counter(s2)
        if s1Count == s2Count:
            return True 

        # Использовать скользящее окно для перемещения по строке s2.
        for i in range(len(s1), len(s2)):
            s2Count[s2[i]] += 1
            s2Count[s2[i - len(s1)]] -= 1
            if s2Count[s2[i - len(s1)]] == 0:
                del s2Count[s2[i - len(s1)]]
            if s1Count == s2Count:
                return True
        
        return False


if __name__ == "__main__":
    example = Solution()
    res = example.checkInclusion(s1 = "ab", s2 = "eidbaooo")
    print(res)