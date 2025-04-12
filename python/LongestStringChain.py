"""
Вам дан массив слов, каждое из которых состоит из строчных английских букв. 
СловоА является предшественником словаВ тогда и только тогда, когда мы можем вставить ровно одну букву в любое место словаА, 
не меняя порядка остальных символов, чтобы оно стало равно словуВ
"""

# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4

def longestStrChain(words):
    words.sort(key=len)
    dp = {}
    longest_chain = 1
    
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]
            if predecessor in dp:
                dp[word] = max(dp[word], dp[predecessor] + 1)
        longest_chain = max(longest_chain, dp[word])
    
    return longest_chain

if __name__ == "__main__":
    result = longestStrChain(words = ["a","b","ba","bca","bda","bdca"])
    print(result)