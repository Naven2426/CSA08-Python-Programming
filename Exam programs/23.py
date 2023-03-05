def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
arr = input("Enter the array of elements separated by comma: ").split(",")
arr = [int(i) for i in arr]
count = 0
for num in arr:
    if is_composite(num):
        count += 1
print("Number of composite numbers in the array:", count)
