"""
Если задан массив строк words, представляющих английский словарь, верните самое длинное слово из words, 
которое может быть построено по одному символу из других слов из words. 
Если существует более одного возможного ответа, верните самое длинное слово с наименьшим лексикографическим порядком. 
Если ответа нет, верните пустую строку. Обратите внимание, 
что слово должно строиться слева направо, причем каждый дополнительный символ добавляется в конец предыдущего слова.
"""

# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"

def longestWord(words):
    words.sort()
    valid_words = {""}
    longest = ""
    for word in words:
        if word[:-1] in valid_words:
            valid_words.add(word)
            if len(word) > len(longest):
                longest = word
    return longest

if __name__ == "__main__":
    result = longestWord(words = ["w","wo","wor","worl","world"])
    print(result)