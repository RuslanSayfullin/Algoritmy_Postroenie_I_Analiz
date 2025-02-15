"""
Вам дан массив целых чисел stations, который представляет позиции автозаправочных станций на оси x. Вам также дано целое число k.
Вы должны добавить k новых автозаправочных станций. Вы можете добавлять станции в любое место на оси x, необязательно в целочисленную позицию.
Определим penalty() как максимальное расстояние между соседними автозаправочными станциями после добавления k новых станций.
Верните наименьшее возможное значение penalty(). Ответы, отличающиеся от фактического ответа не более чем на 10^-6, будут приняты.
"""

# Input: stations = [1,2,3,4,5,6,7,8,9,10], K = 9
# Output: 0.50000

from typing import List

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        N = len(stations)
        deltas = [0] * (N-1)
        for i in range(N-1):
            deltas[i] = stations[i+1] - stations[i]

        dp = [[0] * (K+1) for _ in range(N-1)]
        for i in range(K+1):
            dp[0][i] = deltas[0] / (i+1)

        for p in range(1, N-1):
            for k in range(K+1):
                bns = float('inf')
                for x in range(k+1):
                    bns = min(bns, max(deltas[p] / (x+1), dp[p-1][k-x]))
                dp[p][k] = bns

        return dp[N-2][K]
    

if __name__ == "__main__":
    example = Solution()
    result = example.minmaxGasDist(stations = [1,2,3,4,5,6,7,8,9,10], K = 9)
    print(result)