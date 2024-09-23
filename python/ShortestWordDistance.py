# Дан массив строк wordsDict и две разные строки, которые уже существуют в массиве: word1 и word2. 
# Верните кратчайшее расстояние между этими двумя словами в списке.


"""
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        minDistance = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                for j in range(len(words)):
                    if words[j] == word2:
                        minDistance = min(minDistance, abs(i - j))
        return minDistance

if __name__ == "__main__":
    example = Solution()
    res = example.shortestDistance( ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice")
    print(res)
