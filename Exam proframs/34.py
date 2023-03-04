def is_harshad_number(n):
    a=sum(int(b) for b in str(n))
    if n%a==0:
        return True
    else:
        return False
n=int(input("Enter a number: "))
if is_harshad_number(n):
    print(n, "is a Harshad number")
else:
    print(n, "is not a Harshad number")
