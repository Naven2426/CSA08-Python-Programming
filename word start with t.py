stri=input("Enter the string:")
s=stri.split()
count=0
for i in s:
    if (i[0]=='t' or i[0]=='T'):
        count=count+1
print("The words starting with t are:",count)
