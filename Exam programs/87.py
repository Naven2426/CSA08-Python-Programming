P = int(input("Enter the starting number: "))
Q = int(input("Enter the ending number: "))
R = int(input("Enter the digit to exclude: "))
for i in range(P, Q+1):
    if str(R) not in str(i):
        print(i, end=", ")
