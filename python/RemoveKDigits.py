# Если задана строка num, представляющая неотрицательное целое число num, и целое число k, 
# верните наименьшее возможное целое число после удаления k цифр из num.


"""
Input: num = "1432219", k = 3
Output: "1219"
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        final_stack = stack[:-k] if k else stack
        return ''.join(final_stack).lstrip('0') or '0'

if __name__ == "__main__":
    example = Solution()
    result = example.removeKdigits(num = "1432219", k = 3)
    print(result)