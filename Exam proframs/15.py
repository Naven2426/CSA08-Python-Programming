n=int(input("Enter the rows :"))
b=1
for i in range(n):
    for j in range(1,i+1):
        print((b**2)/100,end=" ")
        b+=1
    print()
