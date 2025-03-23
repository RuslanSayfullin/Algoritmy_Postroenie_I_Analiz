"""
На двумерной плоскости имеется n точек с целочисленными координатами points[i] = [xi, yi]. 
Верните минимальное время в секундах для посещения всех точек в порядке, заданном точками. 
"""

# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7

def minTimeToVisitAllPoints(points):
    def distance(p1, p2):
        return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

    time = 0
    for i in range(len(points) - 1):
        time += distance(points[i], points[i + 1])
    return time

if __name__ == "__main__":
    result = minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]])
    print(result)