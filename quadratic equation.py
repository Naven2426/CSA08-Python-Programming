a=int(input("Enter the value of A :"))
b=int(input("Enter the value of B :"))
c=int(input("Enter the value of C :"))
d=b**2+4*a*c
if d==0:
    print("Roots are real and equal")
elif d>0:
    print("Roots are real and Unequal")
else:
    print("Roots are imaginary")
x1=((-1*b)+d**0.5)/(2*a)
x2=((-1*b)-d**0.5)/(2*a)
print("The First root is :",x1)
print("The First root is :",x2)
