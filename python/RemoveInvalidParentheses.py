# Дана строка s, содержащая скобки и буквы. Удалите минимальное количество неверных скобок, чтобы сделать строку допустимой.
# Верните список уникальных строк, которые являются допустимыми с минимальным количеством удалений. Вы можете вернуть ответ в любом порядке.

"""
Input: s = "()())()"
Output: ["(())()","()()()"]
"""

class Solution:
    def __init__(self):
        self.valid_expressions = set()
        self.minimum_removed = float('inf')

    def reset(self):
        self.valid_expressions.clear()
        self.minimum_removed = float('inf')

    def recurse(self, s, index, left_count, right_count, expression, removed_count):
        if index == len(s):
            if left_count == right_count:
                if removed_count <= self.minimum_removed:
                    possible_answer = "".join(expression)
                    if removed_count < self.minimum_removed:
                        self.valid_expressions.clear()
                        self.minimum_removed = removed_count
                    self.valid_expressions.add(possible_answer)
            return

        current_character = s[index]
        length = len(expression)

        if current_character != '(' and current_character != ')':
            expression.append(current_character)
            self.recurse(s, index + 1, left_count, right_count, expression, removed_count)
            expression.pop()
        else:
            self.recurse(s, index + 1, left_count, right_count, expression, removed_count + 1)
            expression.append(current_character)

            if current_character == '(':
                self.recurse(s, index + 1, left_count + 1, right_count, expression, removed_count)
            elif right_count < left_count:
                self.recurse(s, index + 1, left_count, right_count + 1, expression, removed_count)

            expression.pop()

    def removeInvalidParentheses(self, s: str) -> [str]:
        self.reset()
        self.recurse(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)


if __name__ == "__main__":
    example = Solution()
    result = example.removeInvalidParentheses(s = "()())()")
    print(result)