a=int(input("Enter the rows :"))
for i in range(a):
    for j in range(i):
        print(" ", end="")
    for j in range(i*2, a*2-1):
        print("*", end="")
    print()
