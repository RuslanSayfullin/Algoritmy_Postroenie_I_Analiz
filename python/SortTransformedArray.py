"""
Дан отсортированный массив целых чисел nums и три целых числа a, b и c. 
Примените квадратичную функцию вида f(x) = ax^2 + bx + c к каждому элементу nums[i] в массиве и верните массив в отсортированном порядке.
"""

# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]

class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        transformed = [a * x * x + b * x + c for x in nums]
        self.radix_sort(transformed)
        return transformed

    def radix_sort(self, array):
        max_element = max(abs(num) for num in array)
        place_value = 1

        while max_element // place_value > 0:
            self.counting_sort_by_digit(array, place_value)
            place_value *= 10

        negatives = sorted([x for x in array if x < 0])
        positives = sorted([x for x in array if x >= 0])
        array[:] = negatives + positives

    def counting_sort_by_digit(self, array, place_value):
        output = [0] * len(array)
        count = [0] * 10

        for num in array:
            digit = (abs(num) // place_value) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for num in reversed(array):
            digit = (abs(num) // place_value) % 10
            output[count[digit] - 1] = num
            count[digit] -= 1

        array[:] = output


if __name__ == "__main__":
    example = Solution()
    result = example.sortTransformedArray(nums = [-4,-2,2,4], a = 1, b = 3, c = 5)
    print(result)