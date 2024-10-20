# Вам дана сетка размером m x n, представляющая комнаты, инициализированные следующими значениями:
# -1: Стена или препятствие.
# 0: Ворота.
# INF: Бесконечность, обозначающая пустую комнату. Мы используем значение 2^31 - 1 = 2147483647 для представления INF, так как можно предположить, что расстояние до ворот меньше 2147483647.
# Заполните каждую пустую комнату расстоянием до ближайших ворот. Если невозможно добраться до ворот, комната должна быть заполнена значением INF.


"""
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""

from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))
        
        return rooms

if __name__ == "__main__":
    example = Solution()
    result = example.wallsAndGates( rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])
    print(result)