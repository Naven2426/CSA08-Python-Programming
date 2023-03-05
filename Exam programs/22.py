def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = input("Enter a list of numbers separated by space: ").split()
prime_count = 0
composite_count = 0
for num in numbers:
    num = int(num)
    if is_prime(num):
        prime_count += 1
    else:
        composite_count += 1
print("Number of prime numbers:", prime_count)
print("Number of composite numbers:", composite_count)
