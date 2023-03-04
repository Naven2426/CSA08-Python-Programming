try:
    a=int(input("Enter the Number :"))
    n=0
    c=a
    while a!=0:
        n+=(a%10)**3
        a//=10
    if c==n:
        print("Given Number is Armstrong number")
    else:
        print("Given Number is Not Armstrong number")
except:
    print("Invalid input")
