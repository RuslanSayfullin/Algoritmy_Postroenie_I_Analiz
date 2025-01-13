# Даны две разреженные матрицы mat1 размером m x k и mat2 размером k x n. 
# Вернуть результат перемножения матриц mat1 x mat2. 

"""
Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
"""

from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]],
        mat2: List[List[int]]    
) -> List[List[int]]:
        n = len(mat1)
        k = len(mat1[0])
        m = len(mat2[0])

        # Создайте результирующую матрицу result размером m x n, заполненную нулями.
        ans = [[0] * m for _ in range(n)]
        print(ans)

        for rowIndex in range(n):
            for rowIndex in range(n):
                for elementIndex in range(k):
                    if mat1[rowIndex][elementIndex] != 0:
                        for colIndex in range(m):
                            ans[rowIndex][colIndex] += mat1[rowIndex][elementIndex] * mat2[elementIndex][colIndex]
            
            return ans

if __name__ == "__main__":
    example = Solution()
    res = example.multiply(mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]])
    print(res)