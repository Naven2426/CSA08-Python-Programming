a=int(input("Enter the number to be printed :"))
b=int(input("Max Number of time printed :"))
for i in range(b):
    for j in range(i+1):
        print(a,end=" ")
    print()
for i in range(b-1,0,-1):
    for j in range(i):
        print(a,end=" ")
    print()
