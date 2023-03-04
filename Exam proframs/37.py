M = int(input("Enter the starting number: "))
N = int(input("Enter the ending number: "))
odd_numbers = []
even_numbers = []
for i in range(M, N+1):
    if i % 2 == 1:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)
print("All Odd Numbers =", ','.join(str(num) for num in odd_numbers))
print("All Even Numbers =", ','.join(str(num) for num in even_numbers))
