from difflib import SequenceMatcher

s = SequenceMatcher(lambda x: x==" ", "Мама мыла раму", "Мама мыла малину")
print("difflib: ", s.ratio())
