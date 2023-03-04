lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))
lst = [(i, i**2) for i in range(lower_range, upper_range+1)]
print(lst)
