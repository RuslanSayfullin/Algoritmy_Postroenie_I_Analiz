# Дана m на n доска символов и список строк words, верните все слова, находящиеся на доске.
# Каждое слово должно быть составлено из букв последовательных смежных ячеек, где смежные ячейки находятся по горизонтали или вертикали рядом. Одна и та же ячейка с буквой не может использоваться более одного раза в слове.

"""
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]

            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)

            board[row][col] = "#"

            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if board[newRow][newCol] not in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            board[row][col] = letter

            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords


if __name__ == "__main__":
    example = Solution()
    result = example.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])
    print(result)       