num_elements = int(input("Enter the number of elements in list:"))
elements = [int(input(f"Enter element{i+1}:")) for i in range(num_elements)]
unique_elements = list(set(elements))
print("Non-duplicate items:")
print(unique_elements)
