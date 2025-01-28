"""
Если задана строка s, верните количество палиндромных подстрок в ней. Строка является палиндромом, если она читается так же, как задом наперед. 
Подстрока - это непрерывная последовательность символов в строке.
"""

# Input: s = "abc"
# Output: 3

def countSubstrings(s):
    def expandAroundCenter(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total_count = 0
    for i in range(len(s)):
        total_count += expandAroundCenter(i, i)  # For odd length palindromes
        total_count += expandAroundCenter(i, i + 1)  # For even length palindromes
    return total_count

if __name__ == "__main__":
    result = countSubstrings(s = "abc")
    print(result)
