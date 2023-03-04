def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
arr = input("Enter the array of numbers separated by space: ").split()
arr = [int(x) for x in arr]
prime_nums = []
for num in arr:
    if is_prime(num):
        prime_nums.append(num)
print("Prime numbers in Array elements =", prime_nums)
