# Вам дана строка s и массив строк words. Добавить закрытую пару полужирных тегов <b> и </b>, чтобы обернуть подстроки в s, 
# которые существуют в words. Если две такие подстроки пересекаются, вы должны обернуть их вместе только одной парой закрытых полужирных тегов. 
# Если две подстроки, обернутые полужирными тегами, идут подряд, вы должны объединить их. Верните s после добавления полужирных тегов.

"""
Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"
"""

def addBoldTag(s, words):
    n = len(s)
    bold = [False] * n
    
    for word in words:
        start = s.find(word)
        while start != -1:
            for i in range(start, start + len(word)):
                bold[i] = True
            start = s.find(word, start + 1)
    
    result = []
    i = 0
    while i < n:
        if bold[i]:
            result.append("<b>")
            while i < n and bold[i]:
                result.append(s[i])
                i += 1
            result.append("</b>")
        else:
            result.append(s[i])
            i += 1
    
    return "".join(result)


if __name__ == "__main__":
    result = addBoldTag(s = "abcxyz123", words = ["abc","123"])
    print(result)