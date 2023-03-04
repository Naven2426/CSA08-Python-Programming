a=int(input("Enter the mark in Python :"))
b=int(input("Enter the mark in C programming :"))
c=int(input("Enter the mark in Mathematics :"))
d=int(input("Enter the mark in Physics :"))
m=a+b+c+d
print("Total =",m)
n=m/4
print("Aggregate =",n)
if n>75:
    print("Distinction")
elif n>=60 and n<75:
    print("First Division")
elif n>=50 and n<60:
    print("Second Division")
elif n>=40 and n<50:
    print("Third Division")
else:
    print("Fail")
