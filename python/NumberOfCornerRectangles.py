"""
Дан указатель на начало односвязного списка и два целых числа left и right, где left <= right. 
Необходимо перевернуть узлы списка, начиная с позиции left и заканчивая позицией right, и вернуть измененный список.
"""

# Input: grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
# Output: 1

def countCornerRectangles(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            num_pairs = 0
            for k in range(len(grid[0])):
                if grid[i][k] == 1 and grid[j][k] == 1:
                    num_pairs += 1
            if num_pairs > 1:
                count += num_pairs * (num_pairs - 1) // 2
    return count

if __name__ == "__main__":
    example = countCornerRectangles(grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]])
    print(example)