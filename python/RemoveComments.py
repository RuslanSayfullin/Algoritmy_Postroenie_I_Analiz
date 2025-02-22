"""
Дана программа на C++, удалите из нее комментарии. Исходный текст программы представляет собой массив строк source, где source[i] - это i-я строка исходного кода. 
Это результат разбиения исходной строки исходного кода символом новой строки '\n'. 
В C++ существует два типа комментариев: строчные и блочные. Строка "//" обозначает строчный комментарий, который означает, 
что он и остальные символы справа от него в той же строке должны игнорироваться. Строка "/*" обозначает блочный комментарий, который означает, 
что все символы до следующего (не перекрывающегося) вхождения "*/" должны игнорироваться. 
(Здесь вхождения происходят в порядке чтения: строка за строкой слева направо.) 
Чтобы было понятно, строка "/*/" еще не завершает блочный комментарий, так как окончание будет перекрывать начало. 
Первый эффективный комментарий имеет приоритет над остальными.
Например, если строка "//" встречается в блочном комментарии, она игнорируется. 
Аналогично, если строка "/*" встречается в строчном или блочном комментарии, она также игнорируется. 
Если после удаления комментариев определенная строка кода оказывается пустой, вы не должны выводить эту строку: каждая строка в списке ответов будет непустой.
"""

# Input: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
# Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

def removeComments(source):
    inBlock = False
    buffer = []
    result = []
    for line in source:
        i = 0
        if not inBlock:
            buffer = []
        while i < len(line):
            if not inBlock and i + 1 < len(line) and line[i:i+2] == "/*":
                inBlock = True
                i += 1
            elif inBlock and i + 1 < len(line) and line[i:i+2] == "*/":
                inBlock = False
                i += 1
            elif not inBlock and i + 1 < len(line) and line[i:i+2] == "//":
                break
            elif not inBlock:
                buffer.append(line[i])
            i += 1
        if buffer and not inBlock:
            result.append("".join(buffer))
    return result

if __name__ == "__main__":
    result = removeComments(source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
    print(result)