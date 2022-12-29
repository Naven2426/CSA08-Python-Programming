n=input("Enter the string :")
a=0
for i in n:
    if i in '!@#$%^&*()<>}{"~| ':
        a=a+1
print("The number special character in given string:",a) 
