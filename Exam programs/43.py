a=int(input("Enter the N value :"))
b=int(input("Enter "+str(a)+"Digit Number :"))
n=0
while b!=0:
    n+=b%10
    b//=10
print("Sum of "+str(a)+"digit Number :",n)
