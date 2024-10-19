# Дана строка num, содержащая только цифры, и целое число target. 
# Верните все возможные варианты вставки бинарных операторов '+', '-', и/или '*' между цифрами строки num так, чтобы результирующее выражение вычислялось в значение target.
# Учтите, что операнды в возвращаемых выражениях не должны содержать ведущих нулей.

"""
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
"""

class Solution:
    def __init__(self):
        self.answer = []
        self.digits = ""
        self.target = 0

    def recurse(self, index, previous_operand, current_operand, value, ops):
        if index == len(self.digits):
            if value == self.target and current_operand == 0:
                self.answer.append("".join(ops[1:]))
            return

        current_operand = current_operand * 10 + int(self.digits[index])
        str_operand = str(current_operand)

        if current_operand > 0:
            self.recurse(index + 1, previous_operand, current_operand, value, ops)

        ops.append("+")
        ops.append(str_operand)
        self.recurse(index + 1, current_operand, 0, value + current_operand, ops)
        ops.pop()
        ops.pop()

        if ops:
            ops.append("-")
            ops.append(str_operand)
            self.recurse(index + 1, -current_operand, 0, value - current_operand, ops)
            ops.pop()
            ops.pop()

            ops.append("*")
            ops.append(str_operand)
            self.recurse(index + 1, current_operand * previous_operand, 0, value - previous_operand + (current_operand * previous_operand), ops)
            ops.pop()
            ops.pop()

    def addOperators(self, num, target):
        if not num:
            return []

        self.target = target
        self.digits = num
        self.answer = []
        self.recurse(0, 0, 0, 0, [])
        return self.answer



if __name__ == "__main__":
    example = Solution()
    result = example.addOperators(num = "232", target = 8)
    print(result)