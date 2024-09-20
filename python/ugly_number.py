# Уродливое число — это положительное целое число, простые множители которого ограничены числами 2, 3 и 5.
# Дано целое число n, верните true, если n является уродливым числом.

"""
Input: n = 6
Output: true
Explanation: 6 = 2 × 3
"""

class Solutinon:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            # Если данное целое число n неположительное, возвращаем false, так как неположительное число не может быть уродливым.
            return False
        
        for factor in [2, 3, 5]:
            n = self.keepDividingWhenDivisible(n, factor)
        # Если после всех делений n равно 1, вернём true, иначе вернём false.
        return n == 1

    def keepDividingWhenDivisible(self, dividend: int, divisor: int) -> int:
        # Эта функция будет делить делимое на делитель до тех пор, пока оно делится без остатка. 
        # Функция возвращает измененное делимое. Последовательно примените эту функцию к n с делителями 2, 3 и 5.
        while dividend % divisor == 0:
            dividend //= divisor
        return dividend

if __name__ == "__main__":
    example = Solutinon()
    res = example.isUgly(n = 6)
    print(res)
