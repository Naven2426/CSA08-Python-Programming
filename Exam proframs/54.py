try:
    n=int(input("Enter the year :"))
    if n>0:
        if n%4==0:
            print(n,"Is a Leap Year")
        else:
            print(n,"Is not a Leap Year")
            print("Leap year = ",(n//4)*4)
    else:
        print("Invalid input")
except:
    print("Invalid Input")
