# Вам дан массив строк под названием tokens, который представляет арифметическое выражение в обратной польской нотации.
# Вычислите это выражение. Верните целое число, которое представляет значение этого выражения.

"""
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a/b),
            "*": lambda a, b: a * b,
        }

        current_position = 0

        while len(tokens) > 1:
            while tokens[current_position] not in "+-*/":
                current_position  += 1

            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])

            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)

            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1

        return int(tokens[0])