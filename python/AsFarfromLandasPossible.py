"""
Дана сетка размером n x n, содержащая только значения 0 и 1, где 0 представляет воду, а 1 представляет землю. 
Найдите ячейку с водой, такое что её расстояние до ближайшей ячейки с землёй максимально, и верните это расстояние. Если в сетке нет ни земли, ни воды, верните -1.
Расстояние, используемое в этой задаче, - это манхэттенское расстояние: расстояние между двумя ячейками (x0, y0) и (x1, y1) равно |x0 - x1| + |y0 - y1|.
"""

# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2

from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [row[:] for row in grid]
        q = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        distance = -1
        while q:
            qSize = len(q)
            for _ in range(qSize):
                landCell = q.popleft()
                for dir in directions:
                    x, y = landCell[0] + dir[0], landCell[1] + dir[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visited[x][y] == 0:
                        visited[x][y] = 1
                        q.append((x, y))
            distance += 1
        
        return -1 if distance == 0 else distance
    
    
if __name__ == "__main__":
    example = Solution()
    result = example.maxDistance(grid = [[1,0,1],[0,0,0],[1,0,1]])
    print(result)