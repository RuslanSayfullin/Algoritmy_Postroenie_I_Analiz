# Дан массив двоичных строк strs и два целых числа m и n.
# Верните размер наибольшего подмножества strs, такого что в подмножестве содержится не более m нулей и n единиц.
# Множество x является подмножеством множества y, если все элементы множества x также являются элементами множества y.


"""
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
"""

class Solution:
    def findMaxForm(self, strs, m, n):
        maxlen = 0
        for i in range(1 << len(strs)):
            zeroes, ones, length = 0, 0, 0
            for j in range(32):
                if i & (1 << j):
                    count = self.count_zeroes_ones(strs[j])
                    zeroes += count[0]
                    ones += count[1]
                    if zeroes > m or ones > n:
                        break
                    length += 1
            if zeroes <= m and ones <= n:
                maxlen = max(maxlen, length)
        return maxlen

    def count_zeroes_ones(self, s):
        count = [0, 0]
        for char in s:
            count[int(char)] += 1
        return count

if __name__ == "__main__":
    example = Solution()
    result = example.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3)
    print(result)