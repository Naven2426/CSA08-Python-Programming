n=int(input("Enter the Number of rows :"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("$",end=" ")
        else:
            print(" ",end=" ")
    print()

a=int(input("Enter the no.of rows :"))
b=int(input("Enter the no.of columns :"))
for i in range(a):
    for j in range(b):
        print(" *",end=" ")
    print()
