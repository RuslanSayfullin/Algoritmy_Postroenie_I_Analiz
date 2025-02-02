"""
Дана матрица размером m x n, где каждая ячейка является либо стеной 'W', либо врагом 'E', либо пустой '0'. 
Верните максимальное количество врагов, которых можно уничтожить, используя одну бомбу. 
Вы можете разместить бомбу только в пустой ячейке.
Бомба уничтожает всех врагов в той же строке и столбце от точки установки до тех пор, пока не встретит стену, так как она слишком сильна, чтобы быть разрушенной.
"""

# Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3

class Solution:
    def maxKilledEnemies(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0':
                    hits = self.killEnemies(row, col, grid)
                    max_count = max(max_count, hits)

        return max_count

    def killEnemies(self, row, col, grid):
        enemy_count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            
            while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == 'W':
                    break
                elif grid[r][c] == 'E':
                    enemy_count += 1
                r += dr
                c += dc

        return enemy_count
    
if __name__ == "__main__":
    example = Solution()
    result = example.maxKilledEnemies(grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]])
    print(result)