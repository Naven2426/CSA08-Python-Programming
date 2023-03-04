n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element " + str(i+1) + ": ")))
count = 0
for num in arr:
    if num < 0:
        count += 1
print("Number of negative numbers in array elements = ", count)
