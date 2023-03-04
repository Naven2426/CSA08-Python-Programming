def is_perfect(num):
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)
    return sum(divisors) == num 
def first_n_perfect_numbers(n):
    count = 0
    num = 2
    while count < n:
        if is_perfect(num):
            print(num)
            count += 1
        num += 1
n = int(input("Enter the value of n: "))
print("The first", n, "perfect numbers are:")
first_n_perfect_numbers(n)
