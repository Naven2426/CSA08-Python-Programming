def count_numbers(m, n):
    odd_count = 0
    even_count = 0    
    for i in range(m, n+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count
m = int(input("Enter the value of M: "))
n = int(input("Enter the value of N: "))
odd_count, even_count = count_numbers(m, n)
print("Number of odd numbers between", m, "and", n, ":", odd_count)
print("Number of even numbers between", m, "and", n, ":", even_count)
