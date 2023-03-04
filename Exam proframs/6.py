n=int(input("Enter the number :"))
m=input("enter the Symbol :")
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print(m,end=" ")
        else:
            print(" ",end=" ")
    print()
