"""
Вам дан целочисленный массив score размером n, где score[i] — это результат i-го спортсмена на соревновании. Все результаты гарантированно уникальны.
Спортсмены размещаются на основе своих результатов: спортсмен, занявший 1-е место, имеет наивысший результат, спортсмен, занявший 2-е место, имеет второй по величине результат и так далее. Размещение каждого спортсмена определяет его ранг:
Ранг спортсмена, занявшего 1-е место, — "Gold Medal".
Ранг спортсмена, занявшего 2-е место, — "Silver Medal".
Ранг спортсмена, занявшего 3-е место, — "Bronze Medal".
Для спортсменов, занявших с 4-го по n-е место, их ранг соответствует их номеру в размещении (т.е. ранг спортсмена, занявшего x-е место, — "x").
Верните массив answer размером n, где answer[i] — это ранг i-го спортсмена.
"""

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        max_score = max(score)
        score_to_index = [0] * (max_score + 1)
        
        for i, s in enumerate(score):
            score_to_index[s] = i + 1
        
        MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = [""] * N
        place = 1
        
        for i in range(max_score, -1, -1):
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place < 4:
                    rank[original_index] = MEDALS[place - 1]
                else:
                    rank[original_index] = str(place)
                place += 1
        
        return rank
    
if __name__ == "__main__":
    example = Solution()
    result = example.findRelativeRanks(score = [5,4,3,2,1])
    print(result)