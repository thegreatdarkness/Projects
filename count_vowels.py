# Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum
# of each vowel found.

vowels = ["a", "e", "i", "o", "u", "y"]

string = input("Enter a sentence: ")
string_lower = string.lower()

count = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count_y = 0

for letter in string_lower:
    if letter in vowels:
        count += 1
    if letter in vowels[0]:
        count_a += 1
    if letter in vowels[1]:
        count_e += 1
    if letter in vowels[2]:
        count_i += 1
    if letter in vowels[3]:
        count_o += 1
    if letter in vowels[4]:
        count_u += 1
    if letter in vowels[4]:
        count_y += 1

print("Total vowels: ", count)
print("a =", count_a)
print("e =", count_e)
print("i =", count_i)
print("o =", count_o)
print("u =", count_u)
print("y =", count_y)
