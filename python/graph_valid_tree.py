# У вас есть граф из n узлов, помеченных от 0 до n - 1. Вам даны целое число n и список рёбер, где edges[i] = [ai, bi] указывает на то, что существует неориентированное ребро между узлами ai и bi в графе.
# Верните true, если рёбра данного графа образуют допустимое дерево, и false в противном случае.

"""
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
"""

import collections
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        parent = {0: -1}
        queue = collections.deque([0])
        
        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour == parent[node]:
                    continue
                if neighbour in parent:
                    return False
                parent[neighbour] = node
                queue.append(neighbour)
        
        return len(parent) == n


if __name__ == "__main__":
    example = Solution()
    result = example.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]])
    print(result)