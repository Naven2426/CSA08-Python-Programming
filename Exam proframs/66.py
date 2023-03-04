input_str = input("Enter a sorted array of integers: ")
arr = [int(x) for x in input_str.split()]
last_element = arr[0]
next_unique_index = 1
for i in range(1, len(arr)):
    if arr[i] != last_element:
        arr[next_unique_index] = arr[i]
        last_element = arr[i]
        next_unique_index += 1
arr = arr[:next_unique_index]
print("Sorted Array =", arr)
