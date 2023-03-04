a=int(input("Enter the income :"))
if a<=150000:
    print("No Tax")
elif a>150001 and a<300000:
    b=(a/100)*10
    print("Tax =",b)
elif a>300001 and a<500000:
    b=(a/100)*20
    print("Tax =",b)
elif a>500001:
    b=(a/100)*30
    print("Tax =",b)
else:
    print("Invalid")

