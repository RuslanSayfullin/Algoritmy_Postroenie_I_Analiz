"""
Дана строка, представляющая фрагмент кода, реализуйте валидатор тегов для разбора кода и определения его корректности.
"""

# Input: code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
# Output: true

import re

class Solution:
    def __init__(self):
        self.stack = []
        self.contains_tag = False

    def is_valid_tag_name(self, s, ending):
        if ending:
            if self.stack and self.stack[-1] == s:
                self.stack.pop()
            else:
                return False
        else:
            self.contains_tag = True
            self.stack.append(s)
        return True

    def isValid(self, code: str) -> bool:
        pattern = re.compile(r"<[A-Z]{0,9}>([^<]*(<((\/?[A-Z]{1,9}>)|(!\[CDATA\[.*?\]\]>)))?)*")
        if not pattern.fullmatch(code):
            return False

        i = 0
        while i < len(code):
            ending = False
            if not self.stack and self.contains_tag:
                return False
            if code[i] == '<':
                if code[i + 1] == '!':
                    i = code.find("]]>", i + 1)
                    if i == -1:
                        return False
                    continue
                if code[i + 1] == '/':
                    i += 1
                    ending = True
                close_index = code.find('>', i + 1)
                if close_index == -1 or not self.is_valid_tag_name(code[i + 1:close_index], ending):
                    return False
                i = close_index
            i += 1
        return not self.stack
    
if __name__ == "__main__":
    example = Solution()
    result = example.isValid(code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>")
    print(result)