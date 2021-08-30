# Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards
# like “racecar”

txt = input("Enter your word: ")
txt_rev = ''.join(reversed(txt))

if txt == txt_rev:
    print("'"+ txt + "'", "is a palindrome.")
else:
    print("'"+ txt + "'", "is not a palindrome.")
