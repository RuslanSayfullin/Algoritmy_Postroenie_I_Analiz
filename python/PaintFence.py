# Вы красите забор из n столбцов, используя k различных цветов. Вы должны красить столбы, следуя этим правилам:
# Каждый столб должен быть окрашен в один цвет.
# Не может быть трех или более подряд идущих столбцов одного цвета.
# Учитывая два целых числа n и k, верните количество способов покрасить забор.

"""
Input: n = 3, k = 2
Output: 6
"""

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        twoPostsBack = k
        onePostBack = k * k
        
        for i in range(3, n + 1):
            curr = (k - 1) * (onePostBack + twoPostsBack)
            twoPostsBack = onePostBack
            onePostBack = curr
        
        return onePostBack

if __name__ == "__main__":
    example = Solution()
    result = example.numWays(n = 3, k = 2)
    print(result)