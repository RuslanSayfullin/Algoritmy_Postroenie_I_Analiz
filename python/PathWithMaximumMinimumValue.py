"""
Дана целочисленная матрица grid размером m x n. 
Верните максимальное значение пути, начинающегося в (0, 0) и заканчивающегося в (m - 1, n - 1), двигаясь в 4 кардинальных направлениях.
Значение пути определяется минимальным числом на этом пути.
"""

# Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
# Output: 4

from collections import deque
from typing import List

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        def pathExists(curScore):
            R, C = len(grid), len(grid[0])
            visited = [[False] * C for _ in range(R)]
            dq = deque([(0, 0)])
            visited[0][0] = True

            def push(row, col):
                if 0 <= row < R and 0 <= col < C and not visited[row][col] and grid[row][col] >= curScore:
                    dq.append((row, col))
                    visited[row][col] = True

            while dq:
                curRow, curCol = dq.popleft()
                if curRow == R - 1 and curCol == C - 1:
                    return True

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    push(curRow + dr, curCol + dc)

            return False

        curScore = min(grid[0][0], grid[-1][-1])
        while curScore >= 0:
            if pathExists(curScore):
                return curScore
            curScore -= 1
        return -1
    

if __name__ == "__main__":
    example = Solution()
    result = example.maximumMinimumPath(grid = [[5,4,5],[1,2,6],[7,4,6]])
    print(result)