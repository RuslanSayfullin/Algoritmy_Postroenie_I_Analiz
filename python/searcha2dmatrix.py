# Напишите эффективный алгоритм, который ищет значение target в матрице целых чисел размером m на n. У этой матрицы есть следующие свойства:
# Целые числа в каждой строке отсортированы по возрастанию слева направо.
# Целые числа в каждом столбце отсортированы по возрастанию сверху вниз.

"""
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
"""

class Solution:
    def binarySearch(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        return False

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            # Проверка матрицы: Перед началом поиска убедитесь, что матрица не пуста и не содержит null.
            return False

        shorterDim = min(len(matrix), len(matrix[0]))
        for i in range(shorterDim):
            if self.binarySearch(matrix, target, i, True) or self.binarySearch(matrix, target, i, False):
                return True
        return False

if __name__ == "__main__":
    example = Solution()
    res = example.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
    print(res)
