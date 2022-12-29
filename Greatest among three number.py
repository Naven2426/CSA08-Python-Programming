a=int(input("Enter the First Number :"))
b=int(input("Enter the Second Number :"))
c=int(input("Enter the Third Number :"))
if a>b and a>c:
    print("The greatest number is : ",a)
elif b>a and b>c:
    print("The greatest number is : ",b)
else:
    print("The greatest number is : ",c)
