n = int(input("Enter the value of n: "))
odd_count = 0  
num = 1
while odd_count < n:
    if num % 2 == 1:  
        odd_count += 1
    num += 1
nth_odd = num - 1
nth_odd_after_n = nth_odd + 2  
print(f"{n}th Odd number after {n} odd numbers = {nth_odd_after_n}")
