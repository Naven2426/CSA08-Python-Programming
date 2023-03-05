input_str = input("Enter a string: ")
vowels = "aeiouAEIOU"
result_str = ""
for char in input_str:
    if char not in vowels:
        result_str += char
print("String after removing vowels: ", result_str)
