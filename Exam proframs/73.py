lower_count = 0
upper_count = 0
number_count = 0
while True:
    char = input("Enter any character: ")
    if char == "*":
        break  
    elif char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1
    elif char.isnumeric():
        number_count += 1
print("Total count of lower case: ", lower_count)
print("Total count of upper case: ", upper_count)
print("Total count of numbers: ", number_count)
