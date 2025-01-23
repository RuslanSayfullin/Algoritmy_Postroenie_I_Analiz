# Разработайте систему автозаполнения поиска для поисковой системы.

"""
Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
"""

import collections
import heapq

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = {}
        self.history = collections.defaultdict(int)
        self.keyword = ""

        for i in range(len(sentences)):
            self.history[sentences[i]] += times[i]
            self.add_to_trie(sentences[i])
    
    def add_to_trie(self, sentence):
        node = self.trie
        for char in sentence:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = sentence
    
    def input(self, c):
        if c == '#':
            self.history[self.keyword] += 1
            self.add_to_trie(self.keyword)
            self.keyword = ""
            return []
        
        self.keyword += c
        node = self.trie
        for char in self.keyword:
            if char not in node:
                return []
            node = node[char]

        return self.search_in_trie(node)

    def search_in_trie(self, node):
        pq = []
        self.dfs(node, pq)
        return [item[1] for item in heapq.nsmallest(3, pq)]
    
    def dfs(self, node, pq):
        for char in node:
            if char == '#':
                heapq.heappush(pq, (-self.history[node[char]], node[char]))
            else:
                self.dfs(node[char], pq)


if __name__ == "__main__":
    example = Solution()
    result = example.retrieve([["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]])
    print(result)