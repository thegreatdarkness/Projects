# Enter a string and the program will reverse it and print it out.

txt = input("Enter string: ")

r = ' '.join(reversed(txt.split(' ')))  # split string, reverse words, join them back into string

print(r)
