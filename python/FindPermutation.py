# Перестановка perm из n целых чисел всех чисел в диапазоне [1, n] может быть представлена в виде строки s длиной n - 1, где:
# s[i] == 'I', если perm[i] < perm[i + 1], и
# s[i] == 'D', если perm[i] > perm[i + 1].
# Дана строка s, восстановите лексикографически наименьшую перестановку perm и верните её.

"""
Input: s = "I"
Output: [1,2]
"""

from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = [0] * (len(s) + 1)
        stack = []
        j = 0
        for i in range(1, len(s) + 1):
            if s[i - 1] == 'I':
                stack.append(i)
                while stack:
                    res[j] = stack.pop()
                    j += 1
            else:
                stack.append(i)
        stack.append(len(s) + 1)
        while stack:
            res[j] = stack.pop()
            j += 1
        return res


if __name__ == "__main__":
    example = Solution()
    result = example.findPermutation( s = "I")
    print(result)