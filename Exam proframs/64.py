import string
text = input("Enter a line of text: ")
special_chars = set(string.punctuation)
num_special_chars = 0
for char in text:
    if char in special_chars:
        print(char)
        num_special_chars += 1
print("Number of special characters:", num_special_chars)
