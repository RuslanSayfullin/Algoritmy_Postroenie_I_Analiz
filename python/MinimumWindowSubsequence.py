"""
Если в строках s1 и s2 нет такого окна, которое покрывало бы все символы в s2, верните пустую строку "". 
Если таких окон минимальной длины несколько, возвращается окно с самым левым начальным индексом.
"""

# Input: s1 = "abcdebdde", s2 = "bde"
# Output: "bcde"

from collections import Counter, defaultdict

def minWindow(s1, s2):
    if not s1 or not s2:
        return ""

    dict_t = Counter(s2)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = defaultdict(int)
    ans = float("inf"), None, None

    while r < len(s1):
        character = s1[r]
        window_counts[character] += 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s1[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s1[ans[1]: ans[2] + 1]

if __name__ == "__main__":
    example = minWindow(s1 = "abcdebdde", s2 = "bde")
    print(example)