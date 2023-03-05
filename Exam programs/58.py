a=int(input("Enter the principal Amount :"))
b=int(input("Enter the no.of years :"))
c=str(input("is Customer senior citizen(y/n) :"))
if c=="y":
    si=a*b*12/100
    print("Interest :",si)
elif c=="n":
    si=a*b*10/100
    print("Interest :",si)
