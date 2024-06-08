import re

curse_words = ["foo", "bar", "baz"]
comment = "This string contains a foo word."
curse_count = 0

for word in curse_words:
    if re.search(word, comment):
        curse_count += 1
print("Comment has " + str(curse_count) + " curse word(s).")
