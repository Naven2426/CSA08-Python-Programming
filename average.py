a=int(input("Enter the mark of First subject :"))
b=int(input("Enter the mark of Second subject :"))
c=int(input("Enter the mark of Third subject :"))
avg=(a+b+c)/3
print("Average is :",avg)
if avg>90 and avg<=100:
    print("Grade is A")
elif avg>80 and avg<=90:
    print("Grade is B")
elif avg>70 and avg<=80:
    print("Grade is C")
elif avg>60 and avg<=70:
    print("Grade is D")
elif avg>50 and avg<=60:
    print("Grade is E")
else:
    print("Grade is F")
