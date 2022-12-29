stri=input("Enter the string:")
s=stri.split()
count=0
for i in s:
    if (i[-1]=='a' or i[0]=='A'):
        count=count+1
print("The words Ending with A are:",count)
