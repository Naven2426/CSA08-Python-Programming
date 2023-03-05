import statistics
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)
mean = sum(arr) / n
print("Mean of the array:", mean)
median = statistics.median(arr)
print("Median of the array:", median)
mode = statistics.mode(arr)
print("Mode of the array:", mode)
