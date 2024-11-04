# Мы играем в игру "Угадай число". Правила игры следующие:
# Я загадываю число от 1 до n. Вам нужно угадать, какое число я загадал.
# Каждый раз, когда вы угадываете неправильно, я говорю вам, загаданное число больше или меньше вашего предположения.

"""
Input: n = 10, pick = 6
Output: 6
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        low, hign = 1, n 
        while low <= hign:
            mid = low + (hign - low)  // 2
            res = guess(mid)
            if res== 0:
                return mid
            elif res < 0:
                hign = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == "__main__":
    example = Solution()
    result = example.guessNumber(n = 10)
    print(result)