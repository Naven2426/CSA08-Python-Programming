a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
ch=int(input("Enter your choice :"))
if ch==1:
    c=a**b
    print("Pow =",c)
elif ch==2:
    c=a+b
    print("Addition =",c)
elif ch==3:
    c=a-b
    print("Subraction =",c)
elif ch==4:
    c=a*b
    print("Multiplication =",c)
elif ch==5:
    c=a/b
    print("Division =",c)
else:
    print("Invalid input")
