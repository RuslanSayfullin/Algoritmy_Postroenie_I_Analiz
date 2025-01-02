"""
Вам дано m массивов, где каждый массив отсортирован по возрастанию. 
Вы можете взять два целых числа из двух разных массивов (каждый массив выбирает одно) и вычислить расстояние. 
Мы определяем расстояние между двумя целыми числами a и b как их абсолютную разность |a - b|. 
Верните максимальное расстояние.
"""

# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4


def maxDistance(arrays):
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    max_distance = 0
    
    for i in range(1, len(arrays)):
        max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(arrays[i][0] - max_val))
        min_val = min(min_val, arrays[i][0])
        max_val = max(max_val, arrays[i][-1])
    
    return max_distance

if __name__ == "__main__":
    result = maxDistance(arrays = [[1,2,3],[4,5],[1,2,3]])
    print(result)