num = int(input("Enter a number: "))
while num > 9:
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    num = sum
print("Sum of digits: ", num)
