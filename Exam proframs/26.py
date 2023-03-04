def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter the value of N: "))
count = 0
num = 2
while count < n:
    if is_prime(num):
        count += 1
    num += 1
nth_prime = num - 1
print(n,"th prime number is :",nth_prime)
count = 0
num = nth_prime + 1
print(n,"prime numbers after " ,nth_prime," are: ", end="")
while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1
