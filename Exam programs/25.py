def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
composite_nums = []
for num in range(a, b+1):
    if not is_prime(num) and num > 1:
        composite_nums.append(num)
print("Composite numbers between", a, "and", b, "are:", composite_nums)
