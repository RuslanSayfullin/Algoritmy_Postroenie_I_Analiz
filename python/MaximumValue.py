"""
Даны три положительных целых числа: n, index и maxSum. Вам нужно построить массив nums (индексация с нуля), который удовлетворяет следующим условиям:
- nums.length == n
- nums[i] является положительным целым числом, где 0 <= i < n.
- abs(nums[i] - nums[i+1]) <= 1, где 0 <= i < n-1.
- Сумма всех элементов массива nums не превышает maxSum.
- nums[index] максимально возможен.

Верните значение nums[index] в построенном массиве.
Обратите внимание, что abs(x) равно x, если x >= 0, и -x в противном случае.
"""

# Input: n = 4, index = 2,  maxSum = 6
# Output: 2

class Solution:
    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        return count - value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left

if __name__ == "__main__":
    example = Solution()
    result = example.getSum(n = 4, index = 2,  maxSum = 6)
    print(result)