"""
При наличии массива ключевых слов и строки a выделите все ключевые слова [i] жирным шрифтом. 
Все буквы между тегами <b> и </b> выделяются жирным шрифтом.
Возвращает после добавления тегов, выделенных жирным шрифтом. 
Возвращаемая строка должна содержать как можно меньшее количество тегов, и теги должны образовывать допустимую комбинацию.
"""

# Input: keywords = ["ab","bc"], s = "aabcd"
# Output: "a<b>abc</b>d"

def addBoldTags(keywords, s):
    n = len(s)
    bold = [False] * n
    for word in keywords:
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
    example = addBoldTags(keywords = ["ab","bc"], s = "aabcd")
    print(example)