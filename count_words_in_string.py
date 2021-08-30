# Counts the number of individual words in a string.

string = input("Enter your string: ")
delete_char = "!?."

for char in delete_char:
    string = string.replace(char, "")

lst = string.split()

print("The number of words in string is:", len(lst))
