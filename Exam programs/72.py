M = int(input("Enter the starting number (M): "))
N = int(input("Enter the ending number (N): "))
K = int(input("Enter the number of elements to skip (K): "))
for num in range(M, N+1, K+1):
    print(num, end=", ")
