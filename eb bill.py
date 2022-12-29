n=int(input("Enter the unit:"))
if n<=100:
    c=n*3.46
    print(c)
elif n>=101 and n<=500:
    c=n*7.43
    print(c)
elif n>=501:
    c=n*10.32
    print(c)
else:
    print("Invalid input")
