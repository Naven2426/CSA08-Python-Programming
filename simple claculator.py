a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
ch=int(input("Enter the choice :"))
if ch==1:
    c=a+b
    print("sum =",c)
elif ch==2:
    c=a-b
    print("Subraction =",c)
elif ch==3:
    c=a*b
    print("Product =",c)
elif ch==4:
    c=a/b
    print("Quotient =",c)
else:
    print("Invalid input")
