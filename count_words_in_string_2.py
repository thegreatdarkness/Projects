# Counts the number of individual words in a string. For added complexity read these strings in from a text file
# and generate a summary.

punctuation = "!?.,"
special_signs = "'"

with open("count_words_in_string_2.txt", 'r') as file:
    txt = file.read()

for char in txt:
    txt = txt.replace(punctuation, " ")
    txt = txt.replace(special_signs, "")

lst = txt.split()
print("The number of words in the file is", len(lst))
file.close()
