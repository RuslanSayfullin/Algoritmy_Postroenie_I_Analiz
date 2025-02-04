"""
Дана матрица размером m x n, где каждая ячейка является либо стеной 'W', либо врагом 'E', либо пустой '0'. 
Верните максимальное количество врагов, которых можно уничтожить, используя одну бомбу. 
Вы можете разместить бомбу только в пустой ячейке.
Бомба уничтожает всех врагов в той же строке и столбце от точки установки до тех пор, пока не встретит стену, так как она слишком сильна, чтобы быть разрушенной.
"""

# Input ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"] [[], [1], [2], [3], [4], [300], [300], [301]]
# Output [null, null, null, null, 3, null, 4, 3]

from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)
    
if __name__ == "__main__":
    example = HitCounter()
    result = example.getHits(["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"] [[], [1], [2], [3], [4], [300], [300], [301]])
    print(result)